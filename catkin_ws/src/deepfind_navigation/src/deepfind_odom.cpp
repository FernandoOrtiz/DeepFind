#include <ros/ros.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include "deepfind_navigation/encoders_data.h" 
#include <math.h>

#define RovWid 0.25
#define Pi 3.141592865358979
#define TicksPerRev 1050
#define WheelDia 0.13

int left, right;

void encodersCallback(const deepfind_navigation::encoders_data& msg) {
  left = msg.leftMotor;
  right = msg.rightMotor;
  ROS_INFO("Left motor: %d, Right motor: %d", left, right);
}


int main(int argc, char** argv) {
  ros::init(argc, argv, "odometry_publisher");

  ros::NodeHandle nh;
  ros::Publisher odom_pub = nh.advertise<nav_msgs::Odometry>("odom", 50);
  ros::Subscriber sub = nh.subscribe("encoders", 100, encodersCallback);
  tf::TransformBroadcaster odom_broadcaster;

  double vx = 0.0;
  double vy = 0.0;
  double vth = 0.0;

  float DeltaLeft = 0;
  float DeltaRight = 0;
  float PreviousRight = 0;
  float PreviousLeft = 0;

  float Theta = 0;
  float X = 0;
  float Y = 0;

  float Circum, DisPerTick, expr1,right_minus_left;

  ros::Time current_time, last_time;
  current_time = ros::Time::now();
  last_time = ros::Time::now();

  ros::Rate r(5);
  Circum = Pi * WheelDia;
  DisPerTick = Circum / TicksPerRev;

  while(nh.ok()) {

        ros::spinOnce();               // check for incoming messages
        current_time = ros::Time::now();

        DeltaRight = (right - PreviousRight) * DisPerTick;
        DeltaLeft = (left - PreviousLeft) * DisPerTick;
        PreviousRight = right;
        PreviousLeft = left;


        if (DeltaLeft == DeltaRight){
              X += DeltaLeft * cos(Theta);
              Y += DeltaLeft * sin(Theta);
        }
        else{
               expr1 = RovWid * 2 * (DeltaRight + DeltaLeft)/ 2.0 / (DeltaRight - DeltaLeft);
               right_minus_left = DeltaRight - DeltaLeft;
               X += expr1 * (sin(right_minus_left / (RovWid *2) + Theta) - sin(Theta));
               Y -= expr1 * (cos(right_minus_left / (RovWid *2) + Theta) - cos(Theta));
               Theta += right_minus_left / (RovWid *2);
               Theta = Theta - ((2 * Pi) * floor( Theta / (2 * Pi)));
        }

        geometry_msgs::Quaternion odom_quat = tf::createQuaternionMsgFromYaw(Theta);

        geometry_msgs::TransformStamped odom_trans;
        odom_trans.header.stamp = current_time;
        odom_trans.header.frame_id = "odom";
        odom_trans.child_frame_id = "base_link";

        odom_trans.transform.translation.x = X;
        odom_trans.transform.translation.y = Y;
        odom_trans.transform.translation.z = 0.0;
        odom_trans.transform.rotation = odom_quat;

        odom_broadcaster.sendTransform(odom_trans);

        nav_msgs::Odometry odom;
        odom.header.stamp = current_time;
        odom.header.frame_id = "odom";

        odom.pose.pose.position.x = X;
        odom.pose.pose.position.y = Y;
        odom.pose.pose.position.z = 0.0;
        odom.pose.pose.orientation = odom_quat;

        odom.child_frame_id = "base_link";
        odom.twist.twist.linear.x = 0;
        odom.twist.twist.linear.y = 0;
        odom.twist.twist.angular.z = 0;

        odom_pub.publish(odom);

        last_time = current_time;
        r.sleep();
	}
}
