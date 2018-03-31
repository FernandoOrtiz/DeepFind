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
#include <deepfind_package/encoders_data.h>

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
volatile unsigned int counter1 = 0; 

volatile unsigned int counter2 = 0;  




//ROS variables and methods
ros::NodeHandle nh;

//callback function
void setMotorSpeed(int speed, int motorPin){
  analogWrite(motorPin, 255/100*speed);
}

void setMotorDirection(int direction, int motorPin){
  digitalWrite(motorPin, direction); 
}

void motorSpeedCallback(const deepfind_package::motor_command& message){
  setMotorDirection(message.leftMotorDirection, LEFT_DIRECTION_PIN);
  setMotorDirection(message.rightMotorDirection, RIGHT_DIRECTION_PIN);
  setMotorSpeed(message.leftMotorPower, LEFT_PWM_PIN);
  setMotorSpeed(message.rightMotorPower, RIGHT_PWM_PIN);
}

deepfind_package::encoders_data encoders;
ros::Publisher encoderPb("encoder", &encoders);
ros::Subscriber<deepfind_package::motor_command> sub("motor_speed", motorSpeedCallback);


void setup() { 
  //Encoder as interupt
  pinMode(OUTPUT_A1, INPUT);
  digitalWrite(OUTPUT_A1, HIGH);       // turn on pull-up resistor
  pinMode(OUTPUT_B1, INPUT);
  digitalWrite(OUTPUT_B1, HIGH);       // turn on pull-up resistor
  
  pinMode(OUTPUT_A2, INPUT);
  digitalWrite(OUTPUT_A2, HIGH);       // turn on pull-up resistor
  pinMode(OUTPUT_B2, INPUT);
  digitalWrite(OUTPUT_B2, HIGH);       // turn on pull-up resistor
  
  attachInterrupt(0, doEncoder, CHANGE);  // encoder pin on interrupt 0 - pin 2

   
   //motor as output
   pinMode(LEFT_PWM_PIN, OUTPUT);
   pinMode(RIGHT_PWM_PIN, OUTPUT);
   pinMode(LEFT_DIRECTION_PIN, OUTPUT);
   pinMode(RIGHT_DIRECTION_PIN, OUTPUT);

  
   //ROS  initialization
   nh.initNode();
   nh.subscribe(sub);
   nh.advertise(encoderPb);
} 

void doEncoder() {
  /* If pinA and pinB are both high or both low, it is spinning
     forward. If they're different, it's going backward.

     For more information on speeding up this process, see
     [Reference/PortManipulation], specifically the PIND register.
  */
  if (digitalRead(OUTPUT_A1) == digitalRead(OUTPUT_B1)) {
    counter1++;
  } else {
    counter1--;
  }

 if (digitalRead(OUTPUT_A2) == digitalRead(OUTPUT_B2)) {
    counter2++;
  } else {
    counter2--;
  }
 
}


 void loop() { 

   //Get data to motor_encoder message and publish
   encoders.leftMotor = counter2;
   encoders.rightMotor = counter1;
   encoderPb.publish(&encoders);
   
   nh.spinOnce();
   delay(1);
 }
