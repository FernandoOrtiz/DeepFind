; Auto-generated. Do not edit!


(cl:in-package deepfind_package-msg)


;//! \htmlinclude motor_command.msg.html

(cl:defclass <motor_command> (roslisp-msg-protocol:ros-message)
  ((leftMotorPower
    :reader leftMotorPower
    :initarg :leftMotorPower
    :type cl:float
    :initform 0.0)
   (rightMotorPower
    :reader rightMotorPower
    :initarg :rightMotorPower
    :type cl:float
    :initform 0.0)
   (leftMotorDirection
    :reader leftMotorDirection
    :initarg :leftMotorDirection
    :type cl:integer
    :initform 0)
   (rightMotorDirection
    :reader rightMotorDirection
    :initarg :rightMotorDirection
    :type cl:integer
    :initform 0))
)

(cl:defclass motor_command (<motor_command>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <motor_command>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'motor_command)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name deepfind_package-msg:<motor_command> is deprecated: use deepfind_package-msg:motor_command instead.")))

(cl:ensure-generic-function 'leftMotorPower-val :lambda-list '(m))
(cl:defmethod leftMotorPower-val ((m <motor_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_package-msg:leftMotorPower-val is deprecated.  Use deepfind_package-msg:leftMotorPower instead.")
  (leftMotorPower m))

(cl:ensure-generic-function 'rightMotorPower-val :lambda-list '(m))
(cl:defmethod rightMotorPower-val ((m <motor_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_package-msg:rightMotorPower-val is deprecated.  Use deepfind_package-msg:rightMotorPower instead.")
  (rightMotorPower m))

(cl:ensure-generic-function 'leftMotorDirection-val :lambda-list '(m))
(cl:defmethod leftMotorDirection-val ((m <motor_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_package-msg:leftMotorDirection-val is deprecated.  Use deepfind_package-msg:leftMotorDirection instead.")
  (leftMotorDirection m))

(cl:ensure-generic-function 'rightMotorDirection-val :lambda-list '(m))
(cl:defmethod rightMotorDirection-val ((m <motor_command>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_package-msg:rightMotorDirection-val is deprecated.  Use deepfind_package-msg:rightMotorDirection instead.")
  (rightMotorDirection m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <motor_command>) ostream)
  "Serializes a message object of type '<motor_command>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'leftMotorPower))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'rightMotorPower))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let* ((signed (cl:slot-value msg 'leftMotorDirection)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'rightMotorDirection)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <motor_command>) istream)
  "Deserializes a message object of type '<motor_command>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'leftMotorPower) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'rightMotorPower) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'leftMotorDirection) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'rightMotorDirection) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<motor_command>)))
  "Returns string type for a message object of type '<motor_command>"
  "deepfind_package/motor_command")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'motor_command)))
  "Returns string type for a message object of type 'motor_command"
  "deepfind_package/motor_command")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<motor_command>)))
  "Returns md5sum for a message object of type '<motor_command>"
  "1317423ed0a6985045d450b042cb3a95")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'motor_command)))
  "Returns md5sum for a message object of type 'motor_command"
  "1317423ed0a6985045d450b042cb3a95")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<motor_command>)))
  "Returns full string definition for message of type '<motor_command>"
  (cl:format cl:nil "float64 leftMotorPower~%float64 rightMotorPower~%int32 leftMotorDirection~%int32 rightMotorDirection~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'motor_command)))
  "Returns full string definition for message of type 'motor_command"
  (cl:format cl:nil "float64 leftMotorPower~%float64 rightMotorPower~%int32 leftMotorDirection~%int32 rightMotorDirection~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <motor_command>))
  (cl:+ 0
     8
     8
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <motor_command>))
  "Converts a ROS message object to a list"
  (cl:list 'motor_command
    (cl:cons ':leftMotorPower (leftMotorPower msg))
    (cl:cons ':rightMotorPower (rightMotorPower msg))
    (cl:cons ':leftMotorDirection (leftMotorDirection msg))
    (cl:cons ':rightMotorDirection (rightMotorDirection msg))
))
