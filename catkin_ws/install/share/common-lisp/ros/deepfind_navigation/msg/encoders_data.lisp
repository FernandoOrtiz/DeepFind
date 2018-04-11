; Auto-generated. Do not edit!


(cl:in-package deepfind_navigation-msg)


;//! \htmlinclude encoders_data.msg.html

(cl:defclass <encoders_data> (roslisp-msg-protocol:ros-message)
  ((leftMotor
    :reader leftMotor
    :initarg :leftMotor
    :type cl:integer
    :initform 0)
   (rightMotor
    :reader rightMotor
    :initarg :rightMotor
    :type cl:integer
    :initform 0))
)

(cl:defclass encoders_data (<encoders_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <encoders_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'encoders_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name deepfind_navigation-msg:<encoders_data> is deprecated: use deepfind_navigation-msg:encoders_data instead.")))

(cl:ensure-generic-function 'leftMotor-val :lambda-list '(m))
(cl:defmethod leftMotor-val ((m <encoders_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_navigation-msg:leftMotor-val is deprecated.  Use deepfind_navigation-msg:leftMotor instead.")
  (leftMotor m))

(cl:ensure-generic-function 'rightMotor-val :lambda-list '(m))
(cl:defmethod rightMotor-val ((m <encoders_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_navigation-msg:rightMotor-val is deprecated.  Use deepfind_navigation-msg:rightMotor instead.")
  (rightMotor m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <encoders_data>) ostream)
  "Serializes a message object of type '<encoders_data>"
  (cl:let* ((signed (cl:slot-value msg 'leftMotor)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'rightMotor)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <encoders_data>) istream)
  "Deserializes a message object of type '<encoders_data>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'leftMotor) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rightMotor) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<encoders_data>)))
  "Returns string type for a message object of type '<encoders_data>"
  "deepfind_navigation/encoders_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'encoders_data)))
  "Returns string type for a message object of type 'encoders_data"
  "deepfind_navigation/encoders_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<encoders_data>)))
  "Returns md5sum for a message object of type '<encoders_data>"
  "40c59515e060d941dde4c816f719e5bb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'encoders_data)))
  "Returns md5sum for a message object of type 'encoders_data"
  "40c59515e060d941dde4c816f719e5bb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<encoders_data>)))
  "Returns full string definition for message of type '<encoders_data>"
  (cl:format cl:nil "int32 leftMotor~%int32 rightMotor~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'encoders_data)))
  "Returns full string definition for message of type 'encoders_data"
  (cl:format cl:nil "int32 leftMotor~%int32 rightMotor~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <encoders_data>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <encoders_data>))
  "Converts a ROS message object to a list"
  (cl:list 'encoders_data
    (cl:cons ':leftMotor (leftMotor msg))
    (cl:cons ':rightMotor (rightMotor msg))
))
