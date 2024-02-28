import sys
import os

# Determine the absolute path to the directory containing 'utils'
# Replace 'path_to_utils_directory' with the actual path to the directory containing 'utils'
utils_directory = '/content/yolov9/utils'
absolute_path_to_utils = os.path.abspath(utils_directory)

# Add this directory to sys.path
if absolute_path_to_utils not in sys.path:
    sys.path.insert(0, absolute_path_to_utils)

# Now you can import your module
# from utils import ...


# Now you can import your module
# from utils import ...
current_directory = os.path.dirname(os.path.abspath(__file__))
if current_directory not in sys.path:
    sys.path.insert(0, current_directory)
