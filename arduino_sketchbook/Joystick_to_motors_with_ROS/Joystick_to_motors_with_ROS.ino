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
  //Encoder as input
   pinMode(OUTPUT_A1,INPUT);
   pinMode(OUTPUT_B1,INPUT);
   pinMode(OUTPUT_A2,INPUT);
   pinMode(OUTPUT_B2,INPUT);
   
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
   nh.advertise(encoderPb);
} 



 void loop() { 
  aState1 = digitalRead(OUTPUT_A1); // Reads the "current" state of the outputA
  aState2 = digitalRead(OUTPUT_A2); // Reads the "current" state of the outputA
  //MOTOR 1 
  // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState1 != aLastState1){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(OUTPUT_B1) != aState1) { 
       counter1 ++;
       //if 1000 milliseconds have passed
       if(tstart - tend >= 20){
         //calculate angular velocity
         pulses = counter1;
         Mspeed = (2*3.14*pulses)/(663*(tstart-tend));
       }
       //pass current time to en time 
       tend = tstart;  
     } else {
      //start time lapse for velocity calculation
      //tstart = millis();
      counter1 --;
      
      //if 1000 milliseconds have passed
      if(tstart - tend >= 1000) {
        //calculate angular velocity
        pulses = counter1;
        Mspeed = (2*3.14*pulses)/(663*(tstart-tend));
       }
      //pass current time to en time 
      tend = tstart;
     }
  
   //MOTOR2
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState2 != aLastState2){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(OUTPUT_B2) != aState2) { 
       counter2 ++;
       //if 1000 milliseconds have passed
       if(tstart - tend >= 20){
         //calculate angular velocity
         pulses = counter2;
         Mspeed = (2*3.14*pulses)/(663*(tstart-tend));
       }
       //pass current time to en time 
       tend = tstart;
      } else {
        //start time lapse for velocity calculation
        //tstart = millis();
        counter2 --;
      
        //if 1000 milliseconds have passed
        if(tstart - tend >= 1000){
          
        //calculate angular velocity
        pulses = counter1;
        Mspeed = (2*3.14*pulses)/(663*(tstart-tend));
        }  
        //pass current time to en time 
        tend = tstart;
      }
    }
   } 
   aLastState1 = aState1; // Updates the previous state of the outputA with the current state
   aLastState2 = aState2; // Updates the previous state of the outputA with the current state

   //Get data to motor_encoder message and publish
   encoders.leftMotor = counter2;
   encoders.rightMotor = counter1;
   encoderPb.publish(&encoders);
   
   nh.spinOnce();
   delay(1);
 }
