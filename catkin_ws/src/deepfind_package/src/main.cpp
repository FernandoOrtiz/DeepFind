#include <ros/ros.h>
#include <DeepFindDistance.h>

int main(int argc, char* argv[]) {
	ros::init(argc, argv, "distance_node");

	DeepFindDistance d;

	ros::spin();

	return 0;
}