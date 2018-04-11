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

class keyboard {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.origin = null;
      this.landmark = null;
    }
    else {
      if (initObj.hasOwnProperty('origin')) {
        this.origin = initObj.origin
      }
      else {
        this.origin = 0;
      }
      if (initObj.hasOwnProperty('landmark')) {
        this.landmark = initObj.landmark
      }
      else {
        this.landmark = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type keyboard
    // Serialize message field [origin]
    bufferOffset = _serializer.int32(obj.origin, buffer, bufferOffset);
    // Serialize message field [landmark]
    bufferOffset = _serializer.int32(obj.landmark, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type keyboard
    let len;
    let data = new keyboard(null);
    // Deserialize message field [origin]
    data.origin = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [landmark]
    data.landmark = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a message object
    return 'deepfind_package/keyboard';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '9c71d7b364a278a1344691df36183a79';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int32 origin
    int32 landmark
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new keyboard(null);
    if (msg.origin !== undefined) {
      resolved.origin = msg.origin;
    }
    else {
      resolved.origin = 0
    }

    if (msg.landmark !== undefined) {
      resolved.landmark = msg.landmark;
    }
    else {
      resolved.landmark = 0
    }

    return resolved;
    }
};

module.exports = keyboard;
