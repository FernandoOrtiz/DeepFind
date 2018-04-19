;; Auto-generated. Do not edit!


(when (boundp 'deepfind_package::imu_data)
  (if (not (find-package "DEEPFIND_PACKAGE"))
    (make-package "DEEPFIND_PACKAGE"))
  (shadow 'imu_data (find-package "DEEPFIND_PACKAGE")))
(unless (find-package "DEEPFIND_PACKAGE::IMU_DATA")
  (make-package "DEEPFIND_PACKAGE::IMU_DATA"))

(in-package "ROS")
;;//! \htmlinclude imu_data.msg.html


(defclass deepfind_package::imu_data
  :super ros::object
  :slots (_yaw _pitch _roll _acc_x _acc_y _acc_z _gyr_x _gyr_y _gyr_z _mag_x _mag_y _mag_z ))

(defmethod deepfind_package::imu_data
  (:init
   (&key
    ((:yaw __yaw) 0.0)
    ((:pitch __pitch) 0.0)
    ((:roll __roll) 0.0)
    ((:acc_x __acc_x) 0.0)
    ((:acc_y __acc_y) 0.0)
    ((:acc_z __acc_z) 0.0)
    ((:gyr_x __gyr_x) 0.0)
    ((:gyr_y __gyr_y) 0.0)
    ((:gyr_z __gyr_z) 0.0)
    ((:mag_x __mag_x) 0.0)
    ((:mag_y __mag_y) 0.0)
    ((:mag_z __mag_z) 0.0)
    )
   (send-super :init)
   (setq _yaw (float __yaw))
   (setq _pitch (float __pitch))
   (setq _roll (float __roll))
   (setq _acc_x (float __acc_x))
   (setq _acc_y (float __acc_y))
   (setq _acc_z (float __acc_z))
   (setq _gyr_x (float __gyr_x))
   (setq _gyr_y (float __gyr_y))
   (setq _gyr_z (float __gyr_z))
   (setq _mag_x (float __mag_x))
   (setq _mag_y (float __mag_y))
   (setq _mag_z (float __mag_z))
   self)
  (:yaw
   (&optional __yaw)
   (if __yaw (setq _yaw __yaw)) _yaw)
  (:pitch
   (&optional __pitch)
   (if __pitch (setq _pitch __pitch)) _pitch)
  (:roll
   (&optional __roll)
   (if __roll (setq _roll __roll)) _roll)
  (:acc_x
   (&optional __acc_x)
   (if __acc_x (setq _acc_x __acc_x)) _acc_x)
  (:acc_y
   (&optional __acc_y)
   (if __acc_y (setq _acc_y __acc_y)) _acc_y)
  (:acc_z
   (&optional __acc_z)
   (if __acc_z (setq _acc_z __acc_z)) _acc_z)
  (:gyr_x
   (&optional __gyr_x)
   (if __gyr_x (setq _gyr_x __gyr_x)) _gyr_x)
  (:gyr_y
   (&optional __gyr_y)
   (if __gyr_y (setq _gyr_y __gyr_y)) _gyr_y)
  (:gyr_z
   (&optional __gyr_z)
   (if __gyr_z (setq _gyr_z __gyr_z)) _gyr_z)
  (:mag_x
   (&optional __mag_x)
   (if __mag_x (setq _mag_x __mag_x)) _mag_x)
  (:mag_y
   (&optional __mag_y)
   (if __mag_y (setq _mag_y __mag_y)) _mag_y)
  (:mag_z
   (&optional __mag_z)
   (if __mag_z (setq _mag_z __mag_z)) _mag_z)
  (:serialization-length
   ()
   (+
    ;; float64 _yaw
    8
    ;; float64 _pitch
    8
    ;; float64 _roll
    8
    ;; float64 _acc_x
    8
    ;; float64 _acc_y
    8
    ;; float64 _acc_z
    8
    ;; float64 _gyr_x
    8
    ;; float64 _gyr_y
    8
    ;; float64 _gyr_z
    8
    ;; float64 _mag_x
    8
    ;; float64 _mag_y
    8
    ;; float64 _mag_z
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _yaw
       (sys::poke _yaw (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _pitch
       (sys::poke _pitch (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _roll
       (sys::poke _roll (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _acc_x
       (sys::poke _acc_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _acc_y
       (sys::poke _acc_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _acc_z
       (sys::poke _acc_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gyr_x
       (sys::poke _gyr_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gyr_y
       (sys::poke _gyr_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _gyr_z
       (sys::poke _gyr_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _mag_x
       (sys::poke _mag_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _mag_y
       (sys::poke _mag_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _mag_z
       (sys::poke _mag_z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _yaw
     (setq _yaw (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _pitch
     (setq _pitch (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _roll
     (setq _roll (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _acc_x
     (setq _acc_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _acc_y
     (setq _acc_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _acc_z
     (setq _acc_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gyr_x
     (setq _gyr_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gyr_y
     (setq _gyr_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _gyr_z
     (setq _gyr_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _mag_x
     (setq _mag_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _mag_y
     (setq _mag_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _mag_z
     (setq _mag_z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get deepfind_package::imu_data :md5sum-) "df8149b69f061ec41c794db384bb53e8")
(setf (get deepfind_package::imu_data :datatype-) "deepfind_package/imu_data")
(setf (get deepfind_package::imu_data :definition-)
      "float64 yaw
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

")



(provide :deepfind_package/imu_data "df8149b69f061ec41c794db384bb53e8")


