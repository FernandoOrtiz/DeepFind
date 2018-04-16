import rospy
import message_filters
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

def callback(odometry, twist):
    odom = Odometry()
    odom.header.stamp = odometry.header.stamp
    odom.header.frame_id = odometry.header.frame_id

    odom.pose.pose.position.x = odometry.pose.pose.position.x
    odom.pose.pose.position.y = odometry.pose.pose.position.y
    odom.pose.pose.position.z = odometry.pose.pose.position.z

    odom.pose.pose.orientation.x = odometry.pose.orientation.x
	odom.pose.pose.orientation.y = odometry.pose.orientation.y
	odom.pose.pose.orientation.z = odometry.pose.orientation.z
	odom.pose.pose.orientation.w = odometry.pose.orientation.w

	odom.twist.twist.linear.x = twist.linear.x
	odom.twist.twist.angular.z = twist.angular.z

	pub = rospy.Publisher('odom', Odometry, queue_size = 10)
	pub.publish(odom)


def odom_twist_listener():
	rospy.init_node('odom_twist')
	odom_sub = message_filters.Subscriber('scanmatch_odom', Odometry)
	twist_sub = message_filters.Subscriber('cmd_vel', Twist)

	ts = message_filters.TimeSynchronizer([odom_sub, twist_sub], 10)
	ts.registerCallback(callback)
	rospy.spin()
  
if __name__ == '__main__':
	odom_twist_listener()