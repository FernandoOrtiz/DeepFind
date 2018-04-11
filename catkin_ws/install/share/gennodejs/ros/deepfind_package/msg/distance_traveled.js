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

class distance_traveled {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.distance_origin = null;
      this.distance_traveled = null;
    }
    else {
      if (initObj.hasOwnProperty('distance_origin')) {
        this.distance_origin = initObj.distance_origin
      }
      else {
        this.distance_origin = 0.0;
      }
      if (initObj.hasOwnProperty('distance_traveled')) {
        this.distance_traveled = initObj.distance_traveled
      }
      else {
        this.distance_traveled = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type distance_traveled
    // Serialize message field [distance_origin]
    bufferOffset = _serializer.float64(obj.distance_origin, buffer, bufferOffset);
    // Serialize message field [distance_traveled]
    bufferOffset = _serializer.float64(obj.distance_traveled, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type distance_traveled
    let len;
    let data = new distance_traveled(null);
    // Deserialize message field [distance_origin]
    data.distance_origin = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [distance_traveled]
    data.distance_traveled = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'deepfind_package/distance_traveled';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'a9e63f456f9ece12564e3132719b476c';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 distance_origin
    float64 distance_traveled
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new distance_traveled(null);
    if (msg.distance_origin !== undefined) {
      resolved.distance_origin = msg.distance_origin;
    }
    else {
      resolved.distance_origin = 0.0
    }

    if (msg.distance_traveled !== undefined) {
      resolved.distance_traveled = msg.distance_traveled;
    }
    else {
      resolved.distance_traveled = 0.0
    }

    return resolved;
    }
};

module.exports = distance_traveled;
