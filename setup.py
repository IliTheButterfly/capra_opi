from glob import glob
import os
from setuptools import find_packages, setup

package_name = 'capra_opi'

setup(
    name=package_name,
    version='0.0.0',
    # packages=[package_name, *submodules],
    packages=find_packages(exclude=['test']),
    
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools', 
        'numpy',
        'matplotlib',
        'opencv-contrib-python',
        'imutils',
        'pytesseract',
        'tqdm',
        'colorama',
        'scikit-learn',
    ],
    zip_safe=True,
    maintainer='jocobc',
    maintainer_email='jocobc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'main = capra_opi.main:main',
            'pub = capra_opi.publisher:main',
        ],
    },
)
