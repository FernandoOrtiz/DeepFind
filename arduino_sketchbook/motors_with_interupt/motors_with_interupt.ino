/**
 * WIRING GUIDE:
 * 
 * M1(Right Motor Looking From the Front):
 *  Vcc Red- 5V Arduino
 *  GND Black Arduino
 *  Motor PWM - Digital Pin 4 - Motor Driver PWM1
 *  Encoder - Output A(blue wire) - Digital pin 2 Arduino
 *            Output B(orange wire) - Digital pin 3 Arduino
 *            M+ - M1A Motor Driver
 *            M- - M1B Motor Driver
 *  Orientation - Digital pin 5 Arduino
 *  
 *            
 * M2(Left Motor Looking From the Front):
 *  Vcc Red- 5V Arduino
 *  GND Black Arduino
 *  Motor PWM - Digital Pin 6 - Motor Driver PWM2
 *  Encoder - Output A(blue wire) - Digital pin 20 Arduino
 *            Output B(orange wire) - Digital pin 21 Arduino
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
#define OUTPUT_A1 2 
#define OUTPUT_B1 3
#define OUTPUT_A2 20
#define OUTPUT_B2 21

//motor pwm pin
#define LEFT_PWM_PIN 6
#define RIGHT_PWM_PIN 4

//motor direction pin
#define LEFT_DIRECTION_PIN 9
#define RIGHT_DIRECTION_PIN 5

//scale factor fix encoders
#define SCALE_FACTOR_LEFT 1.31
#define SCALE_FACTOR_RIGHT 0.8

#define WHEEL_DIAMETER 0.13335

//Variables for counting encoder pulses and calculating velocities
int counter1 = 0; 
int counter2 = 0;  
int lastCount1 = 0;
int lastCount2 = 0;
long time[2] = {0,0};
double ddis [2] = {0,0};
double velocity[2] = {0,0};
float scaleFactor[2] = {SCALE_FACTOR_LEFT, SCALE_FACTOR_RIGHT};


//ROS variables and methods
ros::NodeHandle_<ArduinoHardware, 2, 2, 80,105> nh;

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
ros::Publisher pub("encoder", &encoders);
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
  attachInterrupt(2, doEncoder2, CHANGE);  // encoder pin on interrupt 2 - pin 20

   
   //motor as output
   pinMode(LEFT_PWM_PIN, OUTPUT);
   pinMode(RIGHT_PWM_PIN, OUTPUT);
   pinMode(LEFT_DIRECTION_PIN, OUTPUT);
   pinMode(RIGHT_DIRECTION_PIN, OUTPUT);

  
   //ROS  initialization
   nh.initNode();
   nh.subscribe(sub);
   nh.advertise(pub);
   
} 


void doEncoder() {
 
  if (digitalRead(OUTPUT_A1) == digitalRead(OUTPUT_B1)) {
    counter1++;
  } else {
    counter1--;
  }

  lastCount1 = counter1 - lastCount1;
}

void doEncoder2() {
 
 if (digitalRead(OUTPUT_A2) == digitalRead(OUTPUT_B2)) {
    counter2++;
  } else {
    counter2--;
  }

  lastCount2 = counter2 - lastCount2;
}

double ticksToMeters(double ticks){
  return (ticks*3.14*WHEEL_DIAMETER)
}


void getVelocities(int motor){

  long t = millis();
  int dTime = t - time[motor];
  time[motor] = t;
  
  ddis[motor] = ticksToMeters(lastCount1*scaleFactor[motor]);
  
  double estimatedVel = (ddis[motor]/dTime)*1000;
  velocity[motor] = estimatedVel;
  
}


void getMotorsSpeeds(){
  for(int i=0; i<2; i++){
      getVelocities(i);
  }
}


void loop() {

  nh.spinOnce();

   //Get data to motor_encoder message and publish
   encoders.leftMotor = counter2*SCALE_FACTOR_LEFT;
   encoders.rightMotor = counter1*SCALE_FACTOR_RIGHT;
   encoders.speed[0] = velocity[0];
   encoders.speed[1] = velocity[1];
   pub.publish(&encoders);

   getMotorsSpeedseeds();
   
   delay(3);
 }
