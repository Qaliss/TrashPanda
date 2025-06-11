# TrashPanda
A simulated autonomous robot developed in ROS2 that classifies and collects trash using computer vision and autonomous navigation.

This is a proof-of-concept developed under the mentorship of Kaleidoscope Innovations during the spring semester of 2025.

## Overview
This robot autonomous navigates through an environment using a ROS2 navigation stack. Firstly, it will survey the room and use 2D SLAM to map out its surroundings. During this survey, the robot will use a YOLOv8 object detection model in addition to depth camera data in order to flag points on the generated map where trash is detected. After completing its survey, the robot will generate the most efficient path through the flagged points, where it will use a manipulator to dispose of the trash along the way. 

## Features
- Autonomous navigation using ROS2 and Nav2
- Trash classification and detection with custom trained YOLOv8 model
- Simulation environment in Gazebo
- Intake system for collection
