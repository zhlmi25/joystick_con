from launch_ros.actions import Node
from launch import LaunchDescription
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Get the path to the joy config file
    joystick_config_path = os.path.join(
        get_package_share_directory('joy_control'),
        'config',
        'joystick.yaml'
    )


    return LaunchDescription([
        # Launch the joy node
        Node(
            package='joy',
            executable='joy_node',
            name='joy_node',
            parameters=[joystick_config_path]
        ),
        # Launch the teleop node
        Node(
            package='teleop_twist_joy',
            executable='teleop_node',
            name='teleop_node',
            parameters=[joystick_config_path]
        ),
    ])
