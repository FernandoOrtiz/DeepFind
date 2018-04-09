#include <sensor_msgs/Joy.h>
#include <geometry_msgs/PoseStamped.h>
#include <deepfind_distance.h>
#include <math.h>
#include <ros/ros.h>

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
	private_nh_.param("button", button_, 0);

	//Subcribers setup
	joySubscriber_ = node_.subscribe("joy", 1000, &DeepFindDistance::joyCallback, this);
	poseSubscriber_ = node_.subscribe("slam_out_pose", 1000, &DeepFindDistance::poseCallback, this);
	//ros::Timer timer1 = node_.createTimer(ros::Duration(still_time_), timerCallback);

	//Publisher setup
	distancePublisher_ = node_.advertise<deepfind_package::distance_traveled>("distance_traveled", 1000);

	initial_pose = true;

	//ROS_INFO("DeepFindDistance still_time: %f", still_time_);
	//ROS_INFO("DeepFindDistance button: %d", button_);

}

void DeepFindDistance::joyCallback(const sensor_msgs::Joy::ConstPtr& joy) {
	bool pressed = joy->buttons[button_];

	//If button_ was pressed mark current position as a landmark
	if(pressed) {
		setLandmark();	
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
		
void DeepFindDistance::setLandmark() {
	//Set landmark2 to current pose
	update(landmark2, landmark1);

	//ROS_INFO("DeepFindDistance landmark updated to x = %f, y = %f and z = %f", landmark1.pose.position.x, landmark1.pose.position.y, landmark1.pose.position.z);
}






