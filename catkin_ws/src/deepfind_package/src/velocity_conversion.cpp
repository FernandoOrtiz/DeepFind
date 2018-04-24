
/*
  The purpose of this class to take the input of the motor encoders
  and and convert it into a Odometry message that will be used 
  by the navigation system.
*/

#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <deepfind_package/EncodersData.h>
#include <deepfind_package/Velocity.h>
#include <nav_msgs/Odometry.h>


//constants in meters
const double WHEEL_SEPARATION = 0.29845;
const double WHEEL_DIAMETER = 0.13335;

//error managing
const double ODOM_TURN_MULTIPLIER = 1.0;

//global variables
ros::Time currentTime, lastTime;
ros::Publisher odomPub;
double x = 0;
double y = 0;
double th = 0;
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


//Converts the encoder ticks to meters
double ticksToMeters(double ticks){
  return ((ticks/360)*(3.14159265359*WHEEL_DIAMETER));
}

/*
  Subscriber callback function.
  Creates the ODmotry mesage and publishes it
*/
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
 

  //pose and transform
  geometry_msgs::Quaternion odomQuat;
  nav_msgs::Odometry odom;
  tf::TransformBroadcaster odomBroadcaster;
  tf::Transform odomTransform;
  
  double dxy = (distanceTraveled1 + distanceTraveled2) / 2;
  double dth = (((distanceTraveled1 - distanceTraveled2) / WHEEL_SEPARATION)) * ODOM_TURN_MULTIPLIER;

  x += dxy * cosf(th);
  y += dxy * sinf(th);
  th += dth;

  //linear and angular velocities
  double v = dxy/timeDelta; //  m/s
  double w = dth/timeDelta; //  deg/s

  odomQuat = tf::createQuaternionMsgFromRollPitchYaw(0,0,th);
  tf::Quaternion q;
  q.setRPY(0,0,th);
  

  odomTransform.setOrigin(tf::Vector3(x,y,0.0));
  odomTransform.setRotation(q);

  //position and orientation
  odom.pose.pose.position.x = x;
  odom.pose.pose.position.y = y;
  odom.pose.pose.position.z = 0.0;
  odom.pose.pose.orientation = odomQuat;

  //velocity
  odom.twist.twist.linear.x = v;
  odom.twist.twist.linear.y = 0.0;
  odom.twist.twist.linear.z = 0.0;
  odom.twist.twist.angular.x = 0.0;
  odom.twist.twist.angular.y = 0.0;
  odom.twist.twist.angular.z = w;

  //publish
  odomBroadcaster.sendTransform(tf::StampedTransform(odomTransform, ros::Time::now(), "map", "odometry"));
  odomPub.publish(odom);
  

  //update variables 
  lastTime = currentTime;
  lastCount1 = msg.leftMotor;
  lastCount2 = msg.rightMotor;

}

//Main function, initializes the ros node, subcribers and publishers
//Waits encoders_data msg
int main(int argc, char **argv){

  //node
  ros::init(argc, argv, "velocity_publisher");
  ros::NodeHandle nh; 

  //publisher
  odomPub = nh.advertise<deepfind_package::Velocity>("/vel", 50);

  //subscriber
  ros::Subscriber encoderSub = nh.subscribe("/encoder", 1000, quadencCallback);

  lastTime.useSystemTime();
  currentTime.useSystemTime();
  lastTime = ros::Time::now();

  //wait
  ros::spin();
  return 0;
}







// deepfind_package::Velocity vel;
  // vel.header.stamp = ros::Time::now();
  // vel.linearX = v;
  // vel.angularZ = w;
  