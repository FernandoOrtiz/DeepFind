#include <ros/ros.h>
#include <deepfind_distance.h>

int main(int argc, char* argv[]) {
	ros::init(argc, argv, "distance_node");

	DeepFindDistance d;

	ros::spin();

	return 0;
}
