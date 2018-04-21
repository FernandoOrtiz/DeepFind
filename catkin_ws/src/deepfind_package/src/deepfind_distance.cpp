#include <geometry_msgs/PoseStamped.h>
#include <deepfind_distance.h>
#include <deepfind_package/keyboard.h>
#include <math.h>
#include <ros/ros.h>
#include <ros/console.h>

int main(int argc, char* argv[]) {
     ros::init(argc, argv, "distance_node");

     DeepFindDistance d;

     ros::spin();

     return 0;
}

void DeepFindDistance::timerCallback(const ros::TimerEvent&) {
     //ROS_INFO("Timer");
     int a = 0;
}

DeepFindDistance::DeepFindDistance () {
     ros::NodeHandle private_nh_("~");

     private_nh_.param("still_time", still_time_, 3.0);

     //Subcribers setup
     keySubscriber_ = node_.subscribe("key", 1000, &DeepFindDistance::keyCallback, this);
     poseSubscriber_ = node_.subscribe("slam_out_pose", 1000, &DeepFindDistance::poseCallback, this);
     //ros::Timer timer1 = node_.createTimer(ros::Duration(still_time_), timerCallback);

     //Publisher setup
     distancePublisher_ = node_.advertise<deepfind_package::distance_traveled>("distance_traveled", 1000);

     initial_pose = true;

     ROS_INFO("DeepFindDistance still_time: %lf", still_time_);
}

void DeepFindDistance::keyCallback(const deepfind_package::keyboard& key) {
     bool pressed_origin = key.origin;
     bool pressed_landmark = key.landmark;

     //If origin button was pressed mark current position as the new origin
     if(pressed_origin) {
     update(origin, landmark1);
     ROS_INFO("DeepFindDistance origin set to [%.3f, %.3f]", origin.pose.position.x, origin.pose.position.y); 
     }

     //If landmark button was pressed mark current position as a landmark
     if(pressed_landmark) {
     update(landmark2, landmark1);
     ROS_INFO("DeepFindDistance landmark set to [%.3f, %.3f]", landmark2.pose.position.x, landmark2.pose.position.y);   
     }
}

void DeepFindDistance::poseCallback(const geometry_msgs::PoseStamped& curr) {
     //If first time, set initial pose
     if(initial_pose) {
     initial_pose = false;

     //Set intial pose (origin) to current pose
     update(origin, curr);
     }

     //Update current pose
     update(landmark1, curr);

     //Calculate distance from origin and from previous landmark
     calculateDistance();

     //Update distances values
     deepfind_distance.distance_origin = distanceOrigin;
     deepfind_distance.distance_traveled = distanceTraveled;

     //Publish distances to topic
     distancePublisher_.publish(deepfind_distance);
}

void DeepFindDistance::update(geometry_msgs::PoseStamped& msg1, const geometry_msgs::PoseStamped& msg2) {
     //Set current header
     msg1.header.stamp = msg2.header.stamp;
     msg1.header.frame_id = msg2.header.frame_id;

     //Set current position
     msg1.pose.position.x = msg2.pose.position.x;
     msg1.pose.position.y = msg2.pose.position.y;
     msg1.pose.position.z = msg2.pose.position.z;

     //Set current orientation
     msg1.pose.orientation.x = msg2.pose.orientation.x;
     msg1.pose.orientation.y = msg2.pose.orientation.y;
     msg1.pose.orientation.z = msg2.pose.orientation.z;
     msg1.pose.orientation.w = msg2.pose.orientation.w;
}

double DeepFindDistance::calculateDistance() {
     //Calculate distance from origin to current position
     distanceOrigin = std::sqrt(pow(origin.pose.position.x - landmark1.pose.position.x, 2) + pow(origin.pose.position.y - landmark1.pose.position.y, 2));

     //Calculate distance from previous landmark to current position
     distanceTraveled = std::sqrt(pow(landmark2.pose.position.x - landmark1.pose.position.x, 2) + pow(landmark2.pose.position.y - landmark1.pose.position.y, 2));
}






