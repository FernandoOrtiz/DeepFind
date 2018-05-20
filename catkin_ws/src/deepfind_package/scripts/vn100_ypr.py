#! /usr/bin/env python3

import rospy
from sensor_msgs.msg import Imu
from vnpy import *


__vn100_path = '/dev/ttyUSB0'
__vn100_baud_rate = 115200


vn100 = EzAsyncData.connect(__vn100_path, __vn100_baud_rate)
print('Initialized')


def talker():
    pub = rospy.Publisher('vn100_yaw', Imu, queue_size=10)
    rospy.init_node('vn100')
    rate = rospy.Rate(7.1) # 10hz
    message = Imu()

    message.orientation_covariance[0] = -1
    message.angular_velocity_covariance[0] = -1
    message.linear_acceleration_covariance[0] = -1

    for i in range(1,9):
        message.orientation_covariance[i] = 0
        message.angular_velocity_covariance[i] = 0
        message.linear_acceleration_covariance[i] = 0


    while not rospy.is_shutdown():
        message.header.stamp = rospy.Time.now()
        message.header.frame_id = 'base_link'
        values = vn100.next_data()
       
        message.orientation.w = 0
        message.orientation.x = values.yaw_pitch_roll.x*np.pi/180
        message.orientation.y = values.yaw_pitch_roll.y*np.pi/180
        message.orientation.z = values.yaw_pitch_roll.z*np.pi/180

        message.linear_acceleration.x = values.acceleration.x
        message.linear_acceleration.y = values.acceleration.y
        message.linear_acceleration.z = values.acceleration.z

        message.angular_velocity.x = values.angular_rate.x
        message.angular_velocity.y = values.angular_rate.y
        message.angular_velocity.z = values.angular_rate.z

        hello_str = "VN100 {}".format(rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publish(message)
        rate.sleep()


print (__name__)

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
