from setuptools import find_packages, setup

package_name = 'radar_system'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='bibek_innovates',
    maintainer_email='bibekcwl04@gmail.com',
    description='ROS2 Radar System',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'radar_publisher = radar_system.radar_publisher:main',
            'radar_visualizer = radar_system.radar_visualizer:main',
        ],
    },
)
