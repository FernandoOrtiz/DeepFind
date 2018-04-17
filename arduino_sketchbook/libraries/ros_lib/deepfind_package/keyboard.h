#ifndef _ROS_deepfind_package_keyboard_h
#define _ROS_deepfind_package_keyboard_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace deepfind_package
{

  class keyboard : public ros::Msg
  {
    public:
      typedef int32_t _origin_type;
      _origin_type origin;
      typedef int32_t _landmark_type;
      _landmark_type landmark;

    keyboard():
      origin(0),
      landmark(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_origin;
      u_origin.real = this->origin;
      *(outbuffer + offset + 0) = (u_origin.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_origin.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_origin.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_origin.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->origin);
      union {
        int32_t real;
        uint32_t base;
      } u_landmark;
      u_landmark.real = this->landmark;
      *(outbuffer + offset + 0) = (u_landmark.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_landmark.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_landmark.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_landmark.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->landmark);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_origin;
      u_origin.base = 0;
      u_origin.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_origin.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_origin.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_origin.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->origin = u_origin.real;
      offset += sizeof(this->origin);
      union {
        int32_t real;
        uint32_t base;
      } u_landmark;
      u_landmark.base = 0;
      u_landmark.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_landmark.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_landmark.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_landmark.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->landmark = u_landmark.real;
      offset += sizeof(this->landmark);
     return offset;
    }

    const char * getType(){ return "deepfind_package/keyboard"; };
    const char * getMD5(){ return "9c71d7b364a278a1344691df36183a79"; };

  };

}
#endif