# DE-CardShufflerProject
Card Shuffler Main objective: A deivice controlled by a RaspberryPi that powers multiple motors to split and stack a deck of cards in order to mimic the act of shuffling a deck of cards.

Digital Electronics Final Project, Marcus Wong


## **Introduction:**

The goal of this project was to implement and showcase some of the skills that we learned in the Digital Electronics class. The project uses code, wiring and PWM signals to control motors that are able to move the cards in specific ways. I decided to pursue this project because it was something that is a simple and interesting movement in day to day activities. Furthermore it is something that could be continued and updated to deal the cards out as well. 

## **Brainstorm Sketches:**
![IMG_1660](https://github.com/user-attachments/assets/cd2ef7db-1268-4b62-a8c8-46771c3a1e2e)

## **Part Selection:**

I selected various motors, motor drivers and a SBC to make my project work.
	
L298N Motor Driver - This motor driver is able to connect to two different motors and is able to power 12V motors which is why I chose it. Additionally is was cheap and very intutive to use. Furthermore, some of my friends had used this motor driver in the past, giving me an additional resource on how to use it without having to look up videos on it.
	
DC 12V 30RPM N20 Encoder Motor High Torque -  These motors were very small and lightweight making it easy to use multiple of them in my project, also there were multiple options for torque gearing when buying them. I chose the 100 rpm versions since I would not need an excessive amount of speed but rather a lot of torque, which is why these motors were a good option.

Raspberry Pi - I chose the Raspberry Pi as my SBC because it is easy to work with and I was already familiar with it.

Lego Parts 56903 and 61254 - These are the two lego pieces that make up a wheel. I needed to find small rubber wheels in order to get the required traction to move the cards. Since it was almost impossible to find wheels less than 2 inches wide online that were rubber and freestanding I decided to scavenge lego pieces at my house. These made a lot of sense since there were already CAD models of them and they were a very good size, had lots of traction, and easy to mount.

I also used a 12 v power supply to power my motors and multple jumper wires and dupont wires.

## **CAD Models:**

**Base Chassis:**

<img width="954" height="643" alt="Screenshot 2025-12-19 150648" src="https://github.com/user-attachments/assets/5dd45919-99a6-4df6-a717-afc565120c9e" />


**Wheel Mount:**

<img width="597" height="443" alt="Screenshot 2025-11-24 232253" src="https://github.com/user-attachments/assets/0b2835a8-b916-4356-9ab7-ce8dfed62a2e" />

These two pieces were made using Fusion and act as my main base and the mounts for my wheels that turn the cards. The Base chassis has an upper compartment that holds the cards that are to be shuffled and two slits on either side of that are just tall enough for 1 card to slide through. One one side the cards go immediately to the bottom but on the other side the cards are held in a small area before being sent down to the bottom. This simulates the act of splitting the deck. Furthermore the wheel mounts are made using a combination of the online CAD model of the motors to find the right fit fore the hole and the CAD model of a lego axle to ensure that the lego wheels will stay on.

## **Manufacturing:**
	
The majority of the parts for this project were 3-d printed due to the ease and speed. It was very simple to simply downnload the file from Fusion as a STL and send it to the printer. Some of the parts took multiple tries to work as they failed or needed to be changed after the fact due to the part not working quite how it was intedended to. The main base was printed first and then the mounts for the wheels. The wheels themselves were Lego which made it very easy to find the exact dimensinos online as well as find existing CAD models of the parts. 

## **Wiring:** 

For the wiring, dupont connecters were used to easily connect the RaspberryPi to the motor drivers and the power supply to the motors. I connected triplets of GPIO pins from the Raspberry Pi to the motor driver and used the 5V Rpi supply and an external 12 v power supply to provide the power to the motor driver and motors.

## **User Guide:**

## **Code:**

The code for the motors was rather simple due to finding a great video online explaining the code for this motor driver and I expanded on it further by importing wait commands through time.sleep(x) and figured out how I was going to alternate the motors to achieve the desired result of sending the cards to various sides.

	def forwardA(x):
		GPIO.output(ENA,x)
	    GPIO.output(IN1,GPIO.HIGH)
	    GPIO.output(IN2,GPIO.LOW)
		    
	def backwardA(x):
	    GPIO.output(ENA,x)
	    GPIO.output(IN1,GPIO.LOW)
	    GPIO.output(IN2,GPIO.HIGH)

These two segments demonstrate the functions that were detailed in the video to move a motor on port A forward and backwards. The ENA output represents a speed from 0-255 of the motor and when one of the IN1 or IN2 outputs is powered but the other is not then it spins in a direction and if the power is flipped to the other IN port then the direction of the motor is flipped. Furthermore I defined a stop function to ensure the ability to stop the motors when I wanted them to because otherwise the program would continuously run and thus the motors would stay on forever even if a for loop finished.

	def stop():
		GPIO.ouput(ENA,0)
		GPIO.output(ENB,0)

## **Challenges:**

There were multiple technical challenges that I faced when designing, creating, assembling and testing this project.

*Firstly, there were many problems with printing the base chassis as it was too big to be printed as one piece so it had to be printed in two. However this led to the problem of one half of the print failing multiple times and the supports for the print failing multiple times. The problem was solved by using a different printer however it caused a lot of delays.

*Second, the printing of the wheel mounts took some finetuning due to the fact that the printer had trouble printing such a small hole with accuracy and printing the axle without it warping on the tip. This problem was fixed with the addition of a skirt to the print and slowing down the print to around 60% speed and decreasing the flow rate. 

*Third, the breadboard that I had been using to test the wiring failed after the first trial so the motors turned on the first time however it took a few days to realize that the breadboard was the problem and not one of the wiring connections of the Pi, Motor Driver, Motor and dupont connectors. This created a large setback because each day I would have to set up and take a multimeter to the connections to slowly narrow down the problem to the breadboard connetion. This also prevented me from testing my code for a few days. This problem was sovled by removing the breadboard and directly wiring all of the connections.

*Fourth, managing time between doing TA work, the project and helping out with the USC biomechanics project meant that there were certain days where I was not able to work.

## **Final Notes:**

## **Sourcees**

https://www.pololu.com/category/60/micro-metal-gearmotors
https://brickarchitect.com/parts/56903
https://brickarchitect.com/parts/61254
https://grabcad.com/library/lego-technic-axles-1
https://www.youtube.com/watch?v=m8r8prXrcgw
https://www.amazon.com/Encoder-Motor-Arduino-7-5-3000RPM-Feedback/dp/B0DB25VYCR
https://www.amazon.com/WWZMDiB-L298N-H-Bridge-Controller-Raspberry/dp/B0CR6BX5QL?crid=3UL7MDZTO0S4I&dib=eyJ2IjoiMSJ9.hK2FjV8Ukp8CCyVTI1seMk4n3aguoO_lNXX3xoiH-O2g8aOhuJHXrK0PauW3wBb5EJQatv-gXIFVmemNsuPftrk-aGMHac9D3DyNfOiAC839s_74JMHDqxIBvas8RWOvukBGHwAFNvys6ts5brRIWLdxdqa6yigo7yON0DZhOr9qwm-06LsqX34FN8naCuFQj2Atl6BuVDxdvy_YWIFwwxcBZKvb-MmOQfRt-15_pfo.Z5oNvD2vslVNc79inv96RuEOGcfxY5ge-TpfO3NgQxI&dib_tag=se&keywords=L298N%2BMotor%2BDriver&qid=1763764828&sprefix=l298n%2Bmotor%2Bdriver%2Caps%2C196&sr=8-4&th=1
