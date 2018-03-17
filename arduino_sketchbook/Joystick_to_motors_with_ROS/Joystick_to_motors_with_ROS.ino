/**
 * WIRING GUIDE:
 * 
 * M1(Right Motor Looking From the Front):
 *  Vcc Red- 5V Arduino
 *  GND Black Arduino
 *  Motor PWM - Digital Pin 2 - Motor Driver PWM1
 *  Encoder - Output A(blue wire) - Digital pin 3 Arduino
 *            Output B(orange wire) - Digital pin 4 Arduino
 *            M+ - M1A Motor Driver
 *            M- - M1B Motor Driver
 *  Orientation - Digital pin 5 Arduino
 *  
 *            
 * M2(Left Motor Looking From the Front):
 *  Vcc Red- 5V Arduino
 *  GND Black Arduino
 *  Motor PWM - Digital Pin 6 - Motor Driver PWM2
 *  Encoder - Output A(blue wire) - Digital pin 7 Arduino
 *            Output B(orange wire) - Digital pin 8 Arduino
 *            M+ - M2B Motor Driver
 *            M- - M2A Motor Driver
 *  Orientation - Digital pin 9 Arduino
 *            
 * 
 */

#include <ros.h>
#include <deepfind_package/motor_command.h>

//encoder output variables
#define OUTPUT_A1 3 
#define OUTPUT_B1 4
#define OUTPUT_A2 7
#define OUTPUT_B2 8

//motor pwm pin
#define LEFT_PWM_PIN 6
#define RIGHT_PWM_PIN 2

//motor direction pin
#define LEFT_DIRECTION_PIN 9
#define RIGHT_DIRECTION_PIN 5

//Variables for counting encoder pulses
int counter1 = 0; 
int aState1;
int aLastState1;
int counter2 = 0;  
int aState2;
int aLastState2;


//variables for calculating angular velocity
unsigned long Mspeed = 0.0;
unsigned long tstart = 0;
unsigned long tend = 0;
int pulses = 0;


//ROS variables and methods
ros::NodeHandle nh;


//callback function
void setMotorSpeed(int speed, int motorPin){
  analogWrite(motorPin, 255/100*speed);
}
void setMotorDirection(int direction, int motorPin){
  digitalWrite(direction, motorPin); 
}
void motorSpeedCallback(const deepfind_package::motor_command& message){

  setMotorDirection(message.leftMotorDirection, LEFT_DIRECTION_PIN);
  setMotorDirection(message.rightMotorDirection, RIGHT_DIRECTION_PIN);
  setMotorSpeed(message.leftMotorPower, LEFT_PWM_PIN);
  setMotorSpeed(message.rightMotorPower, RIGHT_PWM_PIN);

}
ros::Subscriber<deepfind_package::motor_command> sub("motor_speed", motorSpeedCallback);


void setup() { 
  //Encoder as input
   pinMode (OUTPUT_A1,INPUT);
   pinMode (OUTPUT_B1,INPUT);
   pinMode (OUTPUT_A2,INPUT);
   pinMode (OUTPUT_B2,INPUT);
   //motor as output
   pinMode(LEFT_PWM_PIN, OUTPUT);
   pinMode(RIGHT_PWM_PIN, OUTPUT);
   pinMode(LEFT_DIRECTION_PIN, OUTPUT);
   pinMode(RIGHT_DIRECTION_PIN, OUTPUT);
   
   // Reads the initial state of the outputA
   aLastState1 = digitalRead(OUTPUT_A1); 
   aLastState2 = digitalRead(OUTPUT_A2);
 
   //ROS  initialization
   nh.initNode();
   nh.subscribe(sub);  
 
} 



 void loop() { 
  nh.spinOnce();
  delay(1);
 }
