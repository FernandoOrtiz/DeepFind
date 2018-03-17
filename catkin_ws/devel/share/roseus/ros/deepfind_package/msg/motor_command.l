;; Auto-generated. Do not edit!


(when (boundp 'deepfind_package::motor_command)
  (if (not (find-package "DEEPFIND_PACKAGE"))
    (make-package "DEEPFIND_PACKAGE"))
  (shadow 'motor_command (find-package "DEEPFIND_PACKAGE")))
(unless (find-package "DEEPFIND_PACKAGE::MOTOR_COMMAND")
  (make-package "DEEPFIND_PACKAGE::MOTOR_COMMAND"))

(in-package "ROS")
;;//! \htmlinclude motor_command.msg.html


(defclass deepfind_package::motor_command
  :super ros::object
  :slots (_leftMotorPower _rightMotorPower _leftMotorDirection _rightMotorDirection ))

(defmethod deepfind_package::motor_command
  (:init
   (&key
    ((:leftMotorPower __leftMotorPower) 0.0)
    ((:rightMotorPower __rightMotorPower) 0.0)
    ((:leftMotorDirection __leftMotorDirection) 0)
    ((:rightMotorDirection __rightMotorDirection) 0)
    )
   (send-super :init)
   (setq _leftMotorPower (float __leftMotorPower))
   (setq _rightMotorPower (float __rightMotorPower))
   (setq _leftMotorDirection (round __leftMotorDirection))
   (setq _rightMotorDirection (round __rightMotorDirection))
   self)
  (:leftMotorPower
   (&optional __leftMotorPower)
   (if __leftMotorPower (setq _leftMotorPower __leftMotorPower)) _leftMotorPower)
  (:rightMotorPower
   (&optional __rightMotorPower)
   (if __rightMotorPower (setq _rightMotorPower __rightMotorPower)) _rightMotorPower)
  (:leftMotorDirection
   (&optional __leftMotorDirection)
   (if __leftMotorDirection (setq _leftMotorDirection __leftMotorDirection)) _leftMotorDirection)
  (:rightMotorDirection
   (&optional __rightMotorDirection)
   (if __rightMotorDirection (setq _rightMotorDirection __rightMotorDirection)) _rightMotorDirection)
  (:serialization-length
   ()
   (+
    ;; float64 _leftMotorPower
    8
    ;; float64 _rightMotorPower
    8
    ;; int32 _leftMotorDirection
    4
    ;; int32 _rightMotorDirection
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _leftMotorPower
       (sys::poke _leftMotorPower (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _rightMotorPower
       (sys::poke _rightMotorPower (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; int32 _leftMotorDirection
       (write-long _leftMotorDirection s)
     ;; int32 _rightMotorDirection
       (write-long _rightMotorDirection s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _leftMotorPower
     (setq _leftMotorPower (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _rightMotorPower
     (setq _rightMotorPower (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; int32 _leftMotorDirection
     (setq _leftMotorDirection (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _rightMotorDirection
     (setq _rightMotorDirection (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get deepfind_package::motor_command :md5sum-) "1317423ed0a6985045d450b042cb3a95")
(setf (get deepfind_package::motor_command :datatype-) "deepfind_package/motor_command")
(setf (get deepfind_package::motor_command :definition-)
      "float64 leftMotorPower
float64 rightMotorPower
int32 leftMotorDirection
int32 rightMotorDirection

")



(provide :deepfind_package/motor_command "1317423ed0a6985045d450b042cb3a95")


