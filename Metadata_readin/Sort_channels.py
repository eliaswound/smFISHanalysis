# Run this for sorting channels
# This code takes input folder with a bunch of images output from LASX
# This code also moves the xml file from metadata out into the same image folder
from tkinter import filedialog
from tkinter import *
from glob import glob
import os
import shutil
root = Tk()
filepath = filedialog.askdirectory()
root.destroy()
os.chdir(filepath)
filenames = glob("*.tif")
dir_list = os.listdir()
if '405' not in dir_list:
    os.mkdir("405")
if '565' not in dir_list:
    os.mkdir("565")
if '647' not in dir_list:
    os.mkdir("647")
if len(filenames) !=0:
    for filename in filenames:
        if int(filename[-5]) == 0:
            shutil.move(filename,"405")
        elif int(filename[-5]) == 1:
            shutil.move(filename,"565")
        elif int(filename[-5]) == 2:
            shutil.move(filename,"647")
os.chdir("647")
ch3_filenames = glob("*.tif")
ch3_dirlist = os.listdir()
for i in range(len(ch3_filenames)):
    dir_name = "Image" + str((i+1))
    if dir_name not in ch3_dirlist:
        os.mkdir(dir_name)
        shutil.move(ch3_filenames[i],dir_name)

