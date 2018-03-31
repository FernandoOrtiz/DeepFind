#!/bin/bash

#Install Git
sudo apt-get install git -y

#Install git workspace
cd ~
git clone https://github.com/ortizfer/DeepFind.git

#Install Ardiuno
sudo apt-get install arduino -y

#Install ROS
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
sudo apt-get update
sudo apt-get install ros-kinetic-desktop-full -y
sudo rosdep init
rosdep update
echo "source ~/DeepFind/catkin_ws/devel/setup.bash" >> ~/.bashrc
source ~/.bashrc

#Install VN100 Dependancies
sudo apt-get install python3-dev -y
sudo apt-get install python3-yaml -y
sudo apt-get install python3-pip -y
sudo pip3 install rospkg
sudo pip3 install catkin_pkg
sudo pip3 install pymorse 
cd ~/DeepFind/libraries/vnproglib-1.1/python
sudo python3 setup.py install

#Install Navigation
sudo apt-get install ros-kinetic-navigation -y
sudo apt-get install ros-kinetic-geographic-msgs -y

#Install Joy and PS3 driver
sudo apt-get install ros-kinetic-joy -y
sudo apt-get install xboxdrv -y
sudo apt-get install jstest-gtk -y

#Install Rosserial and Hector_SLAM
cd ~/DeepFind/catkin_ws/src
git clone  https://github.com/tu-darmstadt-ros-pkg/hector_slam
git clone https://github.com/ros-drivers/rosserial.git

cd ~/DeepFind/catkin_ws/
catkin_make
