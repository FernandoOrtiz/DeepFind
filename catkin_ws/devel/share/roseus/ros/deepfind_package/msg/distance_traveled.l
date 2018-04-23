;; Auto-generated. Do not edit!


(when (boundp 'deepfind_package::distance_traveled)
  (if (not (find-package "DEEPFIND_PACKAGE"))
    (make-package "DEEPFIND_PACKAGE"))
  (shadow 'distance_traveled (find-package "DEEPFIND_PACKAGE")))
(unless (find-package "DEEPFIND_PACKAGE::DISTANCE_TRAVELED")
  (make-package "DEEPFIND_PACKAGE::DISTANCE_TRAVELED"))

(in-package "ROS")
;;//! \htmlinclude distance_traveled.msg.html


(defclass deepfind_package::distance_traveled
  :super ros::object
  :slots (_absolute_origin _absolute_landmark ))

(defmethod deepfind_package::distance_traveled
  (:init
   (&key
    ((:absolute_origin __absolute_origin) 0.0)
    ((:absolute_landmark __absolute_landmark) 0.0)
    )
   (send-super :init)
   (setq _absolute_origin (float __absolute_origin))
   (setq _absolute_landmark (float __absolute_landmark))
   self)
  (:absolute_origin
   (&optional __absolute_origin)
   (if __absolute_origin (setq _absolute_origin __absolute_origin)) _absolute_origin)
  (:absolute_landmark
   (&optional __absolute_landmark)
   (if __absolute_landmark (setq _absolute_landmark __absolute_landmark)) _absolute_landmark)
  (:serialization-length
   ()
   (+
    ;; float64 _absolute_origin
    8
    ;; float64 _absolute_landmark
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _absolute_origin
       (sys::poke _absolute_origin (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _absolute_landmark
       (sys::poke _absolute_landmark (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _absolute_origin
     (setq _absolute_origin (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _absolute_landmark
     (setq _absolute_landmark (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get deepfind_package::distance_traveled :md5sum-) "2090cb8db4678ff5744ff25e1aeb8f66")
(setf (get deepfind_package::distance_traveled :datatype-) "deepfind_package/distance_traveled")
(setf (get deepfind_package::distance_traveled :definition-)
      "float64 absolute_origin
float64 absolute_landmark

")



(provide :deepfind_package/distance_traveled "2090cb8db4678ff5744ff25e1aeb8f66")


