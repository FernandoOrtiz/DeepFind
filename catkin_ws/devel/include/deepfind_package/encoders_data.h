// Generated by gencpp from file deepfind_package/encoders_data.msg
// DO NOT EDIT!


#ifndef DEEPFIND_PACKAGE_MESSAGE_ENCODERS_DATA_H
#define DEEPFIND_PACKAGE_MESSAGE_ENCODERS_DATA_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace deepfind_package
{
template <class ContainerAllocator>
struct encoders_data_
{
  typedef encoders_data_<ContainerAllocator> Type;

  encoders_data_()
    : leftMotor(0)
    , rightMotor(0)  {
    }
  encoders_data_(const ContainerAllocator& _alloc)
    : leftMotor(0)
    , rightMotor(0)  {
  (void)_alloc;
    }



   typedef int32_t _leftMotor_type;
  _leftMotor_type leftMotor;

   typedef int32_t _rightMotor_type;
  _rightMotor_type rightMotor;





  typedef boost::shared_ptr< ::deepfind_package::encoders_data_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::deepfind_package::encoders_data_<ContainerAllocator> const> ConstPtr;

}; // struct encoders_data_

typedef ::deepfind_package::encoders_data_<std::allocator<void> > encoders_data;

typedef boost::shared_ptr< ::deepfind_package::encoders_data > encoders_dataPtr;
typedef boost::shared_ptr< ::deepfind_package::encoders_data const> encoders_dataConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::deepfind_package::encoders_data_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::deepfind_package::encoders_data_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace deepfind_package

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'deepfind_package': ['/root/DeepFind/catkin_ws/src/deepfind_package/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::deepfind_package::encoders_data_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::deepfind_package::encoders_data_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepfind_package::encoders_data_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepfind_package::encoders_data_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepfind_package::encoders_data_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepfind_package::encoders_data_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::deepfind_package::encoders_data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "40c59515e060d941dde4c816f719e5bb";
  }

  static const char* value(const ::deepfind_package::encoders_data_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x40c59515e060d941ULL;
  static const uint64_t static_value2 = 0xdde4c816f719e5bbULL;
};

template<class ContainerAllocator>
struct DataType< ::deepfind_package::encoders_data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "deepfind_package/encoders_data";
  }

  static const char* value(const ::deepfind_package::encoders_data_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::deepfind_package::encoders_data_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 leftMotor\n\
int32 rightMotor\n\
";
  }

  static const char* value(const ::deepfind_package::encoders_data_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::deepfind_package::encoders_data_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.leftMotor);
      stream.next(m.rightMotor);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct encoders_data_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::deepfind_package::encoders_data_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::deepfind_package::encoders_data_<ContainerAllocator>& v)
  {
    s << indent << "leftMotor: ";
    Printer<int32_t>::stream(s, indent + "  ", v.leftMotor);
    s << indent << "rightMotor: ";
    Printer<int32_t>::stream(s, indent + "  ", v.rightMotor);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DEEPFIND_PACKAGE_MESSAGE_ENCODERS_DATA_H
