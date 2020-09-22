cmake_minimum_required(VERSION 3.5)
project(package_template)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

include_directories(include)


add_executable(package_template_node src/package_template_node.cpp)
ament_target_dependencies(package_template_node rclcpp)

install(TARGETS
  package_template_node
  DESTINATION lib/${PROJECT_NAME})

ament_package()
