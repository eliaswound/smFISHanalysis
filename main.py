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


# Enter your file path over here
# You should include all files over here
filepath="D:/Northwestern/Research/Christian Petersen Lab/080322_testing_for_quest"

from GettingAngleRead import *
from Preprocessing import *
from spotdetection import *

minimal_distance = (1, 1, 1)
kernel_size = (2.5, 1.5, 1.5)
resolution = (373, 95, 95)
spot_size = (350, 250, 250)

angle = get_angle_read(filepath)
imarray = smFISHpreprocessing(kernel_size, minimal_distance,filepath)
rotated_imarray = rotateImage(angle,imarray)
del imarray
get_elbow_curve(rotated_imarray,resolution,spot_size,filepath)
spots, threshold = spot_detection(imarry,resolution, spot_size,kernel_size,minimal_distance)

