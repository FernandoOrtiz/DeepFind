#include <sensor_msgs/Joy.h>
#include <geometry_msgs/PoseStamped.h>
#include <DeepFindDistance.h>
#include <cmath.h>

DeepFindDistance::DeepFindDistance () {
	ros::NodeHandle private_nh_("~");

	private_nh_.param("still_time", still_time_, 3.0);
	private_nh_.param("button", button_, 0);

	//Subcribers setup
	joySubscriber_ = node_.subscribe("joy", 1000, &DeepFindDistance::joyCallback, this);
	poseCallback_ = node_.subscribe("slam_out_pose", 1000, &DeepFindDistance::poseCallback, this);
	timer1_ = node_.createTimer(ros::Duration(still_time), timerCallback);

	//Publisher setup
	distancePublisher_ = node.advertise<deepfind_package::distance_traveled>("distance_traveled", 1000);

	initial_pose = true;

	ROS_INFO("DeepFindDistance still_time: %f", still_time_);
	ROS_INFO("DeepFindDistance button: %d", button_);

}

void DeepFindDistance::joyCallback(const sensor_msgs::Joy::ConstPtr& joy) {
	bool pressed = joy->buttons[button_];

	//If button_ was pressed mark current position as a landmark
	if(pressed) {
		setLandmark();	
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
	calculateDistance()

	//Update distances values
	deepfind_distance.distance_origin = distanceOrigin;
	deepfind_distance.distance_traveled = distanceTraveled;

	//Publish distances to topic
	distancePublisher_.publish(deepfind_distance);
}

void DeepFindDistance::timerCallback(const ros::TimerEvent& timer) {
	ROS_INFO("Timer");
}

void DeepFindDistance::update(const geometry_msgs::PoseStamped& msg1, const geometry_msgs::PoseStamped& msg2) {
	//Set current header
	msg1.header.stamp = msg2->header.stamp;
	msg1.header.frame_id = msg2->header.frame_id;

	//Set current position
	msg1.pose.position.x = msg2->pose.position.x;
	msg1.pose.position.y = msg2->pose.position.y;
	msg1.pose.position.z = msg2->pose.position.z;

	//Set current orientation
	msg1.pose.orientation.x = msg2->pose.orientation.x;
	msg1.pose.orientation.y = msg2->pose.orientation.y;
	msg1.pose.orientation.z = msg2->pose.orientation.z;
	msg1.pose.orientation.w = msg2->pose.orientation.w;
}

float DeepFindDistance::calculateDistance() {
	//Calculate distance from origin to current position
	distanceOrigin = std::sqrt(pow(origin.position.x - landmark1.position.x, 2) + pow(origin.position.y - landmark1.position.y, 2));

	//Calculate distance from previous landmark to current position
	distanceTraveled = std::sqrt(pow(landmark2.position.x - landmark1.position.x, 2) + pow(landmark2.position.y - landmark1.position.y, 2));
}
		
void DeepFindDistance::setLandmark() {
	//Set landmark2 to current pose
	update(landmark2, landmark1);

	ROS_INFO("DeepFindDistance landmark updated to x = %f, y = %f and z = %f", landmark1.pose.position.x, landmark1.pose.position.y, landmark1.pose.position.z);
}