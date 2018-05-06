// Generated by gencpp from file deepfind_package/distance_traveled.msg
// DO NOT EDIT!


#ifndef DEEPFIND_PACKAGE_MESSAGE_DISTANCE_TRAVELED_H
#define DEEPFIND_PACKAGE_MESSAGE_DISTANCE_TRAVELED_H


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
struct distance_traveled_
{
  typedef distance_traveled_<ContainerAllocator> Type;

  distance_traveled_()
    : absolute_origin(0.0)
    , absolute_landmark(0.0)  {
    }
  distance_traveled_(const ContainerAllocator& _alloc)
    : absolute_origin(0.0)
    , absolute_landmark(0.0)  {
  (void)_alloc;
    }



   typedef double _absolute_origin_type;
  _absolute_origin_type absolute_origin;

   typedef double _absolute_landmark_type;
  _absolute_landmark_type absolute_landmark;





  typedef boost::shared_ptr< ::deepfind_package::distance_traveled_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::deepfind_package::distance_traveled_<ContainerAllocator> const> ConstPtr;

}; // struct distance_traveled_

typedef ::deepfind_package::distance_traveled_<std::allocator<void> > distance_traveled;

typedef boost::shared_ptr< ::deepfind_package::distance_traveled > distance_traveledPtr;
typedef boost::shared_ptr< ::deepfind_package::distance_traveled const> distance_traveledConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::deepfind_package::distance_traveled_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::deepfind_package::distance_traveled_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace deepfind_package

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'nav_msgs': ['/opt/ros/kinetic/share/nav_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'actionlib_msgs': ['/opt/ros/kinetic/share/actionlib_msgs/cmake/../msg'], 'sensor_msgs': ['/opt/ros/kinetic/share/sensor_msgs/cmake/../msg'], 'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'deepfind_package': ['/home/rathk/DeepFind/catkin_ws/src/deepfind_package/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::deepfind_package::distance_traveled_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::deepfind_package::distance_traveled_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepfind_package::distance_traveled_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::deepfind_package::distance_traveled_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepfind_package::distance_traveled_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::deepfind_package::distance_traveled_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::deepfind_package::distance_traveled_<ContainerAllocator> >
{
  static const char* value()
  {
    return "2090cb8db4678ff5744ff25e1aeb8f66";
  }

  static const char* value(const ::deepfind_package::distance_traveled_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x2090cb8db4678ff5ULL;
  static const uint64_t static_value2 = 0x744ff25e1aeb8f66ULL;
};

template<class ContainerAllocator>
struct DataType< ::deepfind_package::distance_traveled_<ContainerAllocator> >
{
  static const char* value()
  {
    return "deepfind_package/distance_traveled";
  }

  static const char* value(const ::deepfind_package::distance_traveled_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::deepfind_package::distance_traveled_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 absolute_origin\n\
float64 absolute_landmark\n\
";
  }

  static const char* value(const ::deepfind_package::distance_traveled_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::deepfind_package::distance_traveled_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.absolute_origin);
      stream.next(m.absolute_landmark);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct distance_traveled_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::deepfind_package::distance_traveled_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::deepfind_package::distance_traveled_<ContainerAllocator>& v)
  {
    s << indent << "absolute_origin: ";
    Printer<double>::stream(s, indent + "  ", v.absolute_origin);
    s << indent << "absolute_landmark: ";
    Printer<double>::stream(s, indent + "  ", v.absolute_landmark);
  }
};

} // namespace message_operations
} // namespace ros

#endif // DEEPFIND_PACKAGE_MESSAGE_DISTANCE_TRAVELED_H
