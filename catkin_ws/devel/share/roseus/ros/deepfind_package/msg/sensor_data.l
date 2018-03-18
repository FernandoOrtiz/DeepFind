;; Auto-generated. Do not edit!


(when (boundp 'deepfind_package::sensor_data)
  (if (not (find-package "DEEPFIND_PACKAGE"))
    (make-package "DEEPFIND_PACKAGE"))
  (shadow 'sensor_data (find-package "DEEPFIND_PACKAGE")))
(unless (find-package "DEEPFIND_PACKAGE::SENSOR_DATA")
  (make-package "DEEPFIND_PACKAGE::SENSOR_DATA"))

(in-package "ROS")
;;//! \htmlinclude sensor_data.msg.html
(if (not (find-package "SENSOR_MSGS"))
  (ros::roseus-add-msgs "sensor_msgs"))


(defclass deepfind_package::sensor_data
  :super ros::object
  :slots (_imu _lidar _encoder ))

(defmethod deepfind_package::sensor_data
  (:init
   (&key
    ((:imu __imu) (instance deepfind_package::imu_data :init))
    ((:lidar __lidar) (instance sensor_msgs::LaserScan :init))
    ((:encoder __encoder) (instance deepfind_package::encoders_data :init))
    )
   (send-super :init)
   (setq _imu __imu)
   (setq _lidar __lidar)
   (setq _encoder __encoder)
   self)
  (:imu
   (&rest __imu)
   (if (keywordp (car __imu))
       (send* _imu __imu)
     (progn
       (if __imu (setq _imu (car __imu)))
       _imu)))
  (:lidar
   (&rest __lidar)
   (if (keywordp (car __lidar))
       (send* _lidar __lidar)
     (progn
       (if __lidar (setq _lidar (car __lidar)))
       _lidar)))
  (:encoder
   (&rest __encoder)
   (if (keywordp (car __encoder))
       (send* _encoder __encoder)
     (progn
       (if __encoder (setq _encoder (car __encoder)))
       _encoder)))
  (:serialization-length
   ()
   (+
    ;; deepfind_package/imu_data _imu
    (send _imu :serialization-length)
    ;; sensor_msgs/LaserScan _lidar
    (send _lidar :serialization-length)
    ;; deepfind_package/encoders_data _encoder
    (send _encoder :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; deepfind_package/imu_data _imu
       (send _imu :serialize s)
     ;; sensor_msgs/LaserScan _lidar
       (send _lidar :serialize s)
     ;; deepfind_package/encoders_data _encoder
       (send _encoder :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; deepfind_package/imu_data _imu
     (send _imu :deserialize buf ptr-) (incf ptr- (send _imu :serialization-length))
   ;; sensor_msgs/LaserScan _lidar
     (send _lidar :deserialize buf ptr-) (incf ptr- (send _lidar :serialization-length))
   ;; deepfind_package/encoders_data _encoder
     (send _encoder :deserialize buf ptr-) (incf ptr- (send _encoder :serialization-length))
   ;;
   self)
  )

(setf (get deepfind_package::sensor_data :md5sum-) "9fccc7b309d5bf5d740dd999ac988ed8")
(setf (get deepfind_package::sensor_data :datatype-) "deepfind_package/sensor_data")
(setf (get deepfind_package::sensor_data :definition-)
      "imu_data imu
sensor_msgs/LaserScan lidar
encoders_data encoder

================================================================================
MSG: deepfind_package/imu_data
Header header
float64 yaw
float64 pitch 
float64 roll
float64 acc_x
float64 acc_y
float64 acc_z
float64 gyr_x
float64 gyr_y
float64 gyr_z
float64 mag_x
float64 mag_y
float64 mag_z


================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: sensor_msgs/LaserScan
# Single scan from a planar laser range-finder
#
# If you have another ranging device with different behavior (e.g. a sonar
# array), please find or create a different message, since applications
# will make fairly laser-specific assumptions about this data

Header header            # timestamp in the header is the acquisition time of 
                         # the first ray in the scan.
                         #
                         # in frame frame_id, angles are measured around 
                         # the positive Z axis (counterclockwise, if Z is up)
                         # with zero angle being forward along the x axis
                         
float32 angle_min        # start angle of the scan [rad]
float32 angle_max        # end angle of the scan [rad]
float32 angle_increment  # angular distance between measurements [rad]

float32 time_increment   # time between measurements [seconds] - if your scanner
                         # is moving, this will be used in interpolating position
                         # of 3d points
float32 scan_time        # time between scans [seconds]

float32 range_min        # minimum range value [m]
float32 range_max        # maximum range value [m]

float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)
float32[] intensities    # intensity data [device-specific units].  If your
                         # device does not provide intensities, please leave
                         # the array empty.

================================================================================
MSG: deepfind_package/encoders_data
int32 leftMotor
int32 rightMotor
")



(provide :deepfind_package/sensor_data "9fccc7b309d5bf5d740dd999ac988ed8")


