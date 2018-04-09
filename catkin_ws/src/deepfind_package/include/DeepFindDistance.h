#include <std_msgs/Header.h>

class DeepFindDistance {
	public:
		DeepFindDistance();

		void joyCallback(const sensor_msgs::Joy::ConstPtr& joy);
		void poseCallback(const geometry_msgs::PoseStamped& curr);
		void timerCallback(const ros::TimerEvent& timer);

		void update(const geometry_msgs::PoseStamped& msg1, const geometry_msgs::PoseStamped& msg2);
		double calculateDistance();
		void setLandmark();

	private:
		geometry_msgs::Pose landmark1;
		geometry_msgs::Pose landmark2;
		geometry_msgs::Pose origin;
		bool initial_pose;
		double distanceOrigin;
		double distanceTraveled;

		ros::NodeHandle node_;

		//Subscribers
		ros::Subscriber joySubscriber_;
		ros::Subscriber slamPoseSubscriber_;

		//Timer
		ros::Timer timer1_;

		//Publishers
		deepfind_package::distance_traveled deepfind_distance;
		ros::Publisher distancePublisher_;

		//Parameters
		double still_time_;
		int button_;
}
