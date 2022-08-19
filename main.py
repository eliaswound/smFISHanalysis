# Two important packages for running sm-FISH analysis
# Tiffile is a package useful for reading big-TIFF format files.
# Big-Tiff can exceed 4GB limit of tiff files, and is hard to be read through conventional methods.
# For details about this package, please visit https://pypi.org/project/tifffile/
# FISH-quant/big-FISH is for quantification.
# For more general details about this package, please visit https://big-fish.readthedocs.io/en/stable/stack/io.html
# and please refer to the paper https://www.biorxiv.org/content/10.1101/2021.07.20.453024v1.full
# If you need install these packages please run the following code. for using jupyter notebook
# For using other console just use pip install + package
# import sys
# !{sys.executable} -m pip install big-fish
# !{sys.executable} -m pip install tifffile
# !{sys.executable} -m pip install -U scikit-learn
# importing everything

from platform import python_version
import os
from PIL import Image
import numpy as np
import tifffile
import scipy.ndimage as nd
import matplotlib.pyplot as plt
from skimage import data
import bigfish
import bigfish.stack as stack
import bigfish.multistack as multistack
import bigfish.plot as plot
import glob


# Enter your file path over here
# You should include all files over here
filepath = ""

