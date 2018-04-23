; Auto-generated. Do not edit!


(cl:in-package deepfind_package-msg)


;//! \htmlinclude distance_traveled.msg.html

(cl:defclass <distance_traveled> (roslisp-msg-protocol:ros-message)
  ((absolute_origin
    :reader absolute_origin
    :initarg :absolute_origin
    :type cl:float
    :initform 0.0)
   (absolute_landmark
    :reader absolute_landmark
    :initarg :absolute_landmark
    :type cl:float
    :initform 0.0))
)

(cl:defclass distance_traveled (<distance_traveled>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <distance_traveled>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'distance_traveled)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name deepfind_package-msg:<distance_traveled> is deprecated: use deepfind_package-msg:distance_traveled instead.")))

(cl:ensure-generic-function 'absolute_origin-val :lambda-list '(m))
(cl:defmethod absolute_origin-val ((m <distance_traveled>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_package-msg:absolute_origin-val is deprecated.  Use deepfind_package-msg:absolute_origin instead.")
  (absolute_origin m))

(cl:ensure-generic-function 'absolute_landmark-val :lambda-list '(m))
(cl:defmethod absolute_landmark-val ((m <distance_traveled>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_package-msg:absolute_landmark-val is deprecated.  Use deepfind_package-msg:absolute_landmark instead.")
  (absolute_landmark m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <distance_traveled>) ostream)
  "Serializes a message object of type '<distance_traveled>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'absolute_origin))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'absolute_landmark))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <distance_traveled>) istream)
  "Deserializes a message object of type '<distance_traveled>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'absolute_origin) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'absolute_landmark) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<distance_traveled>)))
  "Returns string type for a message object of type '<distance_traveled>"
  "deepfind_package/distance_traveled")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'distance_traveled)))
  "Returns string type for a message object of type 'distance_traveled"
  "deepfind_package/distance_traveled")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<distance_traveled>)))
  "Returns md5sum for a message object of type '<distance_traveled>"
  "2090cb8db4678ff5744ff25e1aeb8f66")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'distance_traveled)))
  "Returns md5sum for a message object of type 'distance_traveled"
  "2090cb8db4678ff5744ff25e1aeb8f66")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<distance_traveled>)))
  "Returns full string definition for message of type '<distance_traveled>"
  (cl:format cl:nil "float64 absolute_origin~%float64 absolute_landmark~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'distance_traveled)))
  "Returns full string definition for message of type 'distance_traveled"
  (cl:format cl:nil "float64 absolute_origin~%float64 absolute_landmark~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <distance_traveled>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <distance_traveled>))
  "Converts a ROS message object to a list"
  (cl:list 'distance_traveled
    (cl:cons ':absolute_origin (absolute_origin msg))
    (cl:cons ':absolute_landmark (absolute_landmark msg))
))
