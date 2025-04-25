from setuptools import find_packages, setup

package_name = 'joy_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/joystick.launch.py']),  # Updated launch file name
        ('share/' + package_name + '/config', ['config/joystick.yaml']),  # Added config file
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='zouq',
    maintainer_email='rahmanzulhilmi@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
