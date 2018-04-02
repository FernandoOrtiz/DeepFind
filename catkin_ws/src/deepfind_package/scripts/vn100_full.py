#! /usr/bin/env python3

import rospy
from deepfind_package.msg import imu_data
from vnpy import *


__vn100_path = '/dev/ttyUSB1'
__vn100_baud_rate = 115200


vn100 = EzAsyncData.connect(__vn100_path, __vn100_baud_rate)
print('Initialized')


def talker():
    pub = rospy.Publisher('vn100_yaw', imu_data, queue_size=10)
    rospy.init_node('vn100')
    rate = rospy.Rate(10) # 10hz
    message = imu_data()

    while not rospy.is_shutdown():
        values = vn100.next_data();
        
        if(values.yaw_pitch_roll.x < 0):
            values.yaw_pitch_roll.x += 360

        if(values.yaw_pitch_roll.y < 0):
            values.yaw_pitch_roll.y += 360
        
        if(values.yaw_pitch_roll.z < 0):
            values.yaw_pitch_roll.z += 360

        message.yaw = values.yaw_pitch_roll.x
        message.pitch = values.yaw_pitch_roll.y
        message.roll = values.yaw_pitch_roll.z

        message.acc_x = values.acceleration.x
        message.acc_y = values.acceleration.y
        message.acc_z = values.acceleration.z

        message.gyr_x = values.angular_rate.x
        message.gyr_y = values.angular_rate.y
        message.gyr_z = values.angular_rate.z

        message.mag_x = values.magnetic.x
        message.mag_y = values.magnetic.y
        message.mag_z = values.magnetic.z

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
