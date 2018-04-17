#ifndef _ROS_deepfind_package_encoders_data_h
#define _ROS_deepfind_package_encoders_data_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace deepfind_package
{

  class encoders_data : public ros::Msg
  {
    public:
      typedef int32_t _leftMotor_type;
      _leftMotor_type leftMotor;
      typedef int32_t _rightMotor_type;
      _rightMotor_type rightMotor;
      uint32_t speed_length;
      typedef float _speed_type;
      _speed_type st_speed;
      _speed_type * speed;

    encoders_data():
      leftMotor(0),
      rightMotor(0),
      speed_length(0), speed(NULL)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_leftMotor;
      u_leftMotor.real = this->leftMotor;
      *(outbuffer + offset + 0) = (u_leftMotor.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_leftMotor.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_leftMotor.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_leftMotor.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->leftMotor);
      union {
        int32_t real;
        uint32_t base;
      } u_rightMotor;
      u_rightMotor.real = this->rightMotor;
      *(outbuffer + offset + 0) = (u_rightMotor.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_rightMotor.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_rightMotor.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_rightMotor.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->rightMotor);
      *(outbuffer + offset + 0) = (this->speed_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->speed_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->speed_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->speed_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->speed_length);
      for( uint32_t i = 0; i < speed_length; i++){
      offset += serializeAvrFloat64(outbuffer + offset, this->speed[i]);
      }
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_leftMotor;
      u_leftMotor.base = 0;
      u_leftMotor.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_leftMotor.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_leftMotor.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_leftMotor.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->leftMotor = u_leftMotor.real;
      offset += sizeof(this->leftMotor);
      union {
        int32_t real;
        uint32_t base;
      } u_rightMotor;
      u_rightMotor.base = 0;
      u_rightMotor.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_rightMotor.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_rightMotor.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_rightMotor.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->rightMotor = u_rightMotor.real;
      offset += sizeof(this->rightMotor);
      uint32_t speed_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      speed_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      speed_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      speed_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->speed_length);
      if(speed_lengthT > speed_length)
        this->speed = (float*)realloc(this->speed, speed_lengthT * sizeof(float));
      speed_length = speed_lengthT;
      for( uint32_t i = 0; i < speed_length; i++){
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->st_speed));
        memcpy( &(this->speed[i]), &(this->st_speed), sizeof(float));
      }
     return offset;
    }

    const char * getType(){ return "deepfind_package/encoders_data"; };
    const char * getMD5(){ return "2bf9ef0a1e520aaacbce835a92460e99"; };

  };

}
#endif