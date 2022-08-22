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
from GettingAngleRead import *
from Preprocessing import *
from spotdetection import *
from ClusterDecomposition import *
from DetectionPlots import *
# You should include all files over here
filepath = "D:/Northwestern/Research/Christian Petersen Lab/080322_testing_for_quest"

minimal_distance = (1, 1, 1)   # Minimal distance of spots z,x, y
kernel_size = (2.5, 1.5, 1.5)   # Kernel size of LoG filter, z usuall 2.5-4, x,y start with 1.5
resolution = (373, 95, 95)   # Resolution in nanometer on image, retrieve from LASX
spot_size = (350, 250, 250)   # expected spot size, usuall 200-600 in x,y, 300-800 on z
greeks = (0.7, 1, 5)  # Special numbers for decomposition
# First number alpha: Impact number of spots in each regtion
# Second number beta, affect number of regions to decompose
# Third number gamma, filtering for image denoise
declustering_parameters = (400, 4)
# Fist number is radius of single spots,
# second number is minimal spots in a cluster
# Read the angle and preprocess the image
angle = get_angle_read(filepath)
imarray = smFISHpreprocessing(kernel_size, minimal_distance,filepath)
# Rotate the image to a good 90 degree
imarray = rotateImage(angle,imarray)
# Get elbow curve and spot detection
get_elbow_curve(imarray,resolution,spot_size,filepath)
spots, threshold = spot_detection(imarray,resolution, spot_size,kernel_size,minimal_distance,filepath)
spots_plot_detection(spots,imarray,filepath)
# Decluster and decompose spots
spots_post_decomposition,dense_regions,reference_spot = cluster_decomposition(imarray,spots,resolution,spot_size, greeks)
spots_post_clustering, clusters = declustering(imarray,spots_post_decomposition,resolution,declustering_parameters)
histogram(spots,imarray,spots_post_decomposition,spots_post_clustering,clusters)
