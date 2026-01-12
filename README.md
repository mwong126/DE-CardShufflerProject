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

## **CAD Models:**

**Base Chassis:**

<img width="954" height="643" alt="Screenshot 2025-12-19 150648" src="https://github.com/user-attachments/assets/5dd45919-99a6-4df6-a717-afc565120c9e" />


**Wheel Mount:**

<img width="597" height="443" alt="Screenshot 2025-11-24 232253" src="https://github.com/user-attachments/assets/0b2835a8-b916-4356-9ab7-ce8dfed62a2e" />

These two pieces were made using Fusion and act as my main base and the mounts for my wheels that turn the cards. The Base chassis has an upper compartment that holds the cards that are to be shuffled and two slits on either side of that are just tall enough for 1 card to slide through. One one side the cards go immediately to the bottom but on the other side the cards are held in a small area before being sent down to the bottom. This simulates the act of splitting the deck. Furthermore the wheel mounts are made using a combination of the online CAD model of the motors to find the right fit fore the hole and the CAD model of a lego axle to ensure that the lego wheels will stay on.

## **Manufacturing:**

The majority of the parts for this project were 3-d printed due to the ease and speed. It was very simple to simply downnload the file from Fusion as a STL and send it to the printer. Some of the parts took multiple tries to work as they failed or needed to be changed after the fact due to the part not working quite how it was intedended to. The main base was printed first and then the mounts for the wheels. The wheels themselves were Lego which made it very easy to find the exact dimensinos online as well as find existing CAD models of the parts. 

## **Wiring:** 

For the wiring, dupont connecters were used to easily connect the RaspberryPi to the motor drivers and the power supply to the motors.

## **User Guide:**

## **Code:**

## **Technical Challenges:**

## **Final Notes:**
