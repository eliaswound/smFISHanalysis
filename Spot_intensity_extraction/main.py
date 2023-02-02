# This protocol is written for detect single spot intensity in each image.
# Please notice you should have known your spot intensity does not exceed maximum or overexpose in your collection

import numpy as np
import glob
import os
import tifffile
import matplotlib.pyplot as plt
from intensity_extraction import *
filepath  = "D:/Northwestern/Research/Christian_Petersen_Lab/112822_temp/Colocalization/647"
os.chdir(filepath)
resolution = (373, 142, 142)   # Resolution in nanometer on image, retrieve from LASX
spot_size = (400, 200, 200)   # expected spot size, usuall 200-600 in x,y, 300-800 on z
spotnames = glob.glob('results/*spot.npy')
clusternames = glob.glob('results/*clusters.npy')
imagenames = glob.glob("results/*imarray_rotated.tif")
# Start here you should look for difference between clusters and spots
# Deal with spots first
spots = np.load(spotnames[0])
clusters = np.load(clusternames[0])
imarray = tifffile.imread(imagenames[0])
imarray_size = np.shape(imarray)
spots_intensity = []
spot_pixelsize=np.floor(np.array(spot_size)/np.array(resolution))
spots_intensity = []
for item in spots:
    spot_sphere = sot_range_identification(item,spot_pixelsize,imarray_size)
    spot_withintensity = add_intensity(item,spot_sphere,imarray)
    spots_intensity.append(spot_withintensity)
np.save('results/spotwithintensity.npy',spots_intensity)
intensity_value = []
for item in spots_intensity:
    intensity_number = item[3]
    intensity_value.append(intensity_number)
np.save('results/intensity.npy', intensity_value)
bins_hist = np.linspace(0, max(intensity_value), num=50)
fig = plt.figure(figsize=(10, 7))
plt.hist(intensity_value,bins_hist)
plt.savefig("results/cluster_detection.png")
plt.close(fig)