from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='capra_opi',
            namespace='capra_opi',
            executable='main',
            name='opi',
        ),
        Node(
            package='capra_opi',
            namespace='capra_opi',
            executable='pub',
            name='opi',
        ),
    ])