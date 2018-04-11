; Auto-generated. Do not edit!


(cl:in-package deepfind_package-msg)


;//! \htmlinclude keyboard.msg.html

(cl:defclass <keyboard> (roslisp-msg-protocol:ros-message)
  ((origin
    :reader origin
    :initarg :origin
    :type cl:integer
    :initform 0)
   (landmark
    :reader landmark
    :initarg :landmark
    :type cl:integer
    :initform 0))
)

(cl:defclass keyboard (<keyboard>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <keyboard>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'keyboard)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name deepfind_package-msg:<keyboard> is deprecated: use deepfind_package-msg:keyboard instead.")))

(cl:ensure-generic-function 'origin-val :lambda-list '(m))
(cl:defmethod origin-val ((m <keyboard>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_package-msg:origin-val is deprecated.  Use deepfind_package-msg:origin instead.")
  (origin m))

(cl:ensure-generic-function 'landmark-val :lambda-list '(m))
(cl:defmethod landmark-val ((m <keyboard>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_package-msg:landmark-val is deprecated.  Use deepfind_package-msg:landmark instead.")
  (landmark m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <keyboard>) ostream)
  "Serializes a message object of type '<keyboard>"
  (cl:let* ((signed (cl:slot-value msg 'origin)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
  (cl:let* ((signed (cl:slot-value msg 'landmark)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 4294967296) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <keyboard>) istream)
  "Deserializes a message object of type '<keyboard>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'origin) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'landmark) (cl:if (cl:< unsigned 2147483648) unsigned (cl:- unsigned 4294967296))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<keyboard>)))
  "Returns string type for a message object of type '<keyboard>"
  "deepfind_package/keyboard")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'keyboard)))
  "Returns string type for a message object of type 'keyboard"
  "deepfind_package/keyboard")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<keyboard>)))
  "Returns md5sum for a message object of type '<keyboard>"
  "9c71d7b364a278a1344691df36183a79")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'keyboard)))
  "Returns md5sum for a message object of type 'keyboard"
  "9c71d7b364a278a1344691df36183a79")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<keyboard>)))
  "Returns full string definition for message of type '<keyboard>"
  (cl:format cl:nil "int32 origin~%int32 landmark~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'keyboard)))
  "Returns full string definition for message of type 'keyboard"
  (cl:format cl:nil "int32 origin~%int32 landmark~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <keyboard>))
  (cl:+ 0
     4
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <keyboard>))
  "Converts a ROS message object to a list"
  (cl:list 'keyboard
    (cl:cons ':origin (origin msg))
    (cl:cons ':landmark (landmark msg))
))
