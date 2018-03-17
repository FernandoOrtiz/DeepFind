#!/usr/bin/env python

import rospy
#from std_msgs.msg import *
from deepfind_package.msg import motor_command
from geometry_msgs.msg import Twist

global dict
dict = {'MOTOR_CAP': 40, 'FOWARD': 0, 'BACKWARD': 1}


def diffControlCallback(twistData):
  command.leftMotorPower = (twistData.linerar.x + twistData.angualr.z) * dict['MOTOR_CAP']
  command.rightMotorPower = (twistData.linerar.x - twistData.angualr.z) * dict['MOTOR_CAP']

  if command.leftMotorPower > 0:
  	command.leftMotorDirection = dict['FOWARD']
  else:
    command.leftMotorDirection = dict['BACKWARD']
  
  if command.rightMotorPower > 0:
    command.rightMotorDirection = dict['FOWARD']
  else:
  	motor2Direction = dict['BACKWARD']

 	
  pub = rospy.Publisher('motor_speed', motor_command, queue_size = 10)
  pub.publish(command)


def diffControllerListener():
	rospy.init_node('android_listener')
	rospy.Subscriber('cmd_vel', Twist, diffControlCallback)
	rospy.spin()

if __name__ == '__main__':
    diffControllerListener()