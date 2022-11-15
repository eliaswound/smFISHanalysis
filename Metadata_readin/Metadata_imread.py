# This program is for reading metadata and read in resolution of Image sets
# and it will automatically save Image in the foler it contains
from tkinter import filedialog
from tkinter import *
from glob import glob
import os
from bs4 import BeautifulSoup
# First find the directory
root = Tk()
filepath = filedialog.askdirectory()
root.destroy()
os.chdir(filepath)
# Extracting the dimensional data
# Get all file names
filenames = glob("*.tif")
# Modify the file name ends so its xmL name can be find
# In exporting, usually the suffix is _RAW_ch00/01/02.tif, I reduce this 13 characters and
# Avoided stacking same names in the list
xml_filename = []
for item in filenames:
    short_name = item[0:-13]
    if short_name not in xml_filename:
        xml_filename.append(short_name)
# Change directory to read xmL file.
os.chdir('MetaData')
for item in xml_filename:
    # The file with filename+_properties.xml will give you the dimension information
    with open (item+"_properties.xml","r") as file:
        soup = BeautifulSoup(file,"xml")
    # Tages are Dimension.DimensionDescription
    DimensionDescription = soup.Dimensions.DimensionDescription
    # Read siblings
    Dimension = DimensionDescription.find_next_siblings("DimensionDescription")
    # Number given is um but our program is nm, so need to conver to nm
    x_dim = float(str(DimensionDescription).split("Voxel=")[1].split("\"")[1].replace("e","E"))*float(1E03)
    y_dim = float(str(Dimension[0]).split("Voxel=")[1].split("\"")[1].replace("e","E"))*float(1E03)
    z_dim = float(str(Dimension[1]).split("Voxel=")[1].split("\"")[1].replace("e","E"))*float(1E03)
    os.chdir("..")
    # Write files with \n (change to next line)
    with open(item+".txt","w") as file:
        file.write(str(z_dim))
        file.write("\n")
        file.write(str(x_dim))
        file.write("\n")
        file.write(str(y_dim))
    os.chdir("MetaData")