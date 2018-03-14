// Auto-generated. Do not edit!

// (in-package deepfind_package.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class imu_data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.yaw = null;
      this.pitch = null;
      this.roll = null;
      this.acc_x = null;
      this.acc_y = null;
      this.acc_z = null;
      this.gyr_x = null;
      this.gyr_y = null;
      this.gyr_z = null;
      this.mag_x = null;
      this.mag_y = null;
      this.mag_z = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('yaw')) {
        this.yaw = initObj.yaw
      }
      else {
        this.yaw = 0.0;
      }
      if (initObj.hasOwnProperty('pitch')) {
        this.pitch = initObj.pitch
      }
      else {
        this.pitch = 0.0;
      }
      if (initObj.hasOwnProperty('roll')) {
        this.roll = initObj.roll
      }
      else {
        this.roll = 0.0;
      }
      if (initObj.hasOwnProperty('acc_x')) {
        this.acc_x = initObj.acc_x
      }
      else {
        this.acc_x = 0.0;
      }
      if (initObj.hasOwnProperty('acc_y')) {
        this.acc_y = initObj.acc_y
      }
      else {
        this.acc_y = 0.0;
      }
      if (initObj.hasOwnProperty('acc_z')) {
        this.acc_z = initObj.acc_z
      }
      else {
        this.acc_z = 0.0;
      }
      if (initObj.hasOwnProperty('gyr_x')) {
        this.gyr_x = initObj.gyr_x
      }
      else {
        this.gyr_x = 0.0;
      }
      if (initObj.hasOwnProperty('gyr_y')) {
        this.gyr_y = initObj.gyr_y
      }
      else {
        this.gyr_y = 0.0;
      }
      if (initObj.hasOwnProperty('gyr_z')) {
        this.gyr_z = initObj.gyr_z
      }
      else {
        this.gyr_z = 0.0;
      }
      if (initObj.hasOwnProperty('mag_x')) {
        this.mag_x = initObj.mag_x
      }
      else {
        this.mag_x = 0.0;
      }
      if (initObj.hasOwnProperty('mag_y')) {
        this.mag_y = initObj.mag_y
      }
      else {
        this.mag_y = 0.0;
      }
      if (initObj.hasOwnProperty('mag_z')) {
        this.mag_z = initObj.mag_z
      }
      else {
        this.mag_z = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type imu_data
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [yaw]
    bufferOffset = _serializer.float64(obj.yaw, buffer, bufferOffset);
    // Serialize message field [pitch]
    bufferOffset = _serializer.float64(obj.pitch, buffer, bufferOffset);
    // Serialize message field [roll]
    bufferOffset = _serializer.float64(obj.roll, buffer, bufferOffset);
    // Serialize message field [acc_x]
    bufferOffset = _serializer.float64(obj.acc_x, buffer, bufferOffset);
    // Serialize message field [acc_y]
    bufferOffset = _serializer.float64(obj.acc_y, buffer, bufferOffset);
    // Serialize message field [acc_z]
    bufferOffset = _serializer.float64(obj.acc_z, buffer, bufferOffset);
    // Serialize message field [gyr_x]
    bufferOffset = _serializer.float64(obj.gyr_x, buffer, bufferOffset);
    // Serialize message field [gyr_y]
    bufferOffset = _serializer.float64(obj.gyr_y, buffer, bufferOffset);
    // Serialize message field [gyr_z]
    bufferOffset = _serializer.float64(obj.gyr_z, buffer, bufferOffset);
    // Serialize message field [mag_x]
    bufferOffset = _serializer.float64(obj.mag_x, buffer, bufferOffset);
    // Serialize message field [mag_y]
    bufferOffset = _serializer.float64(obj.mag_y, buffer, bufferOffset);
    // Serialize message field [mag_z]
    bufferOffset = _serializer.float64(obj.mag_z, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type imu_data
    let len;
    let data = new imu_data(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [yaw]
    data.yaw = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [pitch]
    data.pitch = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [roll]
    data.roll = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [acc_x]
    data.acc_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [acc_y]
    data.acc_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [acc_z]
    data.acc_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [gyr_x]
    data.gyr_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [gyr_y]
    data.gyr_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [gyr_z]
    data.gyr_z = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [mag_x]
    data.mag_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [mag_y]
    data.mag_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [mag_z]
    data.mag_z = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 96;
  }

  static datatype() {
    // Returns string type for a message object
    return 'deepfind_package/imu_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5781ee5294affb6dd3e062f6edb954b1';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new imu_data(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.yaw !== undefined) {
      resolved.yaw = msg.yaw;
    }
    else {
      resolved.yaw = 0.0
    }

    if (msg.pitch !== undefined) {
      resolved.pitch = msg.pitch;
    }
    else {
      resolved.pitch = 0.0
    }

    if (msg.roll !== undefined) {
      resolved.roll = msg.roll;
    }
    else {
      resolved.roll = 0.0
    }

    if (msg.acc_x !== undefined) {
      resolved.acc_x = msg.acc_x;
    }
    else {
      resolved.acc_x = 0.0
    }

    if (msg.acc_y !== undefined) {
      resolved.acc_y = msg.acc_y;
    }
    else {
      resolved.acc_y = 0.0
    }

    if (msg.acc_z !== undefined) {
      resolved.acc_z = msg.acc_z;
    }
    else {
      resolved.acc_z = 0.0
    }

    if (msg.gyr_x !== undefined) {
      resolved.gyr_x = msg.gyr_x;
    }
    else {
      resolved.gyr_x = 0.0
    }

    if (msg.gyr_y !== undefined) {
      resolved.gyr_y = msg.gyr_y;
    }
    else {
      resolved.gyr_y = 0.0
    }

    if (msg.gyr_z !== undefined) {
      resolved.gyr_z = msg.gyr_z;
    }
    else {
      resolved.gyr_z = 0.0
    }

    if (msg.mag_x !== undefined) {
      resolved.mag_x = msg.mag_x;
    }
    else {
      resolved.mag_x = 0.0
    }

    if (msg.mag_y !== undefined) {
      resolved.mag_y = msg.mag_y;
    }
    else {
      resolved.mag_y = 0.0
    }

    if (msg.mag_z !== undefined) {
      resolved.mag_z = msg.mag_z;
    }
    else {
      resolved.mag_z = 0.0
    }

    return resolved;
    }
};

module.exports = imu_data;
