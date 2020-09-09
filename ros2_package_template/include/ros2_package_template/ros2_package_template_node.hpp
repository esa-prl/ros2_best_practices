#ifndef ROS2_PACKAGE_TEMPLATE_NODE_HPP_
#define ROS2_PACKAGE_TEMPLATE_NODE_HPP_

#include "rclcpp/rclcpp.hpp"

class Ros2PackageTemplateNode : public rclcpp::Node
{
public:
    Ros2PackageTemplateNode(rclcpp::NodeOptions options, std::string node_name);

private:
};

#endif
