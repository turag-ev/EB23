# ROS Packages

Directory for ROS package development.
Packages are created in the `src` directory.

In order to create new ROS packages run 
```
ros2 pkg create --build_type ament_python <package_name>
```
in a command shell in the `src` directory (LINUX).

In order to build your package run
```
colcon build
```
in a command shell in the `ros_packages` directory (LINUX).
