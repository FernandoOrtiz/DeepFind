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
 

//encoder output variables
#define outputA1 3
#define outputB1 4
#define outputA2 7
#define outputB2 8
//motor pwm pin
int motorPin1 = 2;
int motorPin2 = 6;
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


void setup() { 
  //Encoder as input
   pinMode (outputA1,INPUT);
   pinMode (outputB1,INPUT);
   pinMode (outputA2,INPUT);
   pinMode (outputB2,INPUT);
   //motor as output
   pinMode(motorPin1, OUTPUT);
   pinMode(motorPin2, OUTPUT);
   
   Serial.begin (9600);
   // Reads the initial state of the outputA
   aLastState1 = digitalRead(outputA1); 
   aLastState2 = digitalRead(outputA2);  
 
   while (! Serial);
    Serial.println("Speed 0 to 255");
} 

 void loop() { 
  
  if (Serial.available())
  {
    int speed = Serial.parseInt();
    if (speed >= 0 && speed <= 255)
    {
      analogWrite(motorPin1, speed);
      analogWrite(motorPin2, speed);

      //start time lapse for velocity calculation
      tstart = millis();
    }
  }
   aState1 = digitalRead(outputA1); // Reads the "current" state of the outputA
   aState2 = digitalRead(outputA2); // Reads the "current" state of the outputA
  //MOTOR 1 
   // If the previous and the current state of the outputA are different, that means a Pulse has occured
   if (aState1 != aLastState1){     
     // If the outputB state is different to the outputA state, that means the encoder is rotating clockwise
     if (digitalRead(outputB1) != aState1) { 
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
       if(tstart - tend >= 1000){
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
     if (digitalRead(outputB2) != aState2) { 
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
     
     Serial.print("Position M1: ");
     Serial.println(counter1);
     Serial.print("Position M2: ");
     Serial.println(counter2);
     Serial.println("Angular Velocity: ");
     Serial.println(Mspeed);
   } 
   aLastState1 = aState1; // Updates the previous state of the outputA with the current state
   aLastState2 = aState2; // Updates the previous state of the outputA with the current state

 }
