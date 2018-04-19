#include <ros/ros.h>
#include <geometry_msgs/PoseWithCovarianceStamped.h>
#include <deepfind_package/distance_traveled.h>
#include <deepfind_package/keyboard.h>

class DeepFindDistance {
	public:
		DeepFindDistance();

		void keyCallback(const deepfind_package::keyboard& message);
		void poseCallback(const geometry_msgs::PoseWithCovarianceStamped& curr);
		void timerCallback(const ros::TimerEvent& timer);

		void update(geometry_msgs::PoseWithCovarianceStamped& msg1, const geometry_msgs::PoseWithCovarianceStamped& msg2);
		double calculateDistance();

	private:
		geometry_msgs::PoseWithCovarianceStamped landmark1;
		geometry_msgs::PoseWithCovarianceStamped landmark2;
		geometry_msgs::PoseWithCovarianceStamped origin;
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
