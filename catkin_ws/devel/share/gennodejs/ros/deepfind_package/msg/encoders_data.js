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
      this.help = null;
    }
    else {
      if (initObj.hasOwnProperty('help')) {
        this.help = initObj.help
      }
      else {
        this.help = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type encoders_data
    // Serialize message field [help]
    bufferOffset = _serializer.string(obj.help, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type encoders_data
    let len;
    let data = new encoders_data(null);
    // Deserialize message field [help]
    data.help = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.help.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'deepfind_package/encoders_data';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '6ded41f8a691465b353a1de637830f92';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string help
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new encoders_data(null);
    if (msg.help !== undefined) {
      resolved.help = msg.help;
    }
    else {
      resolved.help = ''
    }

    return resolved;
    }
};

module.exports = encoders_data;
