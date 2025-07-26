## Timestamp

*Timestamp*

7/12/2025 13:09:27

## Team Name

*What is your team's name?*

ETC autoPrikratki

## League

*What league do you participate in?*

Lightweight League

## Country

*Where are you from?*

Croatia

## Contact

*If other teams have questions about your robot, now or in the future, what email address(es) can we publish along with this document for people to reach you?

(You can put in multiple email addresses, like multiple team members, an email for the whole team or both. Feel free to share other ways of communication like Discord handles)*

etcautoprikratkicroteam@gmail.com

## Social Media

*Team Social Media Links (if you have any)*

https://www.instagram.com/etc_autoprikratki/

## Team Photo

*Upload a photo of your whole team with your mentor and robots

Note: This is not mandatory and will be published along with your TDP if you choose to upload something*

![](images/1uLtJWgc0mTHB4kr8Jzqho7qqEg6Rq394.jpg)

## Members & Roles

*What are the names of the team members and their role(s)?*

Our four-member team includes Juraj (captain, coding), Franko (mechanical design, assembly), Vinka (electronics, PCB, coding), and Duje (documentation, soldering, assembly).

## Meeting Frequency

*How often did your team meet?
(e.g. 90 minutes once per week or a day every weekend.)*

We worked every Saturday all day and Mondays for 90 minutes, with extra sessions as needed — continuing until the robot worked as intended.

## Meeting Place

*Where did you meet to work on your robot?
(e.g. a robotics room at school, at some other place, one of your homes, school library etc.)*

We worked at school, at our mentor’s home, and at our own homes.

## Start Date

*When did your team start working on this year's robot?*

In september.

## Past Competitions

*Which RoboCupJunior competitions have you competed in and in which leagues?*

Slovakian Open 2024. - Lightweight League
Croatian Open 2024. - Lightweight League
European Championship 2024. - Lightweight League
World Championship 2024. - Lightweight League
Slovakian Open 2025. - Lightweight League
Croatian Open 2025. - Lightweight League
European Championship 2025. - Lightweight League

## Mentor Contribution

*Which parts of your work received the most contribution from your mentor?*

Our mentor secured sponsorships and purchased the components we needed for our robots. He was mainly focused in organising us to work as a Team.

## Workload Management

*How did you manage the workload?*

We primarily communicate through a WhatsApp group, which we use for everything. We also use Google Drive for sharing files and GitHub for collaborating on code.

## AI Tools

*Which AI tools did you use?*

We mainly use ChatGPT for code debugging and idea generation, as well as for grammar checks in our documentation.

## Robot1 Overall

*Robot 1 Overall View*

![](images/1b2W_1bG4L_2dQWdNt0lkFGNpB_dAocsn.jpg)

## Robot1 Front

*Robot 1 Front view*

![](images/1i_CunLMN7zdEzn3v9gT-yR_HqFbRDqXB.jpg)

## Robot1 Back

*Robot 1 Back view*

![](images/134krtEXye9Umba_je_mKTOHj7vxLur9o.jpg)

## Robot1 Top

*Robot 1 Top View*

![](images/1elJitUHSOHpa-mp1xZfP5F9lnnLatRyY.jpg)

## Robot1 Bottom

*Robot 1 Bottom View*

![](images/1uaWbinevUFeLUtRflY9HFGL9r6O3GXHs.jpg)

## Robot1 Right

*Robot 1 Right View*

![](images/1_SjKxzZ49xvWv12CNJKACWdxynEleD-u.jpg)

## Robot1 Left

*Robot 1 Left View*

![](images/1_9A2Ik07vcck6ujBi-bpBJhGSGgN-7u7.jpg)

## Positioning & Movement

*How do you find your position inside the field and how do you use that position to move your robots around?*

We use a SparkFun odometry sensor and typically start the robot near the center of the field. As the robot moves while tracking the ball, it continuously updates its position using odometry. Additionally, we developed our own custom line sensor system — whenever any of the sensors detect the field line, the robot is programmed to return toward the origin point at position (0, 0).

## Robot2 Overall

*Robot 2 Overall View*

![](images/1gK18ahFkcm3yWzX1KRVsbR_JKjNpOeLN.jpg)

## Robot2 Front

*Robot 2 Front view*

![](images/19eG1nZgnKe3zTKZ8aP7JMIC3UdqD76Av.jpg)

## Robot2 Back

*Robot 2 Back view*

![](images/1eDuZi6KudBQKSa-nu8XFtNMLl4W-gGwq.jpg)

## Robot2 Top

*Robot 2 Top View*

![](images/18P5VTY4DpInmnB7kBYidliRj1vNPpKxk.jpg)

## Robot2 Bottom

*Robot 2 Bottom View*

![](images/1rEAOSQBoHAdzJ--nfy61YQ_ly23-IjEl.jpg)

## Robot2 Right

*Robot 2 Right View*

![](images/1vyvokH0DwVt-KiXUdCQB15iud0J03K6Q.jpg)

## Robot2 Left

*Robot 2 Left View*

![](images/1J4oWgnrF2ARVw5p-_o5MPG5PpXZPI575.jpg)

## Mechanical Design

*How did you design the mechanical parts of your robots?*

This year, we used an octagonal chassis to stand out from typical circular designs. Components like motors, drivers, and the kicker were placed on the bottom plate for a compact layout. PLA side walls reduced weight and allowed camera mounting. We placed the battery in the center for balance and added the kicker board at the front for easier assembly.

## Build Method

*How did you build your design?*

Most of the robot's parts were 3D printed at our school, while screws and nuts were bought locally. PCBs were ordered from JLCPCB, and custom polyurethane wheel treads were made by Gumiimpex. The biggest redesigns this year were the improved dual-layer wheels and updated plastic parts. We also separated the power supply from the main board, created a dedicated kicker PCB, and added a camera for better aiming.

## Motors & Reason

*How many motors have you used and why?*

We used four Joinmax JMP-BE 3561 motors and designed custom wheels to match, as off-the-shelf options didn’t meet our performance needs. After testing several prototypes, we found that roller spacing affected drift — wider spacing gave better grip, while narrower spacing caused more sliding. Each wheel has five parts, including 14 polyurethane rollers on 3D-printed rims, spinning on custom metal axles. A rear section reduces weight, and both halves are aligned with a 3D-printed spacer to prevent interference between rollers.

## Kicker Design

*If your robot has a kicker, explain how you designed and built the mechanics of the kicker*

Last year, we used a SparkFun kicker board with a single transistor, but it burned out after two days at the world championship and damaged our robot. This year, we kept the same solenoid but designed a more robust custom PCB with a stronger MOSFET. To trigger it reliably, we added a level shifter to convert the signal from the Teensy to the required 5V logic level.

## Dribbler Design

*If your robot has a dribbler, explain how you designed and built the mechanics of the dribbler.*

We developed a dribbler and reduced the robot’s weight using a PLA Aero chassis, which held up well during the European championship. However, due to the fast-paced nature of the Soccer Lightweight league and frequent collisions, we found the dribbler impractical. After testing 1-on-1 matches, we concluded the robot performs better without it.

## CAD Files

*CAD design files*

https://github.com/ETCautoPrikratkiCROTeam/ETC_autoPrikratki

## Mechanical Innovation

*Mechanical Innovation*

Our dual-layer wheels with polyurethane rollers were this year’s most valuable upgrade, greatly improving movement smoothness and responsiveness. We also developed a new 48-sensor line sensor in a Y-formation, which boosted line detection performance by about 90% over last year’s design. Additionally, our fully enclosed and reinforced chassis proved highly durable, withstanding over three competitions and more than 60 high-speed matches.

## Mechanical Photos

*Photos of your mechanical designs highlights*

![](images/1-P1ufBsm_Ix59G3Rem3XeNKWeOKcvr7q.jpg)
![](images/1rf3ku-0jKuT3PNHAvvmuB3ZR00N7-x3t.jpg)

## Electronics Block Diagram

*Provide us with a block diagram of your robot's electronics*

![](images/16rvNPo76h4mQHu7pSOxVSemMzQHtsJAw.png)

## Power Circuit

*How does your power circuits work?*

Our robot operates on 12V, 5V, and 3.3V and supports analog/digital, I2C, UART, and PWM communication. A 12V battery powers the motors, kicker, and power supply PCB, which steps down to 5V and 3.3V for other components. The Teensy 4.1 and ESP32 run on 5V, while the BNO055 IMU, ball sensor, and light barrier use 3.3V. The camera runs on 5V and communicates via UART; I2C connects the BNO055 and SparkFun OTOS. The line PCB, running on 3.3V, has 48 reflectance sensors with SMD LEDs and uses three analog multiplexers. To trigger the kicker, a 3.3V signal is boosted to 5V to activate a MOSFET, allowing 12V to power the solenoid. Four JoinMax JMP-BE-3561 motors are each controlled via PWM using MRMS ML-R motor drivers.

## Motor Drive Circuit

*How do you drive your motors? Explain the circuits you use for that*

To drive the motors, we use locally purchased ML-R 1x50A MRMS motor drivers, which are connected directly to the 12.5V battery. Each motor is wired to its own motor driver. From the driver, we use three control pins: a PWM pin to manage motor speed, a DIR pin to set the motor's rotation direction, and an SLP (sleep) pin that enables or disables the motor. The SLP pin is wired to a physical switch, allowing us to manually disable the motors for safety or debugging purposes, without needing to modify the code.

## Microcontroller & Reason

*What kind of micro controller or board do you use for your robot? Why did you decide to use this part for your robot? If you have more than 1 processor, explain each one separately.*

We use a Teensy 4.1 and an ESP32 XIAO C6. The Teensy was chosen for its strong processing power, many I/O pins, and proven reliability, making it ideal for our compact robot. The ESP32 XIAO C6 supports ESP-NOW, which we use for robot-to-robot communication, allowing us to coordinate strategies and improve team performance on the field.

## Ball Detection

*How does your ball detection sensors and/or camera[s] work?*

Our ball sensor connects to the Teensy 4.1 using two analog signals for distance and angle, plus a 3.3V power line. It provides continuous analog output for real-time ball tracking. For goal detection, we use an OpenMV H7 Plus camera connected via UART, using the find_blob() function to efficiently detect and track the colored goal marker.

## Line Detection

*How does your line detection circuits work?*

We designed a custom line sensor with 48 reflectance sensors arranged in a Y-shaped layout (12 per side), connected through three multiplexers to minimize analog pin usage. Each sensor has a red LED and a resistor. The multiplexers are controlled via 4 digital pins using binary combinations to cycle through all channels. Sensors read analog values based on surface reflectivity. Red LEDs were chosen for their strong contrast with the green field and white lines, improving detection accuracy.

## Navigation/Position Sensors

*What sensors do you use for navigation and how are these sensors connected to your processor? What sensors do you use to find your position in the field? What about the direction your robot faces?*

We use an odometry sensor to accurately track the robot's position, a BNO055 compass to determine its orientation, and a camera to detect the position of the goal.

## Kicker Circuit

*How do you drive your kicker system? How does the circuit make the kicker work?*

Last year, we used a SparkFun kicker board with a single transistor, but it burned out after two days at the world championship and damaged our robot. This year, we kept the same solenoid but built a stronger custom kicker PCB with a more durable MOSFET. To trigger it, we used a level shifter to convert the Teensy's 3.3V signal to the required 5V.

## Dribbler Circuit

*How does your dribbler system work? What components and circuits did you use to drive it?*

Our dribbler uses one ML-R motor driver and operates the same way as a regular motor — it simply rotates. Inside the system, we designed a 45:10 gear ratio to ensure optimal rotation speed. We also custom-ordered our own polyurethane rollers, manufactured based on our mold design. We dont use dribbler in games, but we developed one.

## Schematics

*Schematics of your robot*

![](images/1L-nRjtqDyCfDk9E_tU3TgUh1mbAKP-_d.png)

## PCB

*PCB of your robot*

![](images/1XMm-xQ63Wm50zK9gziVObqZDO4zcIvab.png)
![](images/1eMn-GgClX3pKNK6TELQbVWfK7ADUpYQB.png)
![](images/19b2BQgaxb2B_fWOdYv3gOy765Yiehr7l.png)
![](images/1TE2BqyCFGc-fcZ3sDCMo4d82FTg8FcLi.png)
![](images/1IK1ptSC3tXkJIjHMLNTiF1bpZgHFgg0f.png)

## Innovation

*Innovations*

We are especially proud of our custom Kicker PCB, as we finally succeeded in creating a board capable of withstanding the demands of competition. This was achieved by using a more durable MOSFET transistor and adding a Zener diode for reverse voltage protection.
We’re also proud of our Line Sensor PCB, which features 48 reflectance sensors connected through 3 multiplexers. We chose to arrange the sensors in a Y-pattern on each of the four sides of the robot. Additionally, we used SMD resistors instead of standard ones to reduce the overall weight of the PCB.

## Circuit Photos

*Photo of your circuit boards highlights*

![](images/1TtXwsD-7_vRS0cSSfgXMmNq9O0st_ZAm.jpg)
![](images/1ZKg8eTOYGqi2uO5PgP_vKyANDwhFI5aW.jpg)
![](images/1-x2SZr4bNPjSemJXI1YU_B-wXdBYIG6i.jpg)
![](images/110kJF5PoSP5bS7NFi7YXgOMjJg1Y4_wE.jpg)

## Motor Control

*How do you use your processor to move your motors?*

Each of our four motor drivers uses three signal pins: PWM for speed, DIR for direction, and SLP (sleep), which disables the motor when not held at 3.3V. The SLP pin is connected to 3.3V and a push-button, allowing us to manually disable motors during debugging.
We created a go(...) function that calculates each motor’s speed and rotation based on movement speed (0–100%), movement angle (0°–360°), rotation (for compass correction), and a speed limit. The angle is converted into sine and cosine values to determine motor contributions. Motor speeds combine linear and rotational components and are normalized to stay within the defined limit.

## Ball Detection Method

*How do you find where the ball is? How do you read the data from the ball detection sensors or camera?*

The ball sensor outputs analog values ranging from 0 to 1023, which we map to angles from 0° to 360°. To read this data, we simply connect the sensor's two analog output lines to the Teensy 4.1 board.

## Ball Catch Algorithm

*How does your algorithm work to catch the ball? Is there a difference between your robots in how they move towards the ball? Explain the differences.*

To approach the ball, our robot reads the angle of the ball and adds an offset of +90° to orbit around it, allowing the robot to face the ball while circling it. However, if the ball is far away, we also read the distance value from the sensor. Based on that distance, the +90° offset is dynamically reduced, so the robot moves more directly toward the ball when it’s farther away and starts orbiting only when it's closer.

## Line Algorithm

*How does your robot find the lines to stay inside the field? What algorithms do you use to avoid going out of bounds?*

We developed an algorithm using our odometry sensor that keeps the robot from going out of bounds. Whenever any of the line sensors detect the field line, the robot calculates the angle back toward the center of the field using the formula: Angle equals arctangent of (x_target minus x_current, y_target minus y_current), multiplied by pi divided by 180. This computed angle is then used to guide the robot smoothly back toward the center, ensuring it stays within the playing area during the match.

## Goal Algorithm

*What algorithms do you use to score goals? How do you use your kicker and dribbler to handle the ball?*

Our robot keeps a constant heading toward the opponent’s goal. It uses the ball sensor to orbit the ball and approach it from the front. If the ball enters the light barrier, the robot uses the camera to align with the goal and kicks. If the ball is near but outside the barrier, it overshoots slightly to strike it toward the goal with a side wheel.

## Defense Algorithm

*What algorithms do you use to avoid the opponent team scoring? How do your robots defend your own goal?*

For defense, our robot stays positioned on the line between the front and back line sensors, moving left or right to follow the ball while always facing the center of our goal. If the ball is directly in front, it moves forward and kicks it away from the danger zone. If the robot doesn’t receive an ESP32 (ESP-NOW) signal that its teammate is still active, it switches to the attacking phase and starts approaching the ball with the goal of scoring.

## Robot Communication

*Do your robots communicate with each other? How do you use this communication to your advantage?*

Yes, our robots communicate using the ESP32 XIAO C6 via the ESP-NOW protocol. For example, if the striker goes out of bounds, the defender switches to attack to keep the game flowing. We tested dynamic role-switching, but it didn’t work well since one robot's camera faces forward and the other backward, making goal detection unreliable. In the future, we plan to add a second or 360-degree camera to enable seamless role switching.

## Innovation2

*Innovations*

As an innovation, we use an odometry sensor to track the robot’s position and developed an algorithm that pulls the robot toward the center when a line is detected, reducing out-of-bounds errors and enabling higher speeds.
We also introduced an overshooting strategy, tested at the European competition, to reach the ball faster. For the World Championship, we prepared two strategies: one with overshooting for quick interceptions, and another where the robot approaches the ball directly and aligns with the goal before shooting.

## GitHub Link

*GitHub link*

https://github.com/ETCautoPrikratkiCROTeam/ETC_autoPrikratki

## BOM

*Bill of Materials (BOM)*

[https://drive.google.com/open?id=1I1jxhI1-awF15fbubzEFaam6GkeufbMqJ3UiT_4J3us](https://drive.google.com/open?id=1I1jxhI1-awF15fbubzEFaam6GkeufbMqJ3UiT_4J3us)

## Cost

*How much did it cost you to build your robots?*

Robots (both): 1557.54 Euro 
Experiments (without robots): around 300 Euro mostly burned teensy and motor drivers.
Everything was provided by the school, robots, experiments and environment. We don't know how much school paid for the environment.

## Funding

*How did you gathered the funds to build the robots?*

Material and robots are 100% from school.
Sponsors funded our travel.

## Affordability

*How affordable was it to compete in RoboCupJunior Soccer?*

5

## Answer Check

*Have you checked all of your answers?*

Yes!

## Publication Consent

*We publish TDPs and posters during or after the competition as described in the beginning*

Yes, we acknowledge everything submitted in the above form can be published.

## Email Address

*Email Address*

jura.kolaric0@gmail.com

## TDP File

*TDP File Upload (Not required)*



## Extra Column

*Column 67*



