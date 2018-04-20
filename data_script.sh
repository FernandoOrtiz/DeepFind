#! /bin/bash

roslaunch deepfind_package deepfind_robot.launch
roslaunch rplidar_ros view_slam.launch
python3 ~/Deepfind/catkin_ws/src/deepfind_package/scripts/vn100_full.py
rosrun deepfind_package data_recollection.py
cd Deepfind
rosbag record --duration=30m /sensor_data
