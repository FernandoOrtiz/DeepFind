;; Auto-generated. Do not edit!


(when (boundp 'deepfind_package::encoders_data)
  (if (not (find-package "DEEPFIND_PACKAGE"))
    (make-package "DEEPFIND_PACKAGE"))
  (shadow 'encoders_data (find-package "DEEPFIND_PACKAGE")))
(unless (find-package "DEEPFIND_PACKAGE::ENCODERS_DATA")
  (make-package "DEEPFIND_PACKAGE::ENCODERS_DATA"))

(in-package "ROS")
;;//! \htmlinclude encoders_data.msg.html


(defclass deepfind_package::encoders_data
  :super ros::object
  :slots (_leftMotor _rightMotor ))

(defmethod deepfind_package::encoders_data
  (:init
   (&key
    ((:leftMotor __leftMotor) 0)
    ((:rightMotor __rightMotor) 0)
    )
   (send-super :init)
   (setq _leftMotor (round __leftMotor))
   (setq _rightMotor (round __rightMotor))
   self)
  (:leftMotor
   (&optional __leftMotor)
   (if __leftMotor (setq _leftMotor __leftMotor)) _leftMotor)
  (:rightMotor
   (&optional __rightMotor)
   (if __rightMotor (setq _rightMotor __rightMotor)) _rightMotor)
  (:serialization-length
   ()
   (+
    ;; int32 _leftMotor
    4
    ;; int32 _rightMotor
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _leftMotor
       (write-long _leftMotor s)
     ;; int32 _rightMotor
       (write-long _rightMotor s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _leftMotor
     (setq _leftMotor (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _rightMotor
     (setq _rightMotor (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get deepfind_package::encoders_data :md5sum-) "40c59515e060d941dde4c816f719e5bb")
(setf (get deepfind_package::encoders_data :datatype-) "deepfind_package/encoders_data")
(setf (get deepfind_package::encoders_data :definition-)
      "int32 leftMotor
int32 rightMotor
")



(provide :deepfind_package/encoders_data "40c59515e060d941dde4c816f719e5bb")


