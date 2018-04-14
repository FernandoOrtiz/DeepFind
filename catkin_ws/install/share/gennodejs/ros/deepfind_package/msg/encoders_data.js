// Auto-generated. Do not edit!

// (in-package deepfind_package.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class encoders_data {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.leftMotor = null;
      this.rightMotor = null;
    }
    else {
      if (initObj.hasOwnProperty('leftMotor')) {
        this.leftMotor = initObj.leftMotor
      }
      else {
        this.leftMotor = 0;
      }
      if (initObj.hasOwnProperty('rightMotor')) {
        this.rightMotor = initObj.rightMotor
      }
      else {
        this.rightMotor = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type encoders_data
    // Serialize message field [leftMotor]
    bufferOffset = _serializer.int32(obj.leftMotor, buffer, bufferOffset);
    // Serialize message field [rightMotor]
    bufferOffset = _serializer.int32(obj.rightMotor, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type encoders_data
    let len;
    let data = new encoders_data(null);
    // Deserialize message field [leftMotor]
    data.leftMotor = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [rightMotor]
    data.rightMotor = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'deepfind_package/encoders_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '40c59515e060d941dde4c816f719e5bb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 leftMotor
    int32 rightMotor
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new encoders_data(null);
    if (msg.leftMotor !== undefined) {
      resolved.leftMotor = msg.leftMotor;
    }
    else {
      resolved.leftMotor = 0
    }

    if (msg.rightMotor !== undefined) {
      resolved.rightMotor = msg.rightMotor;
    }
    else {
      resolved.rightMotor = 0
    }

    return resolved;
    }
};

module.exports = encoders_data;
