#!/usr/bin/env python

import getch
import rospy
from deepfind_package.msg import keyboard
from std_msgs.msg import String

def keyboard_listener():
  #Initialize ROS node, publisher and keyboard object
  pub = rospy.Publisher('key', keyboard, queue_size = 10)
  rospy.init_node('keyboard')
  keyb = keyboard()
  
  #While node is stil active get key pressed and do some action
  while not rospy.is_shutdown():
    k = ord(getch.getch())
    if k == 111: #Letter O ASCII key code
      keyb.origin = 1
      rospy.loginfo("Key pressed: Origin")
    elif k == 108: #Letter L ASCII key code
      keyb.landmark = 1
      rospy.loginfo("Key pressed: Landmark")
    else:
      rospy.loginfo("Key pressed: Not supported")

    #Publish and reset key values
    pub.publish(keyb)
    keyb.origin = 0
    keyb.landmark = 0

if __name__=='__main__':
    keyboard_listener()
