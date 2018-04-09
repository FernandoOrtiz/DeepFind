// Generated by gencpp from file deepfind_package/sensor_data.msg
// DO NOT EDIT!


#ifndef DEEPFIND_PACKAGE_MESSAGE_SENSOR_DATA_H
#define DEEPFIND_PACKAGE_MESSAGE_SENSOR_DATA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <deepfind_package/imu_data.h>
#include <sensor_msgs/LaserScan.h>
#include <deepfind_package/encoders_data.h>

namespace deepfind_package
{
template <class ContainerAllocator>
struct sensor_data_
{
  typedef sensor_data_<ContainerAllocator> Type;

  sensor_data_()
    : imu()
    , lidar()
    , encoder()  {
    }
  sensor_data_(const ContainerAllocator& _alloc)
    : imu(_alloc)
    , lidar(_alloc)
    , encoder(_alloc)  {
  (void)_alloc;
    }



   typedef  ::deepfind_package::imu_data_<ContainerAllocator>  _imu_type;
  _imu_type imu;

   typedef  ::sensor_msgs::LaserScan_<ContainerAllocator>  _lidar_type;
  _lidar_type lidar;

   typedef  ::deepfind_package::encoders_data_<ContainerAllocator>  _encoder_type;
  _encoder_type encoder;





  typedef boost::shared_ptr< ::deepfind_package::sensor_data_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::deepfind_package::sensor_data_<ContainerAllocator> const> ConstPtr;

}; // struct sensor_data_

typedef ::deepfind_package::sensor_data_<std::allocator<void> > sensor_data;

typedef boost::shared_ptr< ::deepfind_package::sensor_data > sensor_dataPtr;
typedef boost::shared_ptr< ::deepfind_package::sensor_data const> sensor_dataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::deepfind_package::sensor_data_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::deepfind_package::sensor_data_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace deepfind_package

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/kinetic/share/nav_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'deepfind_package': ['/home/nvidia/DeepFind/catkin_ws/src/deepfind_package/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::deepfind_package::sensor_data_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::deepfind_package::sensor_data_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepfind_package::sensor_data_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepfind_package::sensor_data_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepfind_package::sensor_data_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepfind_package::sensor_data_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::deepfind_package::sensor_data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9fccc7b309d5bf5d740dd999ac988ed8";
  }

  static const char* value(const ::deepfind_package::sensor_data_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9fccc7b309d5bf5dULL;
  static const uint64_t static_value2 = 0x740dd999ac988ed8ULL;
};

template<class ContainerAllocator>
struct DataType< ::deepfind_package::sensor_data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "deepfind_package/sensor_data";
  }

  static const char* value(const ::deepfind_package::sensor_data_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::deepfind_package::sensor_data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "imu_data imu\n\
sensor_msgs/LaserScan lidar\n\
encoders_data encoder\n\
\n\
================================================================================\n\
MSG: deepfind_package/imu_data\n\
Header header\n\
float64 yaw\n\
float64 pitch \n\
float64 roll\n\
float64 acc_x\n\
float64 acc_y\n\
float64 acc_z\n\
float64 gyr_x\n\
float64 gyr_y\n\
float64 gyr_z\n\
float64 mag_x\n\
float64 mag_y\n\
float64 mag_z\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: sensor_msgs/LaserScan\n\
# Single scan from a planar laser range-finder\n\
#\n\
# If you have another ranging device with different behavior (e.g. a sonar\n\
# array), please find or create a different message, since applications\n\
# will make fairly laser-specific assumptions about this data\n\
\n\
Header header            # timestamp in the header is the acquisition time of \n\
                         # the first ray in the scan.\n\
                         #\n\
                         # in frame frame_id, angles are measured around \n\
                         # the positive Z axis (counterclockwise, if Z is up)\n\
                         # with zero angle being forward along the x axis\n\
                         \n\
float32 angle_min        # start angle of the scan [rad]\n\
float32 angle_max        # end angle of the scan [rad]\n\
float32 angle_increment  # angular distance between measurements [rad]\n\
\n\
float32 time_increment   # time between measurements [seconds] - if your scanner\n\
                         # is moving, this will be used in interpolating position\n\
                         # of 3d points\n\
float32 scan_time        # time between scans [seconds]\n\
\n\
float32 range_min        # minimum range value [m]\n\
float32 range_max        # maximum range value [m]\n\
\n\
float32[] ranges         # range data [m] (Note: values < range_min or > range_max should be discarded)\n\
float32[] intensities    # intensity data [device-specific units].  If your\n\
                         # device does not provide intensities, please leave\n\
                         # the array empty.\n\
\n\
================================================================================\n\
MSG: deepfind_package/encoders_data\n\
int32 leftMotor\n\
int32 rightMotor\n\
";
  }

  static const char* value(const ::deepfind_package::sensor_data_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::deepfind_package::sensor_data_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.imu);
      stream.next(m.lidar);
      stream.next(m.encoder);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct sensor_data_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::deepfind_package::sensor_data_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::deepfind_package::sensor_data_<ContainerAllocator>& v)
  {
    s << indent << "imu: ";
    s << std::endl;
    Printer< ::deepfind_package::imu_data_<ContainerAllocator> >::stream(s, indent + "  ", v.imu);
    s << indent << "lidar: ";
    s << std::endl;
    Printer< ::sensor_msgs::LaserScan_<ContainerAllocator> >::stream(s, indent + "  ", v.lidar);
    s << indent << "encoder: ";
    s << std::endl;
    Printer< ::deepfind_package::encoders_data_<ContainerAllocator> >::stream(s, indent + "  ", v.encoder);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DEEPFIND_PACKAGE_MESSAGE_SENSOR_DATA_H
