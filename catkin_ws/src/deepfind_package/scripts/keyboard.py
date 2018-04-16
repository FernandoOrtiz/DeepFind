#!/usr/bin/env python

import getch
import rospy
from deepfind_package.msg import keyboard
from std_msgs.msg import String

def keyboard_listener():
	#keyboard = keyboard()
	pub = rospy.Publisher('key', keyboard, queue_size = 10)
	rospy.init_node('keyboard')
	keyb = keyboard()
	while not rospy.is_shutdown():
		k = ord(getch.getch())
		if k == 111:
			keyb.origin = 1
			rospy.loginfo("Key pressed: O")
		elif k == 108:
			keyb.landmark = 1
			rospy.loginfo("Key pressed: L")
		else:
			pass
		pub.publish(keyb)
		keyb.origin = 0
		keyb.landmark = 0

if __name__=='__main__':
	keyboard_listener()
