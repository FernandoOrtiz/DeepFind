// Generated by gencpp from file deepfind_package/keyboard.msg
// DO NOT EDIT!


#ifndef DEEPFIND_PACKAGE_MESSAGE_KEYBOARD_H
#define DEEPFIND_PACKAGE_MESSAGE_KEYBOARD_H


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
struct keyboard_
{
  typedef keyboard_<ContainerAllocator> Type;

  keyboard_()
    : origin(0)
    , landmark(0)  {
    }
  keyboard_(const ContainerAllocator& _alloc)
    : origin(0)
    , landmark(0)  {
  (void)_alloc;
    }



   typedef int32_t _origin_type;
  _origin_type origin;

   typedef int32_t _landmark_type;
  _landmark_type landmark;





  typedef boost::shared_ptr< ::deepfind_package::keyboard_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::deepfind_package::keyboard_<ContainerAllocator> const> ConstPtr;

}; // struct keyboard_

typedef ::deepfind_package::keyboard_<std::allocator<void> > keyboard;

typedef boost::shared_ptr< ::deepfind_package::keyboard > keyboardPtr;
typedef boost::shared_ptr< ::deepfind_package::keyboard const> keyboardConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::deepfind_package::keyboard_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::deepfind_package::keyboard_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace deepfind_package

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/kinetic/share/nav_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'deepfind_package': ['/home/nvidia/DeepFind/catkin_ws/src/deepfind_package/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::deepfind_package::keyboard_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::deepfind_package::keyboard_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepfind_package::keyboard_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepfind_package::keyboard_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepfind_package::keyboard_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepfind_package::keyboard_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::deepfind_package::keyboard_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9c71d7b364a278a1344691df36183a79";
  }

  static const char* value(const ::deepfind_package::keyboard_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9c71d7b364a278a1ULL;
  static const uint64_t static_value2 = 0x344691df36183a79ULL;
};

template<class ContainerAllocator>
struct DataType< ::deepfind_package::keyboard_<ContainerAllocator> >
{
  static const char* value()
  {
    return "deepfind_package/keyboard";
  }

  static const char* value(const ::deepfind_package::keyboard_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::deepfind_package::keyboard_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int32 origin\n\
int32 landmark\n\
";
  }

  static const char* value(const ::deepfind_package::keyboard_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::deepfind_package::keyboard_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.origin);
      stream.next(m.landmark);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct keyboard_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::deepfind_package::keyboard_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::deepfind_package::keyboard_<ContainerAllocator>& v)
  {
    s << indent << "origin: ";
    Printer<int32_t>::stream(s, indent + "  ", v.origin);
    s << indent << "landmark: ";
    Printer<int32_t>::stream(s, indent + "  ", v.landmark);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DEEPFIND_PACKAGE_MESSAGE_KEYBOARD_H
