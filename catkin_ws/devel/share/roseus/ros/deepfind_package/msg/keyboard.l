;; Auto-generated. Do not edit!


(when (boundp 'deepfind_package::keyboard)
  (if (not (find-package "DEEPFIND_PACKAGE"))
    (make-package "DEEPFIND_PACKAGE"))
  (shadow 'keyboard (find-package "DEEPFIND_PACKAGE")))
(unless (find-package "DEEPFIND_PACKAGE::KEYBOARD")
  (make-package "DEEPFIND_PACKAGE::KEYBOARD"))

(in-package "ROS")
;;//! \htmlinclude keyboard.msg.html


(defclass deepfind_package::keyboard
  :super ros::object
  :slots (_origin _landmark ))

(defmethod deepfind_package::keyboard
  (:init
   (&key
    ((:origin __origin) 0)
    ((:landmark __landmark) 0)
    )
   (send-super :init)
   (setq _origin (round __origin))
   (setq _landmark (round __landmark))
   self)
  (:origin
   (&optional __origin)
   (if __origin (setq _origin __origin)) _origin)
  (:landmark
   (&optional __landmark)
   (if __landmark (setq _landmark __landmark)) _landmark)
  (:serialization-length
   ()
   (+
    ;; int32 _origin
    4
    ;; int32 _landmark
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32 _origin
       (write-long _origin s)
     ;; int32 _landmark
       (write-long _landmark s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32 _origin
     (setq _origin (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _landmark
     (setq _landmark (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get deepfind_package::keyboard :md5sum-) "9c71d7b364a278a1344691df36183a79")
(setf (get deepfind_package::keyboard :datatype-) "deepfind_package/keyboard")
(setf (get deepfind_package::keyboard :definition-)
      "int32 origin
int32 landmark

")



(provide :deepfind_package/keyboard "9c71d7b364a278a1344691df36183a79")


