import os
workpath = os.getcwd()
os.chdir(workpath)
os.chdir('Metadata_readin')
os.system('Metadata_readin.py')
os.system("Sort_channels.py")