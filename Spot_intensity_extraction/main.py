# This protocol is written for detect single spot intensity in each image.
# Please notice you should have known your spot intensity does not exceed maximum or overexpose in your collection

import numpy as np
import glob
import os
filepath  = "D:/Northwestern/Research/Christian_Petersen_Lab/060722_python_script_test"
os.chdir(filepath)
resolution = (373, 95, 95)   # Resolution in nanometer on image, retrieve from LASX
spot_size = (600, 400, 400)   # expected spot size, usuall 200-600 in x,y, 300-800 on z
filenames = glob.glob('results/*.npy')
imagenames = glob.glob("*.tif")
