#ifndef PACKAGE_TEMPLATE_NODE_HPP_
#define PACKAGE_TEMPLATE_NODE_HPP_

#include "rclcpp/rclcpp.hpp"

class PackageTemplateNode : public rclcpp::Node
{
public:
    PackageTemplateNode(rclcpp::NodeOptions options, std::string node_name);

private:
};

#endif
