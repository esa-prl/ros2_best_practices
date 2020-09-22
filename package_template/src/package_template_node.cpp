#include "package_template/package_template_node.hpp"

PackageTemplateNode::PackageTemplateNode()
    : Node("package_template_node")
{
}

int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<PackageTemplateNode>());
    rclcpp::shutdown();
    return 0;
}
