#!/usr/bin/env python

"""
#The differential controller script is responsible sending velocity commands
#to the Arduino that controls de DC Motors. Here the Twist message coming from 
#the teleop device is converted into MotorCommand message used by the Arduino.
"""

import rospy
from deepfind_package.msg import MotorCommand
from geometry_msgs.msg import Twist

# Motor global variables 
global dict
dict = {'MOTOR_CAP': 40, 'FORWARD': 0, 'BACKWARD': 1}

# Converts incoming Twist message to Motorommand message and
# sends the command to the Arduino.
def diff_control_callback(twistData):
  command = MotorCommand()
  command.leftMotorPower = int((twistData.linear.x + twistData.angular.z) * dict['MOTOR_CAP'])
  command.rightMotorPower = int((twistData.linear.x - twistData.angular.z) * dict['MOTOR_CAP'])

  if command.leftMotorPower > 0:
  	command.leftMotorDirection = dict['FORWARD']
  else:
    command.leftMotorDirection = dict['BACKWARD']
  
  if command.rightMotorPower > 0:
    command.rightMotorDirection = dict['FORWARD']
  else:
    command.rightMotorDirection = dict['BACKWARD']

  command.leftMotorPower = abs(command.leftMotorPower)
  command.rightMotorPower = abs(command.rightMotorPower)
 	
  pub = rospy.Publisher('motor_speed', MotorCommand, queue_size = 10)
  pub.publish(command)

# Main function, waits for new Twist messages to arrive
# Creates node and subscriber
def diff_controller_listener():
  rospy.init_node('differential_controller')
  rospy.Subscriber('cmd_vel', Twist, diff_control_callback)
  rospy.spin()

if __name__ == '__main__':
    diff_controller_listener()


