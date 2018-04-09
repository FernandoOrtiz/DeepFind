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
  :slots (_distance_origin _distance_traveled ))

(defmethod deepfind_package::distance_traveled
  (:init
   (&key
    ((:distance_origin __distance_origin) 0.0)
    ((:distance_traveled __distance_traveled) 0.0)
    )
   (send-super :init)
   (setq _distance_origin (float __distance_origin))
   (setq _distance_traveled (float __distance_traveled))
   self)
  (:distance_origin
   (&optional __distance_origin)
   (if __distance_origin (setq _distance_origin __distance_origin)) _distance_origin)
  (:distance_traveled
   (&optional __distance_traveled)
   (if __distance_traveled (setq _distance_traveled __distance_traveled)) _distance_traveled)
  (:serialization-length
   ()
   (+
    ;; float64 _distance_origin
    8
    ;; float64 _distance_traveled
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _distance_origin
       (sys::poke _distance_origin (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _distance_traveled
       (sys::poke _distance_traveled (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _distance_origin
     (setq _distance_origin (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _distance_traveled
     (setq _distance_traveled (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get deepfind_package::distance_traveled :md5sum-) "a9e63f456f9ece12564e3132719b476c")
(setf (get deepfind_package::distance_traveled :datatype-) "deepfind_package/distance_traveled")
(setf (get deepfind_package::distance_traveled :definition-)
      "float64 distance_origin
float64 distance_traveled

")



(provide :deepfind_package/distance_traveled "a9e63f456f9ece12564e3132719b476c")


