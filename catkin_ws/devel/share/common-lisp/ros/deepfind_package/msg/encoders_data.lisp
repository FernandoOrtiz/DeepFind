; Auto-generated. Do not edit!


(cl:in-package deepfind_package-msg)


;//! \htmlinclude encoders_data.msg.html

(cl:defclass <encoders_data> (roslisp-msg-protocol:ros-message)
  ((help
    :reader help
    :initarg :help
    :type cl:string
    :initform ""))
)

(cl:defclass encoders_data (<encoders_data>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <encoders_data>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'encoders_data)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name deepfind_package-msg:<encoders_data> is deprecated: use deepfind_package-msg:encoders_data instead.")))

(cl:ensure-generic-function 'help-val :lambda-list '(m))
(cl:defmethod help-val ((m <encoders_data>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader deepfind_package-msg:help-val is deprecated.  Use deepfind_package-msg:help instead.")
  (help m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <encoders_data>) ostream)
  "Serializes a message object of type '<encoders_data>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'help))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'help))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <encoders_data>) istream)
  "Deserializes a message object of type '<encoders_data>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'help) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'help) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<encoders_data>)))
  "Returns string type for a message object of type '<encoders_data>"
  "deepfind_package/encoders_data")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'encoders_data)))
  "Returns string type for a message object of type 'encoders_data"
  "deepfind_package/encoders_data")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<encoders_data>)))
  "Returns md5sum for a message object of type '<encoders_data>"
  "6ded41f8a691465b353a1de637830f92")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'encoders_data)))
  "Returns md5sum for a message object of type 'encoders_data"
  "6ded41f8a691465b353a1de637830f92")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<encoders_data>)))
  "Returns full string definition for message of type '<encoders_data>"
  (cl:format cl:nil "string help~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'encoders_data)))
  "Returns full string definition for message of type 'encoders_data"
  (cl:format cl:nil "string help~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <encoders_data>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'help))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <encoders_data>))
  "Converts a ROS message object to a list"
  (cl:list 'encoders_data
    (cl:cons ':help (help msg))
))
