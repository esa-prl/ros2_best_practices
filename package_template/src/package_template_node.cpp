#include "package_template/package_template_node.hpp"

PackageTemplateNode::PackageTemplateNode(rclcpp::NodeOptions options, std::string node_name)
    : Node(node_name)
{
}

int main(int argc, char *argv[])
{
    rclcpp::NodeOptions options;
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<PackageTemplateNode>(options, "package_template_node"));
    rclcpp::shutdown();
    return 0;
}
