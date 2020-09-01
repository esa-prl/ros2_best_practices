#ifndef ROS2_PACKAGE_TEMPLATE_H
#define ROS2_PACKAGE_TEMPLATE_H

#include "rclcpp/rclcpp.hpp"

class Ros2PackageTemplateNode : public rclcpp::Node
{
public:
    Ros2PackageTemplateNode(rclcpp::NodeOptions options, std::string node_name);

private:
};

#endif