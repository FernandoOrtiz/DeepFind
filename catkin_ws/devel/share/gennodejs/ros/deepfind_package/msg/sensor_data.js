// Auto-generated. Do not edit!

// (in-package deepfind_package.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let imu_data = require('./imu_data.js');
let encoders_data = require('./encoders_data.js');
let geometry_msgs = _finder('geometry_msgs');
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------

class sensor_data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.imu = null;
      this.lidar = null;
      this.encoder = null;
      this.pose = null;
    }
    else {
      if (initObj.hasOwnProperty('imu')) {
        this.imu = initObj.imu
      }
      else {
        this.imu = new imu_data();
      }
      if (initObj.hasOwnProperty('lidar')) {
        this.lidar = initObj.lidar
      }
      else {
        this.lidar = new sensor_msgs.msg.LaserScan();
      }
      if (initObj.hasOwnProperty('encoder')) {
        this.encoder = initObj.encoder
      }
      else {
        this.encoder = new encoders_data();
      }
      if (initObj.hasOwnProperty('pose')) {
        this.pose = initObj.pose
      }
      else {
        this.pose = new geometry_msgs.msg.PoseStamped();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type sensor_data
    // Serialize message field [imu]
    bufferOffset = imu_data.serialize(obj.imu, buffer, bufferOffset);
    // Serialize message field [lidar]
    bufferOffset = sensor_msgs.msg.LaserScan.serialize(obj.lidar, buffer, bufferOffset);
    // Serialize message field [encoder]
    bufferOffset = encoders_data.serialize(obj.encoder, buffer, bufferOffset);
    // Serialize message field [pose]
    bufferOffset = geometry_msgs.msg.PoseStamped.serialize(obj.pose, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type sensor_data
    let len;
    let data = new sensor_data(null);
    // Deserialize message field [imu]
    data.imu = imu_data.deserialize(buffer, bufferOffset);
    // Deserialize message field [lidar]
    data.lidar = sensor_msgs.msg.LaserScan.deserialize(buffer, bufferOffset);
    // Deserialize message field [encoder]
    data.encoder = encoders_data.deserialize(buffer, bufferOffset);
    // Deserialize message field [pose]
    data.pose = geometry_msgs.msg.PoseStamped.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += imu_data.getMessageSize(object.imu);
    length += sensor_msgs.msg.LaserScan.getMessageSize(object.lidar);
    length += geometry_msgs.msg.PoseStamped.getMessageSize(object.pose);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'deepfind_package/sensor_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd889fddaeeb05675262e5f8a70744d81';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    imu_data imu
    sensor_msgs/LaserScan lidar
    encoders_data encoder
    geometry_msgs/PoseStamped pose
    
    ================================================================================
    MSG: deepfind_package/imu_data
    Header header
    float64 yaw
    float64 pitch 
    float64 roll
    float64 acc_x
    float64 acc_y
    float64 acc_z
    float64 gyr_x
    float64 gyr_y
    float64 gyr_z
    float64 mag_x
    float64 mag_y
    float64 mag_z
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    ================================================================================
    MSG: sensor_msgs/LaserScan
    # Single scan from a planar laser range-finder
    #
    # If you have another ranging device with different behavior (e.g. a sonar
    # array), please find or create a different message, since applications
    # will make fairly laser-specific assumptions about this data
    
    Header header            # timestamp in the header is the acquisition time of 
                             # the first ray in the scan.
                             #
                             # in frame frame_id, angles are measured around 
                             # the positive Z axis (counterclockwise, if Z is up)
                             # with zero angle being forward along the x axis
                             
    float32 angle_min        # start angle of the scan [rad]
    float32 angle_max        # end angle of the scan [rad]
    float32 angle_increment  # angular distance between measurements [rad]
    
    float32 time_increment   # time between measurements [seconds] - if your scanner
                             # is moving, this will be used in interpolating position
                             # of 3d points
    float32 scan_time        # time between scans [seconds]
    
    float32 range_min        # minimum range value [m]
    float32 range_max        # maximum range value [m]
    
    float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)
    float32[] intensities    # intensity data [device-specific units].  If your
                             # device does not provide intensities, please leave
                             # the array empty.
    
    ================================================================================
    MSG: deepfind_package/encoders_data
    int32 leftMotor
    int32 rightMotor
    ================================================================================
    MSG: geometry_msgs/PoseStamped
    # A Pose with reference coordinate frame and timestamp
    Header header
    Pose pose
    
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new sensor_data(null);
    if (msg.imu !== undefined) {
      resolved.imu = imu_data.Resolve(msg.imu)
    }
    else {
      resolved.imu = new imu_data()
    }

    if (msg.lidar !== undefined) {
      resolved.lidar = sensor_msgs.msg.LaserScan.Resolve(msg.lidar)
    }
    else {
      resolved.lidar = new sensor_msgs.msg.LaserScan()
    }

    if (msg.encoder !== undefined) {
      resolved.encoder = encoders_data.Resolve(msg.encoder)
    }
    else {
      resolved.encoder = new encoders_data()
    }

    if (msg.pose !== undefined) {
      resolved.pose = geometry_msgs.msg.PoseStamped.Resolve(msg.pose)
    }
    else {
      resolved.pose = new geometry_msgs.msg.PoseStamped()
    }

    return resolved;
    }
};

module.exports = sensor_data;
