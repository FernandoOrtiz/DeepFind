
(cl:in-package :asdf)

(defsystem "deepfind_package-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "encoders_data" :depends-on ("_package_encoders_data"))
    (:file "_package_encoders_data" :depends-on ("_package"))
    (:file "imu_data" :depends-on ("_package_imu_data"))
    (:file "_package_imu_data" :depends-on ("_package"))
    (:file "lidar_data" :depends-on ("_package_lidar_data"))
    (:file "_package_lidar_data" :depends-on ("_package"))
    (:file "sensor_data" :depends-on ("_package_sensor_data"))
    (:file "_package_sensor_data" :depends-on ("_package"))
  ))