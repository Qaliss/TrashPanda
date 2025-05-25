import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # pkg_path = get_package_share_directory('trashbot')
    # urdf_path = os.path.join(pkg_path, 'urdf/urdf/garbagebot.urdf')
    urdf = os.path.join(get_package_share_directory('trashbot'), 'urdf/urdf/garbagebot.urdf')
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        # Launch Gazebo with the empty world
        ExecuteProcess(
            cmd=[
                'gazebo', '--verbose',
                '/home/qalis/ros2_ws/src/trashbot/configs/room.world',
                '-s', 'libgazebo_ros_factory.so'
            ],
            output='screen'
        ),

        # Spawn your robot into Gazebo

        TimerAction(
            period=5.0,
            actions=[
                ExecuteProcess(
                    cmd=[
                        'ros2', 'run', 'gazebo_ros', 'spawn_entity.py',
                        '-entity', 'trashbot',
                        '-file', urdf,
                        '-x', '-2', '-y', '1.5', '-z', '2'
                    ],
                    output='screen'
                )
            ]
        ),
        
    ])
