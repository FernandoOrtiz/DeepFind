#!/usr/bin/env python

import getch
import rospy
from std_msgs.msg import String 
from std_msgs.msg import Int32

def keyboard_listener():
	keyboard = keyboard()
	pub = rospy.Publisher('key', Int32, queue_size = 10)	
<<<<<<< HEAD
    	rospy.init_node('keyboard')
    	while not rospy.is_shutdown():
		k = ord(getch.getch())
    		if k == 79: #Key = o/O
    			keyboard.origin = 1
    		elif k == 76: #Key = i/I
    			keyboard.landmark = 1
    		else:
    			pass
  	   	pub.publish(keyboard);
  	    	keyboard.origin = 0
    		keyboard.landmark = 0;
=======
    rospy.init_node('keyboard')
    while not rospy.is_shutdown():
    	k = ord(getch.getch())
    	if k == 79: #Key = o/O
    		keyboard.origin = 1
    	elif k == 76: #Key = i/I
    		keyboard.landmark = 1
    	else:
    		pass
  	    pub.publish(keyboard)
  	    keyboard.origin = 0
    	keyboard.landmark = 0
>>>>>>> 8a43419b976b544debb4e9d6748f10b1f5cdeddb


if __name__=='__main__':
	keyboard_listener()
