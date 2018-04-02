// Auto-generated. Do not edit!

// (in-package deepfind_package.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let encoders_data = require('./encoders_data.js');
let sensor_msgs = _finder('sensor_msgs');

//-----------------------------------------------------------

class sensor_data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.imu = null;
      this.lidar = null;
      this.encoder = null;
    }
    else {
      if (initObj.hasOwnProperty('imu')) {
        this.imu = initObj.imu
      }
      else {
        this.imu = new sensor_msgs.msg.Imu();
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
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type sensor_data
    // Serialize message field [imu]
    bufferOffset = sensor_msgs.msg.Imu.serialize(obj.imu, buffer, bufferOffset);
    // Serialize message field [lidar]
    bufferOffset = sensor_msgs.msg.LaserScan.serialize(obj.lidar, buffer, bufferOffset);
    // Serialize message field [encoder]
    bufferOffset = encoders_data.serialize(obj.encoder, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type sensor_data
    let len;
    let data = new sensor_data(null);
    // Deserialize message field [imu]
    data.imu = sensor_msgs.msg.Imu.deserialize(buffer, bufferOffset);
    // Deserialize message field [lidar]
    data.lidar = sensor_msgs.msg.LaserScan.deserialize(buffer, bufferOffset);
    // Deserialize message field [encoder]
    data.encoder = encoders_data.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += sensor_msgs.msg.Imu.getMessageSize(object.imu);
    length += sensor_msgs.msg.LaserScan.getMessageSize(object.lidar);
    return length + 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'deepfind_package/sensor_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '4263fc74ca2818109dbcf4431d9c193b';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    sensor_msgs/Imu imu
    sensor_msgs/LaserScan lidar
    encoders_data encoder
    
    ================================================================================
    MSG: sensor_msgs/Imu
    # This is a message to hold data from an IMU (Inertial Measurement Unit)
    #
    # Accelerations should be in m/s^2 (not in g's), and rotational velocity should be in rad/sec
    #
    # If the covariance of the measurement is known, it should be filled in (if all you know is the 
    # variance of each measurement, e.g. from the datasheet, just put those along the diagonal)
    # A covariance matrix of all zeros will be interpreted as "covariance unknown", and to use the
    # data a covariance will have to be assumed or gotten from some other source
    #
    # If you have no estimate for one of the data elements (e.g. your IMU doesn't produce an orientation 
    # estimate), please set element 0 of the associated covariance matrix to -1
    # If you are interpreting this message, please check for a value of -1 in the first element of each 
    # covariance matrix, and disregard the associated estimate.
    
    Header header
    
    geometry_msgs/Quaternion orientation
    float64[9] orientation_covariance # Row major about x, y, z axes
    
    geometry_msgs/Vector3 angular_velocity
    float64[9] angular_velocity_covariance # Row major about x, y, z axes
    
    geometry_msgs/Vector3 linear_acceleration
    float64[9] linear_acceleration_covariance # Row major x, y z 
    
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
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
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
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new sensor_data(null);
    if (msg.imu !== undefined) {
      resolved.imu = sensor_msgs.msg.Imu.Resolve(msg.imu)
    }
    else {
      resolved.imu = new sensor_msgs.msg.Imu()
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

    return resolved;
    }
};

module.exports = sensor_data;
