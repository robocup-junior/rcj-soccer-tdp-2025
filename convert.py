#!/usr/bin/env python3

import csv
import sys
import os
import re
import requests
import fcntl
import time
from multiprocessing import Pool, cpu_count

from PIL import Image
from io import BytesIO

# Add HEIF format support
try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HEIF_SUPPORT = True
except ImportError:
    HEIF_SUPPORT = False
    print("[INFO] pillow-heif not installed. HEIF images will not be supported.")

csv.field_size_limit(sys.maxsize)

# Output directory for markdown files
OUTPUT_DIR = 'md_out'
IMAGE_DIR = os.path.join(OUTPUT_DIR, 'images')
FAILED_IMAGES_FILE = os.path.join(OUTPUT_DIR, 'failed_images.txt')
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(IMAGE_DIR, exist_ok=True)

# Load failed image IDs
def load_failed_images():
    failed_images = set()
    if os.path.exists(FAILED_IMAGES_FILE):
        try:
            with open(FAILED_IMAGES_FILE, 'r') as f:
                for line in f:
                    failed_images.add(line.strip())
        except Exception as e:
            print(f"[WARN] Could not load failed images file: {e}")
    return failed_images

# Save failed image ID
def save_failed_image(file_id):
    try:
        with open(FAILED_IMAGES_FILE, 'a') as f:
            f.write(f"{file_id}\n")
    except Exception as e:
        print(f"[WARN] Could not save failed image ID {file_id}: {e}")

# Load set of failed image IDs
FAILED_IMAGES = load_failed_images()

# Header summary list (English)
SUMMARY_HEADERS = [
    "Timestamp", "Team Name", "League", "Country", "Contact", "Social Media", "Team Photo", "Members & Roles", "Meeting Frequency", "Meeting Place", "Start Date", "Past Competitions", "Mentor Contribution", "Workload Management", "AI Tools", "Robot1 Overall", "Robot1 Front", "Robot1 Back", "Robot1 Top", "Robot1 Bottom", "Robot1 Right", "Robot1 Left", "Positioning & Movement", "Robot2 Overall", "Robot2 Front", "Robot2 Back", "Robot2 Top", "Robot2 Bottom", "Robot2 Right", "Robot2 Left", "Mechanical Design", "Build Method", "Motors & Reason", "Kicker Design", "Dribbler Design", "CAD Files", "Mechanical Innovation", "Mechanical Photos", "Electronics Block Diagram", "Power Circuit", "Motor Drive Circuit", "Microcontroller & Reason", "Ball Detection", "Line Detection", "Navigation/Position Sensors", "Kicker Circuit", "Dribbler Circuit", "Schematics", "PCB", "Innovation", "Circuit Photos", "Motor Control", "Ball Detection Method", "Ball Catch Algorithm", "Line Algorithm", "Goal Algorithm", "Defense Algorithm", "Robot Communication", "Innovation2", "GitHub Link", "BOM", "Cost", "Funding", "Affordability", "Answer Check", "Publication Consent", "Email Address", "TDP File", "Extra Column"
]

def sanitize_filename(name):
    # Remove or replace characters not allowed in filenames
    return re.sub(r'[^\w\-_\. ]', '_', name)

def compress_image_if_needed(file_path, max_size_mb=1):
    """Compress image if file size exceeds specified limit"""
    try:
        # Check file size (in bytes)
        file_size = os.path.getsize(file_path)
        max_size_bytes = max_size_mb * 1024 * 1024
        
        if file_size <= max_size_bytes:
            return file_path  # No compression needed
        
        # Say "Compressing image..."
        print(f"Compressing image {file_path}...")

        # Load image
        img = Image.open(file_path)
        
        # Adjust compression quality and save
        if file_path.lower().endswith('.jpg'):
            # For JPEG, reduce quality for compression
            quality = 85
            while quality > 10:
                img.save(file_path, 'JPEG', quality=quality, optimize=True)
                if os.path.getsize(file_path) <= max_size_bytes:
                    break
                quality -= 10
        else:
            
            # Reduce size for compression
            original_size = img.size
            scale_factor = 0.9
            while scale_factor > 0.3:
                new_size = (int(original_size[0] * scale_factor), int(original_size[1] * scale_factor))
                resized_img = img.resize(new_size, Image.Resampling.LANCZOS)
                resized_img.save(file_path, 'PNG', optimize=True, pnginfo=None)
                if os.path.getsize(file_path) <= max_size_bytes:
                    break
                scale_factor -= 0.1
        
        final_size = os.path.getsize(file_path)
        if final_size > max_size_bytes:
            print(f"[WARN] Could not compress {file_path} below {max_size_mb}MB (final size: {final_size/1024/1024:.1f}MB)")
        
        return file_path
        
    except Exception as e:
        print(f"[WARN] Error compressing {file_path}: {e}")
        return file_path

def download_and_convert_drive_image(file_id, force_jpeg=False):
    # Download from Google Drive (public files only)
    url = f'https://drive.google.com/uc?export=download&id={file_id}'
    
    # Skip if image ID is in failed list
    if file_id in FAILED_IMAGES:
        return None
    
    # First, check both JPEG and PNG possibilities
    jpg_path = os.path.join(IMAGE_DIR, f'{file_id}.jpg')
    png_path = os.path.join(IMAGE_DIR, f'{file_id}.png')
    
    # Return existing file if it exists
    if os.path.exists(jpg_path):
        return jpg_path
    if os.path.exists(png_path):
        # If force_jpeg is True and PNG exists, convert it to JPEG
        if force_jpeg:
            try:
                print(f"[INFO] Converting PNG to JPEG for {file_id}...")
                img = Image.open(png_path)
                img = img.convert('RGB')
                img.save(jpg_path, 'JPEG', quality=95)
                compress_image_if_needed(jpg_path, max_size_mb=1)
                # Remove original PNG file after successful conversion
                os.remove(png_path)
                print(f"[INFO] Removed original PNG file for {file_id}")
                return jpg_path
            except Exception as e:
                print(f"[WARN] Could not convert PNG to JPEG for {file_id}: {e}")
        return png_path
    
    # Create lock file to prevent duplicate downloads
    lock_file = os.path.join(IMAGE_DIR, f'{file_id}.lock')
    try:
        with open(lock_file, 'w') as f:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
            
            # Check existence again after acquiring lock (another process might have created it)
            if os.path.exists(jpg_path):
                return jpg_path
            if os.path.exists(png_path):
                # If force_jpeg is True and PNG exists, convert it to JPEG
                if force_jpeg:
                    try:
                        print(f"[INFO] Converting PNG to JPEG for {file_id}...")
                        img = Image.open(png_path)
                        img = img.convert('RGB')
                        img.save(jpg_path, 'JPEG', quality=95)
                        compress_image_if_needed(jpg_path, max_size_mb=1)
                        # Remove original PNG file after successful conversion
                        os.remove(png_path)
                        print(f"[INFO] Removed original PNG file for {file_id}")
                        return jpg_path
                    except Exception as e:
                        print(f"[WARN] Could not convert PNG to JPEG for {file_id}: {e}")
                return png_path
            
            try:
                resp = requests.get(url, stream=True, timeout=30)
                resp.raise_for_status()
                img = Image.open(BytesIO(resp.content))
                
                # Detect original image format
                original_format = img.format
                
                # Force JPEG conversion for team photos and robot photos
                if force_jpeg:
                    # Save as JPEG format for team photos and robot photos
                    img = img.convert('RGB')  # JPEG uses RGB format
                    img.save(jpg_path, 'JPEG', quality=95)
                    # Compress if over 1MB
                    compress_image_if_needed(jpg_path, max_size_mb=1)
                    return jpg_path
                
                # Determine save format based on compression method for other images
                if original_format in ['JPEG', 'JPG', 'JFIF']:
                    # Save as JPEG format for JPEG-based images
                    img = img.convert('RGB')  # JPEG uses RGB format
                    img.save(jpg_path, 'JPEG', quality=95)
                    # Compress if over 1MB
                    compress_image_if_needed(jpg_path, max_size_mb=1)
                    return jpg_path
                else:
                    # Save as PNG format for PNG and other lossless formats
                    img = img.convert('RGBA')  # PNG uses RGBA format
                    img.save(png_path, 'PNG', optimize=True, pnginfo=None)
                    # Compress if over 1MB
                    compress_image_if_needed(png_path, max_size_mb=1)
                    return png_path
                    
            except Exception as e:
                error_msg = str(e)
                if "HEIF" in error_msg and not HEIF_SUPPORT:
                    print(f"[WARN] HEIF image {file_id} detected but pillow-heif not installed. Install with: pip install pillow-heif")
                elif "HEIF" in error_msg:
                    print(f"[WARN] Could not process HEIF image {file_id}: {e}")
                else:
                    print(f"[WARN] Could not download or convert image {file_id}: {e}")
                
                # Record failed image ID
                save_failed_image(file_id)
                return None
                
    except (IOError, OSError):
        # If lock cannot be acquired (another process is processing)
        # Wait a bit and check existence again
        import time
        time.sleep(0.1)
        if os.path.exists(jpg_path):
            return jpg_path
        if os.path.exists(png_path):
            # If force_jpeg is True and PNG exists, convert it to JPEG
            if force_jpeg:
                try:
                    print(f"[INFO] Converting PNG to JPEG for {file_id}...")
                    img = Image.open(png_path)
                    img = img.convert('RGB')
                    img.save(jpg_path, 'JPEG', quality=95)
                    compress_image_if_needed(jpg_path, max_size_mb=1)
                    # Remove original PNG file after successful conversion
                    os.remove(png_path)
                    print(f"[INFO] Removed original PNG file for {file_id}")
                    return jpg_path
                except Exception as e:
                    print(f"[WARN] Could not convert PNG to JPEG for {file_id}: {e}")
            return png_path
        return None
    finally:
        # Remove lock file
        try:
            os.remove(lock_file)
        except:
            pass

def format_drive_images(text, field_name=None):
    # Find Google Drive image URLs, download, convert, and return local Markdown image links
    
    # Define fields that should be converted to JPEG
    jpeg_fields = [
        "Team Photo",
        "Robot1 Overall", "Robot1 Front", "Robot1 Back", "Robot1 Top", "Robot1 Bottom", "Robot1 Right", "Robot1 Left",
        "Robot2 Overall", "Robot2 Front", "Robot2 Back", "Robot2 Top", "Robot2 Bottom", "Robot2 Right", "Robot2 Left",
        "Mechanical Photos", "Circuit Photos"
    ]
    
    # Check if this field should be forced to JPEG
    force_jpeg = field_name in jpeg_fields if field_name else False

    
    urls = re.split(r'[\s,]+', text)
    images = []
    for url in urls:
        url = url.strip()
        # open?id=... pattern
        m = re.match(r'https?://drive\.google\.com/open\?id=([\w-]+)', url)
        if m:
            file_id = m.group(1)
            local_path = download_and_convert_drive_image(file_id, force_jpeg=force_jpeg)
            if local_path:
                rel_path = os.path.relpath(local_path, OUTPUT_DIR)
                images.append(f'![]({rel_path})')
            else:
                # Use original link if conversion fails
                images.append(f'[{url}]({url})')
            continue
        # file/d/.../view pattern
        m = re.match(r'https?://drive\.google\.com/file/d/([\w-]+)/view.*', url)
        if m:
            file_id = m.group(1)
            local_path = download_and_convert_drive_image(file_id, force_jpeg=force_jpeg)
            if local_path:
                rel_path = os.path.relpath(local_path, OUTPUT_DIR)
                images.append(f'![]({rel_path})')
            else:
                # Use original link if conversion fails
                images.append(f'[{url}]({url})')
            continue
    if images:
        return '\n'.join(images)
    return text.strip()

def process_row(args):
    row, row_index, headers, summary_headers = args
    if not row or len(row) < 2:
        return None # skip empty or malformed rows
    team_name = row[1].strip() or f"team_{row_index}"
    filename = sanitize_filename(team_name) + '.md'
    filepath = os.path.join(OUTPUT_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as md:
        for i, (header, value) in enumerate(zip(headers, row)):
            summary = summary_headers[i] if i < len(summary_headers) else header.strip()
            content = format_drive_images(value, summary) # Pass header to format_drive_images
            # Add the original question in italics under the heading
            md.write(f"## {summary}\n\n*{header.strip()}*\n\n{content}\n\n")
    return filepath

def format_time(seconds):
    """Convert seconds to readable format"""
    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        minutes = int(seconds // 60)
        remaining_seconds = seconds % 60
        return f"{minutes} minutes {remaining_seconds:.1f} seconds"
    else:
        hours = int(seconds // 3600)
        remaining_minutes = int((seconds % 3600) // 60)
        remaining_seconds = seconds % 60
        return f"{hours} hours {remaining_minutes} minutes {remaining_seconds:.1f} seconds"

def main():
    start_time = time.time()
    print(f"Starting CSV processing at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    with open('tdp.csv', newline='', encoding='utf-8') as tdpcsv:
        reader = csv.reader(tdpcsv)
        headers = next(reader)
        
        # Prepare data for parallel processing
        rows_with_index = [(row, i+2, headers, SUMMARY_HEADERS) for i, row in enumerate(reader)]
        
        # Create Pool for parallel processing
        num_processes = min(cpu_count(), len(rows_with_index))
        print(f"Processing {len(rows_with_index)} rows using {num_processes} processes...")
        
        with Pool(num_processes) as pool:
            # Process each row in parallel
            results = pool.map(process_row, rows_with_index)

        # Filter parallel processing results and show only successful files
        successful_files = [f for f in results if f is not None]
        print(f"\nSuccessfully processed {len(successful_files)} files.")
        if successful_files:
            print("Processed files:")
            for f in successful_files:
                print(f"  - {f}")
    
    end_time = time.time()
    total_time = end_time - start_time
    print(f"\nProcessing completed at {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Total processing time: {format_time(total_time)}")
    print(f"Average time per row: {format_time(total_time / len(rows_with_index))}")

if __name__ == '__main__':
    main()