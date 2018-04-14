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

class motor_command {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.leftMotorPower = null;
      this.rightMotorPower = null;
      this.leftMotorDirection = null;
      this.rightMotorDirection = null;
    }
    else {
      if (initObj.hasOwnProperty('leftMotorPower')) {
        this.leftMotorPower = initObj.leftMotorPower
      }
      else {
        this.leftMotorPower = 0;
      }
      if (initObj.hasOwnProperty('rightMotorPower')) {
        this.rightMotorPower = initObj.rightMotorPower
      }
      else {
        this.rightMotorPower = 0;
      }
      if (initObj.hasOwnProperty('leftMotorDirection')) {
        this.leftMotorDirection = initObj.leftMotorDirection
      }
      else {
        this.leftMotorDirection = 0;
      }
      if (initObj.hasOwnProperty('rightMotorDirection')) {
        this.rightMotorDirection = initObj.rightMotorDirection
      }
      else {
        this.rightMotorDirection = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type motor_command
    // Serialize message field [leftMotorPower]
    bufferOffset = _serializer.int32(obj.leftMotorPower, buffer, bufferOffset);
    // Serialize message field [rightMotorPower]
    bufferOffset = _serializer.int32(obj.rightMotorPower, buffer, bufferOffset);
    // Serialize message field [leftMotorDirection]
    bufferOffset = _serializer.int32(obj.leftMotorDirection, buffer, bufferOffset);
    // Serialize message field [rightMotorDirection]
    bufferOffset = _serializer.int32(obj.rightMotorDirection, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type motor_command
    let len;
    let data = new motor_command(null);
    // Deserialize message field [leftMotorPower]
    data.leftMotorPower = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [rightMotorPower]
    data.rightMotorPower = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [leftMotorDirection]
    data.leftMotorDirection = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [rightMotorDirection]
    data.rightMotorDirection = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'deepfind_package/motor_command';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '382ef61c60c451a76309a7978532675c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 leftMotorPower
    int32 rightMotorPower
    int32 leftMotorDirection
    int32 rightMotorDirection
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new motor_command(null);
    if (msg.leftMotorPower !== undefined) {
      resolved.leftMotorPower = msg.leftMotorPower;
    }
    else {
      resolved.leftMotorPower = 0
    }

    if (msg.rightMotorPower !== undefined) {
      resolved.rightMotorPower = msg.rightMotorPower;
    }
    else {
      resolved.rightMotorPower = 0
    }

    if (msg.leftMotorDirection !== undefined) {
      resolved.leftMotorDirection = msg.leftMotorDirection;
    }
    else {
      resolved.leftMotorDirection = 0
    }

    if (msg.rightMotorDirection !== undefined) {
      resolved.rightMotorDirection = msg.rightMotorDirection;
    }
    else {
      resolved.rightMotorDirection = 0
    }

    return resolved;
    }
};

module.exports = motor_command;
