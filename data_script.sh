#! /bin/bash

roslaunch rplidar_ros view_slam.launch &
sleep 5 python3 ~/Deepfind/catkin_ws/src/deepfind_package/scripts/vn100_full.py &
rosrun deepfind_package data_recollection.py &
cd ~/Deepfind 
#sleep 5 rosbag record --duration=30m /sensor_data
