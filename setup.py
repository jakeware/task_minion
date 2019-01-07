## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['task_minion',
              'task_minion_ros'
              'task_master'
              'task_master_ros',
              'test_nodes'],
    package_dir={'': 'src'}
)

setup(**setup_args)