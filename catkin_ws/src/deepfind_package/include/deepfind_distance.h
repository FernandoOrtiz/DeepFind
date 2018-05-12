#include <ros/ros.h>
#include <geometry_msgs/PoseStamped.h>
#include <deepfind_package/Distance.h>
#include <deepfind_package/keyboard.h>

class DeepFindDistance {
  public:
   DeepFindDistance();

   void keyCallback(const deepfind_package::keyboard& message);
   void poseCallback(const geometry_msgs::PoseStamped& curr);

   void update(geometry_msgs::PoseStamped& msg1, const geometry_msgs::PoseStamped& msg2);
   double calculateDistance();

  private:
   geometry_msgs::PoseStamped landmark1;
   geometry_msgs::PoseStamped landmark2;
   geometry_msgs::PoseStamped origin;

   bool initialPose;
   double absoluteDistOrigin;   //Absolute distance from origin	
   double absoluteDistLandmark; //Absolute distance from previous landmark

   ros::NodeHandle node;

   //Subscribers
   ros::Subscriber keySubscriber;
   ros::Subscriber poseSubscriber;

   //Publishers
   deepfind_package::Distance deepfindDistance;
   ros::Publisher distancePublisher;
};
