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
  :slots (_help ))

(defmethod deepfind_package::encoders_data
  (:init
   (&key
    ((:help __help) "")
    )
   (send-super :init)
   (setq _help (string __help))
   self)
  (:help
   (&optional __help)
   (if __help (setq _help __help)) _help)
  (:serialization-length
   ()
   (+
    ;; string _help
    4 (length _help)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _help
       (write-long (length _help) s) (princ _help s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _help
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _help (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get deepfind_package::encoders_data :md5sum-) "6ded41f8a691465b353a1de637830f92")
(setf (get deepfind_package::encoders_data :datatype-) "deepfind_package/encoders_data")
(setf (get deepfind_package::encoders_data :definition-)
      "string help

")



(provide :deepfind_package/encoders_data "6ded41f8a691465b353a1de637830f92")


