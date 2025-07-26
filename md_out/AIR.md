## Timestamp

*Timestamp*

7/12/2025 18:37:15

## Team Name

*What is your team's name?*

AIR

## League

*What league do you participate in?*

Lightweight League

## Country

*Where are you from?*

Ritsumeikan Moriyama High School, Moriyama, Shiga, Japan

## Contact

*If other teams have questions about your robot, now or in the future, what email address(es) can we publish along with this document for people to reach you?

(You can put in multiple email addresses, like multiple team members, an email for the whole team or both. Feel free to share other ways of communication like Discord handles)*

Tanuki.1116.au@gmail.com

## Social Media

*Team Social Media Links (if you have any)*

https://x.com/air_3838?s=21&t=FOVZXhIMGPvi0YPvd8sd3Q

## Team Photo

*Upload a photo of your whole team with your mentor and robots

Note: This is not mandatory and will be published along with your TDP if you choose to upload something*

![](images/1axyjSr9OPtu9hwuw9JAkyAfoHj5TU0PI.jpg)

## Members & Roles

*What are the names of the team members and their role(s)?*

Asahi Uchida: Captain, Circuit, PCB design and Programming 
Kosuke Kano: Programming 
Kengo Nakazawa: Hardware design
Sora Matsui: Hardware design assistant

## Meeting Frequency

*How often did your team meet?
(e.g. 90 minutes once per week or a day every weekend.)*

Five times a week for two hours

## Meeting Place

*Where did you meet to work on your robot?
(e.g. a robotics room at school, at some other place, one of your homes, school library etc.)*

Robotics club at our school Ritsumeikan Moriyama High School.

## Start Date

*When did your team start working on this year's robot?*

4 years

## Past Competitions

*Which RoboCupJunior competitions have you competed in and in which leagues?*

Japan Open 2021: Soccer Entry league
Japan Open 2022~2025: Soccer Lightweight league

## Mentor Contribution

*Which parts of your work received the most contribution from your mentor?*

I asked my mentor to purchase tape, soldering iron, tools, etc., which we use in our daily development. Our mentor can’t do anything on our development, just only advice.

## Workload Management

*How did you manage the workload?*

We used LINE as a communication tool and Github to manage the team. We also used Notion to manage schedules, goals, and development notes. Since we basically met and developed the team every day, there was no need to use such tools too much.

## AI Tools

*Which AI tools did you use?*

Translated the poster's and this TDP Japanese into English using chat GPT.

## Robot1 Overall

*Robot 1 Overall View*

![](images/1HNpPhVI-17ZfU5CUp4WSNI5RumQ7ISUM.jpg)

## Robot1 Front

*Robot 1 Front view*

![](images/1Ct-6Y6rMJuaUlD-kdhA_dkudC4BWahQI.jpg)

## Robot1 Back

*Robot 1 Back view*

![](images/17_4Pe5ekIoUJvSrI3frFcidv34emMkMz.jpg)

## Robot1 Top

*Robot 1 Top View*

![](images/19J6R2vveJqmtXuBeJP72X69Bb0JwQKWC.jpg)

## Robot1 Bottom

*Robot 1 Bottom View*

![](images/1oYugrz4hJJ3uZa_TPoVRf_NcqiHicL_7.jpg)

## Robot1 Right

*Robot 1 Right View*

![](images/1cE29WCPZ6ByIQCFvCMYnJ739OhdLwNO4.jpg)

## Robot1 Left

*Robot 1 Left View*

![](images/1pvafH--bEsWvfO30yfuq-9qIMqx1UK66.jpg)

## Positioning & Movement

*How do you find your position inside the field and how do you use that position to move your robots around?*

We have not implemented any special method for precisely determining the robot’s position on the field. In the context of RCJ LWL, we believe that such information can actually become excessive, leading to unnecessarily complex processing and increasing the risk of errors. Therefore, we feel that simply estimating the approximate position using the angle of the goal detected by the camera provides a sufficient and well-balanced solution.

## Robot2 Overall

*Robot 2 Overall View*

![](images/17ODHHFOwMiGFitE6rSRioIPFa71oXl3y.jpg)

## Robot2 Front

*Robot 2 Front view*

![](images/16MrORgIYxYhhH3XdLX6VdhnIvXXlZUjA.jpg)

## Robot2 Back

*Robot 2 Back view*

![](images/14R3rDBOPB4MC3hzjmiEyhvNTnkqdx3UL.jpg)

## Robot2 Top

*Robot 2 Top View*

![](images/1OBNbUqX5BjuwXYgINCc22I4YSl5A3MMz.jpg)

## Robot2 Bottom

*Robot 2 Bottom View*

![](images/1C9skSL46mrGP2LCW4qa1ExNfI-vt6bTY.jpg)

## Robot2 Right

*Robot 2 Right View*

![](images/120EVOykOaucyVogbHcgS0ciXOwToiz6K.jpg)

## Robot2 Left

*Robot 2 Left View*

![](images/13H-7Xcy4UR4W39EvGYD7b1amGnzhFVhp.jpg)

## Mechanical Design

*How did you design the mechanical parts of your robots?*

The robot frame was designed in Fusion360 and 3D printed. Circuit boards were designed with KiCad and ordered from JLCPCB.
I programmed using VSCode. We added a camera to stabilize goal detection and introduced a kicker to shoot while avoiding opponents. To improve maintainability, the motor can be removed without full disassembly, and the line sensor can be detached from below.
Omni-wheel improvements included replacing a 3D-printed fixed part, which melted from motor heat, with a metal hub. We also increased the infill to 100% and used ABS filament. These changes made the tires durable even at high motor speeds.

## Build Method

*How did you build your design?*

All robot frames are 3D printed in our club using Bambu Lab, FlashForge, and Raise3D printers. Therefore, we rarely order from outside companies, except for special frames. Circuit board designs are ordered from our sponsor, JLCPCB. For urgent needs, we use universal circuit boards.
When attaching the kicker, the motors initially interfered due to their wide size. We fixed this by rotating the motors slightly, taking advantage of their flat surfaces to avoid interference.

## Motors & Reason

*How many motors have you used and why?*

Both Robot1 and Robot2 use four motors for higher torque. Four wheels provide better resistance to pushing forces than three wheels due to their combined movement vectors.
We made the omni wheels ourselves. For Robot1, each side wheel has its own shaft secured with washers on both ends for durability and smooth rotation. Urethane was used for its wear resistance and ease of laser cutting, suitable for many matches in the World Championship. For Robot2, side wheels are fixed together with a wire and washers, using silicone rubber as before.

## Kicker Design

*If your robot has a kicker, explain how you designed and built the mechanics of the kicker*

The kicker is fixed to the lower frame using a custom-made 3D-printed mount. To ensure that the kicking force is transmitted effectively, we fine-tuned the position of the kicker.

## Dribbler Design

*If your robot has a dribbler, explain how you designed and built the mechanics of the dribbler.*



## CAD Files

*CAD design files*

https://github.com/Gamu2124/RCJ2025-Brazil_CAD-design-files

## Mechanical Innovation

*Mechanical Innovation*

Our greatest pride is the improved maintainability. We redesigned the structure to minimize screws and nuts. Previously, motor mounts were separate and fixed with screws; now, they are integrated into the lower frame, reducing damage risk from loose screws. This design also allows easy motor removal without disassembling the whole robot, greatly improving maintenance.

## Mechanical Photos

*Photos of your mechanical designs highlights*

![](images/1WN5L4tTjP5EgvGlgEnocQzZ1-P-OZVnf.jpg)
![](images/137-e6qq1G0c56n0qdd5EoT-FHFLRdboF.jpg)
![](images/1J-pEFnmy6zC-_W9LCmyrnxv0GeMfRyv6.jpg)
![](images/1r-SAyPAAPhzp_enYoB-9h6a_8wzW_w4F.jpg)
![](images/1bJC-tc0OnnRdKqNee_UgarYkHAgsXova.jpg)

## Electronics Block Diagram

*Provide us with a block diagram of your robot's electronics*

![](images/183nf04zRkcFu0oq7SPrkViv7lD22Qh13.png)

## Power Circuit

*How does your power circuits work?*

We use an 11.1V LiPo battery. The power distribution board steps down this voltage to 5V and 3.3V using a DC-DC converter. The 3.3V output powers only the motor control board, while 5V is supplied to each microcontroller. Both the main and line sensor boards further step down 5V to 3.3V via linear regulators. The kicker voltage is boosted from 11.1V to about 40V.

## Motor Drive Circuit

*How do you drive your motors? Explain the circuits you use for that*

The motors used for robot1 are DRV8432, and for robot2 are DRV8774. The elements are operated by inputting the power supply voltage and high voltage 3.3V and 5V. The input PWM is sent from the main microcontroller.

## Microcontroller & Reason

*What kind of micro controller or board do you use for your robot? Why did you decide to use this part for your robot? If you have more than 1 processor, explain each one separately.*

Our main microcontroller is the Teensy 4.1, about 38 times faster than the ATmega2560 we used before. It solved previous speed limits and offers easy debugging and many UART pins. For sub-microcontrollers, we use the ATmega32U4 for 16 ball sensors—too many for the main controller—and the ATmega2560 for line sensors. The ATmega32U4 was chosen for its dedicated processing and strong support. Previously, line sensors were read as analog inputs via a multiplexer, causing slow response and out-of-bounds issues. Switching to digital outputs processed by the ATmega2560 greatly improved performance.

## Ball Detection

*How does your ball detection sensors and/or camera[s] work?*

We use TSSP4038 sensors as ball sensors, reading digital signals. By combining their vectors, we calculate the ball’s angle with 0.1° precision and estimate the distance using the Pythagorean theorem. The UnitV AI Camera is used only to detect the goal’s angle.

## Line Detection

*How does your line detection circuits work?*

We use 24 sets of phototransistors and LEDs as line sensors. In Robot1, analog signals are converted to digital using comparators and processed by a sub-microcontroller. In Robot2, analog signals are read directly by the main microcontroller via a multiplexer.

## Navigation/Position Sensors

*What sensors do you use for navigation and how are these sensors connected to your processor? What sensors do you use to find your position in the field? What about the direction your robot faces?*

We use the BNO055 sensor to detect the robot’s orientation. Data is read via I2C communication and processed by the main microcontroller. We do not have sensors such as ultrasonic sensors or LiDAR for position detection installed. Although currently under development, we plan to implement self-localization using cameras in the future.

## Kicker Circuit

*How do you drive your kicker system? How does the circuit make the kicker work?*

For the kicker, we boost 11.1V to 40V with a step-up converter. The microcontroller controls capacitor charging and discharging via digital pins that switch a P-channel MOSFET. To isolate the main microcontroller from the 40V line, we use an AQW212 optocoupler.

## Dribbler Circuit

*How does your dribbler system work? What components and circuits did you use to drive it?*

We don't have dribbler

## Schematics

*Schematics of your robot*

[https://drive.google.com/open?id=1av1kICUuhU7M-ZXPbWHk2MJdx_kmg8Ln](https://drive.google.com/open?id=1av1kICUuhU7M-ZXPbWHk2MJdx_kmg8Ln)
[https://drive.google.com/open?id=1o4XxhyBAypE8takjPAsQU0oVYgdPLhZ2](https://drive.google.com/open?id=1o4XxhyBAypE8takjPAsQU0oVYgdPLhZ2)
[https://drive.google.com/open?id=1w9VdBgtX6IXPVoxHFHD3oVNW-WuZu4GT](https://drive.google.com/open?id=1w9VdBgtX6IXPVoxHFHD3oVNW-WuZu4GT)
[https://drive.google.com/open?id=1CmcZXyQGcmMC4N3Qs1YPxXnbeSyHv7jP](https://drive.google.com/open?id=1CmcZXyQGcmMC4N3Qs1YPxXnbeSyHv7jP)
[https://drive.google.com/open?id=1VE45WGVCTGTToT8ewZXVkcug076XxlOX](https://drive.google.com/open?id=1VE45WGVCTGTToT8ewZXVkcug076XxlOX)

## PCB

*PCB of your robot*

![](images/15B2zRDO_IdJ713X-WRxcYlyXk_0I1fc9.png)
![](images/1fZnlaSROHvuAL-ZutyAXNvBhLTd95Vkk.png)
![](images/1JWk3mQJ_zreDQaZLD7I-p69BrVbGaQFB.png)
![](images/1lmAdlyDv9Aq7cuiAOfeJ2RrXbDSFqucD.png)
![](images/1Plaj4T5wOfzrtlx-BZJdJLs5DZNidl-Q.png)

## Innovation

*Innovations*

This section covers the line sensor. Previously, analog signals were read via a multiplexer, causing slow processing. Adding a microcontroller and using comparators to convert analog to digital enabled fast, reliable line detection. To improve maintainability, we redesigned the robot so motors can be removed from below, requiring a large hole in the center of the line sensor board. Despite having the most wiring, we made it a two-layer PCB to keep wiring neat and maintenance easy. We are proud of these line sensor board improvements.

## Circuit Photos

*Photo of your circuit boards highlights*

![](images/1XZBcHs6v2CjiAoOOFE0FRsWA17PKPVfl.jpg)
![](images/1KbmR9fa6Ur7dKa7NNzQwevtwDExgUTf2.jpg)
![](images/1y73xIbV_nPlck5Ay60lhV1llU0DsMLfV.jpg)
![](images/1BqDXOxTgpM9tYb5DK52wfHVP3qF04D2y.jpg)
![](images/1HUlHHEgyIOaG9ulrerPQmF5tbB64RKTS.jpg)

## Motor Control

*How do you use your processor to move your motors?*

The motor is operated using the DRV8432 and DRV8774 motor drivers. This product has a built-in switching element, and can drive the motor by providing the appropriate PWM, power, and signals. The processing is done by Teensy4.1. The angle is calculated from the detected information, and the speed of each motor is determined accordingly. Specifically, this is expressed by the formula sin(radians(ang - mAngle[i])) * speed + DIR.

## Ball Detection Method

*How do you find where the ball is? How do you read the data from the ball detection sensors or camera?*

Ball sensor digital values are accumulated over fixed cycles. From the total, we estimate the ball’s approximate direction by finding the closest sensor angle. Using the sensor with the highest value and its seven neighbors, we perform vector synthesis to calculate the precise ball angle. Distance is then estimated using the Pythagorean theorem based on this vector.

## Ball Catch Algorithm

*How does your algorithm work to catch the ball? Is there a difference between your robots in how they move towards the ball? Explain the differences.*

Robot1 acts as the attacker, circling the ball and controlling movement by linearly scaling based on ball angle and applying distance-based corrections. Robot2 is the defender, usually guarding the goal with line tracing. From the neutral point, it moves toward the ball’s angle to try and knock it away.

## Line Algorithm

*How does your robot find the lines to stay inside the field? What algorithms do you use to avoid going out of bounds?*

We use line sensors to detect white lines. In Robot2, analog values are thresholded into digital 0 or 1, like Robot1. Active sensor positions generate vectors to detect line direction. When multiple sensors detect continuously, their vectors combine to find the line’s overall direction. If detections are scattered, synthesized vectors are further combined to calculate the final direction and line angle. If over half the robot crosses the white line, the dot product is used to decide moving opposite the detected vector to return. Even if fully inside the line area, the robot can recover using the last stored detection vector.

## Goal Algorithm

*What algorithms do you use to score goals? How do you use your kicker and dribbler to handle the ball?*

After circling the ball and confirming possession, the robot enters the shooting phase. It detects the goal’s angle and moves forward, adjusting orientation to face the target. Once aligned, it shoots using the kicker. To handle goalkeepers, we developed a camera-based enemy avoidance system. Unlike typical teams that detect only short defenders, we split the goal into two zones when a defender is present. This lets the robot recognize tall defenders and avoid them by identifying the opponent, greatly improving stability and shot success.

## Defense Algorithm

*What algorithms do you use to avoid the opponent team scoring? How do your robots defend your own goal?*

Robot2 plays defense by line tracing the white line in front of the goal and moving sideways to block the ball. It adjusts its speed based on the ball’s velocity to handle angled or fast shots and predicts the ball’s future position for better defense. To prevent leaving the goal area, Robot2 uses a rear-facing camera to automatically return to its original position, ensuring it stays in front of the goal.

## Robot Communication

*Do your robots communicate with each other? How do you use this communication to your advantage?*



## Innovation2

*Innovations*

We are especially proud of our camera-based enemy avoidance program. Previously, our shooting success rate was low, and we struggled to use the kicker and camera effectively. Since implementing this program, we consistently avoid defenders and make accurate shots. Notably, we successfully bypassed the goalkeeper of "Edge," the team that won last year’s World Tournament overall championship. Their defense was considered the strongest in RCJ LWL, so scoring against them was a major achievement we are very proud of.

## GitHub Link

*GitHub link*

https://github.com/Gamu2124

## BOM

*Bill of Materials (BOM)*

[https://drive.google.com/open?id=13_2jpun1usE1WLPjgzjHNNAH6_dpc-Sv](https://drive.google.com/open?id=13_2jpun1usE1WLPjgzjHNNAH6_dpc-Sv)

## Cost

*How much did it cost you to build your robots?*

Robots (cost of components that are in your robots right now):150000 yen each
Experiments (failed builds, broken hardware etc.): 100000 yen
Environment (fields, balls, etc.) : The total, including the items used in the club activities, is 1,500,000 yen, but for the team, it is 50,000 yen.
1 USD = 147.33 yen

## Funding

*How did you gathered the funds to build the robots?*

40% sponsors
10% school
50% parents

## Affordability

*How affordable was it to compete in RoboCupJunior Soccer?*

1

## Answer Check

*Have you checked all of your answers?*

Yes!

## Publication Consent

*We publish TDPs and posters during or after the competition as described in the beginning*

Yes, we acknowledge everything submitted in the above form can be published.

## Email Address

*Email Address*

tanuki.1116.au@gmail.com

## TDP File

*TDP File Upload (Not required)*



## Extra Column

*Column 67*



