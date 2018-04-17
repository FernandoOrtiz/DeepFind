#ifndef _ROS_deepfind_package_distance_traveled_h
#define _ROS_deepfind_package_distance_traveled_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace deepfind_package
{

  class distance_traveled : public ros::Msg
  {
    public:
      typedef float _distance_origin_type;
      _distance_origin_type distance_origin;
      typedef float _distance_traveled_type;
      _distance_traveled_type distance_traveled;

    distance_traveled():
      distance_origin(0),
      distance_traveled(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += serializeAvrFloat64(outbuffer + offset, this->distance_origin);
      offset += serializeAvrFloat64(outbuffer + offset, this->distance_traveled);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->distance_origin));
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->distance_traveled));
     return offset;
    }

    const char * getType(){ return "deepfind_package/distance_traveled"; };
    const char * getMD5(){ return "a9e63f456f9ece12564e3132719b476c"; };

  };

}
#endif