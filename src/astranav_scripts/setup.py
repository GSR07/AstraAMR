from setuptools import find_packages, setup

package_name = 'astranav_scripts'

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
    maintainer='gsr',
    maintainer_email='ganeshsreddy1@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'read_lidar = astranav_scripts.read_lidar:main',
            'read_imu = astranav_scripts.read_imu:main',
            'read_camera = astranav_scripts.read_camera:main',
            'detect_marker = astranav_scripts.detect_marker:main',
            'maze_solver = astranav_scripts.maze_solver:main',
            'auto_dock_undock = astranav_scripts.auto_dock_undock:main',
            'docling_with_patrolling = astranav_scripts.docling_with_patrolling:main',
            'battery_auto_dock=  astranav_scripts.auto_docking_with_battery:main',
            'cleaning = astranav_scripts.Cleaning_with_battery:main',
            'rl_nav = astranav_scripts.rl_docking:main',
        ],
    },
)
