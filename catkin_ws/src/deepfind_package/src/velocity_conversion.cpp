#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <deepfind_package/EncodersData.h>
#include <deepfind_package/Velocity.h>
#include <nav_msgs/Odometry.h>

ros::Time currentTime, lastTime;
ros::Publisher velPub;


//constants in meters
const double WHEEL_SEPARATION = 0.29845;
const double WHEEL_DIAMETER = 0.13335;

const double ODOM_TURN_MULTIPLIER = 1.0;

//double x = 0;
//double y = 0;
//double th = 0;
double timeDelta = 0;
double dl = 0, dr = 0;
double lastCount1 = 0;
double lastCount2 = 0;
double countDifference1 = 0;
double countDifference2 = 0;
double distanceTraveled1 = 0;
double distanceTraveled2 = 0;
double leftSpeed = 0;
double rightSpeed = 0;

double ticksToMeters(double ticks){
  return ((ticks/360)*(3.14159265359*WHEEL_DIAMETER));
}

void quadencCallback(const deepfind_package::EncodersData& msg){

  currentTime = ros::Time::now();
  timeDelta = currentTime.toSec() - lastTime.toSec();
  

  //velocity calculation
  countDifference1 = msg.leftMotor - lastCount1;
  countDifference2 = msg.rightMotor - lastCount2;

  distanceTraveled1 = ticksToMeters(countDifference1);
  distanceTraveled2 = ticksToMeters(countDifference2);

  leftSpeed = (distanceTraveled1/timeDelta);
  rightSpeed = (distanceTraveled2/timeDelta);

  lastTime = currentTime;
  lastCount1 = msg.leftMotor;
  lastCount2 = msg.rightMotor;
 

  // //pose and transform
  // geometry_msgs::Quaternion odomQuat;
  // nav_msgs::Odometry odom;
  // tf::TransformBroadcaster odomBroadcaster;
  // tf::Transform odomTransform;
  
  //dl = timeDelta * leftSpeed;
  //dr = timeDelta * rightSpeed;

  double dxy = (distanceTraveled2 + distanceTraveled2) / 2;
  double dth = (((distanceTraveled1 - distanceTraveled2) / WHEEL_SEPARATION)) * ODOM_TURN_MULTIPLIER;

  // x += dxy * cosf(th);
  // y += dxy * sinf(th);

  // th += dth;

  double v = dxy/timeDelta;
  double w = dth/timeDelta;

  // odomQuat = tf::createQuaternionMsgFromRollPitchYaw(0,0,th);
  // tf::Quaternion q;
  // q.setRPY(0,0,th);
  
  // double lm = msg.leftMotor; 
  printf("%f   %f    %f    %f\n",rightSpeed, distanceTraveled2, countDifference2, timeDelta); 
   
  // odomTransform.setOrigin(tf::Vector3(x,y,0.0));
  // //odomTransform.transform.translation.x = x;
  // //odomTransform.transform.translation.y = y;
  // //odomTransform.transform.translation.z = 0;
  // odomTransform.setRotation(q);

  // //position ****Tal vez se puede sacar del mapa
  // odom.pose.pose.position.x = x;
  // odom.pose.pose.position.y = y;
  // odom.pose.pose.position.z = 0.0;
  // odom.pose.pose.orientation = odomQuat;

  // //velocity
  // odom.twist.twist.linear.x = v;
  // odom.twist.twist.linear.y = 0.0;
  // odom.twist.twist.linear.z = 0.0;
  // odom.twist.twist.angular.x = 0.0;
  // odom.twist.twist.angular.y = 0.0;
  // odom.twist.twist.angular.z = w;



  //publish
  //odomBroadcaster.sendTransform(tf::StampedTransform(odomTransform, ros::Time::now(), "map", "odometry"));

  deepfind_package::Velocity vel;
  vel.header.stamp = ros::Time::now();
  vel.linearX = v;
  vel.angularZ = w;
  
  velPub.publish(vel);


}


int main(int argc, char **argv){

  ros::init(argc, argv, "velocity_publisher");
  ros::NodeHandle nh; 

  velPub = nh.advertise<deepfind_package::Velocity>("/vel", 50);

  ros::Subscriber encoderSub = nh.subscribe("/encoder", 1000, quadencCallback);

  lastTime.useSystemTime();
  currentTime.useSystemTime();
  lastTime = ros::Time::now();

  ros::spin();
  
  return 0;
}








/*
  tf::TransformBroadcaster odom_broadcaster;
  current_time = ros::Time::now();
  qe1 = msg.rightMotor*0.00007124683339;//0.00007302800423;//0.00007356235548;//0.00007391858965;//0.00007427482381;//0.00007436388235;//fr //convert qecounts into m 
  qe2 = msg.leftMotor*0.00007121120998;//0.00007302800423;//0.00007356235548;//0.00007391858965;//0.00007427482381;//0.00007432825894; //fl

  dist = (qe1+qe2)/2;
  dth = (qe1-qe2)/2;
  dth = dth/.147701; //convert to radians of rotation .14605m is 11.5in/2 (half of wheel base) [.147701 is a calibrated value]
  dx = dist*cos(th);
  dy = dist*sin(th);
  x += dx;
  y += dy;
  th += dth;
 //we need a quaternion to describe rotation in 3d
  

  dt =(current_time-last_time).toSec(); //calc velocities
  vx = dist/dt; //v is in base_link frame
  vy = 0;
  vth = dth/dt;
 
  nav_msgs::Odometry odom; //create nav_msgs::odometry 
  odom.header.stamp = current_time;
  odom.header.frame_id = "odom";

  odom.pose.pose.position.x = x; //set positions 
  odom.pose.pose.position.y = y;
  odom.pose.pose.position.z = 0.0;
  odom.pose.pose.orientation = odom_quat;
  
  odom.child_frame_id = "base_link"; // set child frame and set velocity in twist message
  odom.twist.twist.linear.x =vx;
  odom.twist.twist.linear.y =vy;
  odom.twist.twist.angular.z =vth;
  
  odom_pub.publish(odom);  //publish odom message
 
  last_time = current_time;
  */
