#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <deepfind_package/distance_traveled.h>
#include <deepfind_package/keyboard.h>

class DeepFindDistance {
  public:
   DeepFindDistance();

   void keyCallback(const deepfind_package::keyboard& message);
   void poseCallback(const geometry_msgs::PoseStamped& curr);
   void timerCallback(const ros::TimerEvent& timer);

   void update(geometry_msgs::PoseStamped& msg1, const geometry_msgs::PoseStamped& msg2);
   double calculateDistance();

  private:
   geometry_msgs::PoseStamped landmark1;
   geometry_msgs::PoseStamped landmark2;
   geometry_msgs::PoseStamped origin;

   bool initial_pose;	
   double distanceOrigin;
   double distanceTraveled;

   ros::NodeHandle node_;

   //Subscribers
   ros::Subscriber keySubscriber_;
   ros::Subscriber poseSubscriber_;

   //Publishers
   deepfind_package::distance_traveled deepfind_distance;
   ros::Publisher distancePublisher_;

   //Parameters
   double still_time_;
};
