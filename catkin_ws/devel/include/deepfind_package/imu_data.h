// Generated by gencpp from file deepfind_package/imu_data.msg
// DO NOT EDIT!


#ifndef DEEPFIND_PACKAGE_MESSAGE_IMU_DATA_H
#define DEEPFIND_PACKAGE_MESSAGE_IMU_DATA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>

namespace deepfind_package
{
template <class ContainerAllocator>
struct imu_data_
{
  typedef imu_data_<ContainerAllocator> Type;

  imu_data_()
    : header()
    , yaw(0.0)
    , pitch(0.0)
    , roll(0.0)
    , acc_x(0.0)
    , acc_y(0.0)
    , acc_z(0.0)
    , gyr_x(0.0)
    , gyr_y(0.0)
    , gyr_z(0.0)
    , mag_x(0.0)
    , mag_y(0.0)
    , mag_z(0.0)  {
    }
  imu_data_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , yaw(0.0)
    , pitch(0.0)
    , roll(0.0)
    , acc_x(0.0)
    , acc_y(0.0)
    , acc_z(0.0)
    , gyr_x(0.0)
    , gyr_y(0.0)
    , gyr_z(0.0)
    , mag_x(0.0)
    , mag_y(0.0)
    , mag_z(0.0)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef double _yaw_type;
  _yaw_type yaw;

   typedef double _pitch_type;
  _pitch_type pitch;

   typedef double _roll_type;
  _roll_type roll;

   typedef double _acc_x_type;
  _acc_x_type acc_x;

   typedef double _acc_y_type;
  _acc_y_type acc_y;

   typedef double _acc_z_type;
  _acc_z_type acc_z;

   typedef double _gyr_x_type;
  _gyr_x_type gyr_x;

   typedef double _gyr_y_type;
  _gyr_y_type gyr_y;

   typedef double _gyr_z_type;
  _gyr_z_type gyr_z;

   typedef double _mag_x_type;
  _mag_x_type mag_x;

   typedef double _mag_y_type;
  _mag_y_type mag_y;

   typedef double _mag_z_type;
  _mag_z_type mag_z;





  typedef boost::shared_ptr< ::deepfind_package::imu_data_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::deepfind_package::imu_data_<ContainerAllocator> const> ConstPtr;

}; // struct imu_data_

typedef ::deepfind_package::imu_data_<std::allocator<void> > imu_data;

typedef boost::shared_ptr< ::deepfind_package::imu_data > imu_dataPtr;
typedef boost::shared_ptr< ::deepfind_package::imu_data const> imu_dataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::deepfind_package::imu_data_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::deepfind_package::imu_data_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace deepfind_package

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'deepfind_package': ['/home/resorte/DeepFind/catkin_ws/src/deepfind_package/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::deepfind_package::imu_data_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::deepfind_package::imu_data_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepfind_package::imu_data_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepfind_package::imu_data_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepfind_package::imu_data_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepfind_package::imu_data_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::deepfind_package::imu_data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5781ee5294affb6dd3e062f6edb954b1";
  }

  static const char* value(const ::deepfind_package::imu_data_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5781ee5294affb6dULL;
  static const uint64_t static_value2 = 0xd3e062f6edb954b1ULL;
};

template<class ContainerAllocator>
struct DataType< ::deepfind_package::imu_data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "deepfind_package/imu_data";
  }

  static const char* value(const ::deepfind_package::imu_data_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::deepfind_package::imu_data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
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
\n\
\n\
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
";
  }

  static const char* value(const ::deepfind_package::imu_data_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::deepfind_package::imu_data_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.yaw);
      stream.next(m.pitch);
      stream.next(m.roll);
      stream.next(m.acc_x);
      stream.next(m.acc_y);
      stream.next(m.acc_z);
      stream.next(m.gyr_x);
      stream.next(m.gyr_y);
      stream.next(m.gyr_z);
      stream.next(m.mag_x);
      stream.next(m.mag_y);
      stream.next(m.mag_z);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct imu_data_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::deepfind_package::imu_data_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::deepfind_package::imu_data_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "yaw: ";
    Printer<double>::stream(s, indent + "  ", v.yaw);
    s << indent << "pitch: ";
    Printer<double>::stream(s, indent + "  ", v.pitch);
    s << indent << "roll: ";
    Printer<double>::stream(s, indent + "  ", v.roll);
    s << indent << "acc_x: ";
    Printer<double>::stream(s, indent + "  ", v.acc_x);
    s << indent << "acc_y: ";
    Printer<double>::stream(s, indent + "  ", v.acc_y);
    s << indent << "acc_z: ";
    Printer<double>::stream(s, indent + "  ", v.acc_z);
    s << indent << "gyr_x: ";
    Printer<double>::stream(s, indent + "  ", v.gyr_x);
    s << indent << "gyr_y: ";
    Printer<double>::stream(s, indent + "  ", v.gyr_y);
    s << indent << "gyr_z: ";
    Printer<double>::stream(s, indent + "  ", v.gyr_z);
    s << indent << "mag_x: ";
    Printer<double>::stream(s, indent + "  ", v.mag_x);
    s << indent << "mag_y: ";
    Printer<double>::stream(s, indent + "  ", v.mag_y);
    s << indent << "mag_z: ";
    Printer<double>::stream(s, indent + "  ", v.mag_z);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DEEPFIND_PACKAGE_MESSAGE_IMU_DATA_H
