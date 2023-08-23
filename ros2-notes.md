# Package Creation

Adapted from https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html and from https://docs.ros.org/en/foxy/Tutorials/Beginner-Client-Libraries/Custom-ROS2-Interfaces.html#create-a-new-package.

1) `cd AccuRad-PRD/src/`

2) `. /opt/ros/humble/setup.bash`

3) `ros2 pkg create --build-type ament_python driver_accurad_prd`

4) `ros2 pkg create --build-type ament_cmake accurad_interfaces`