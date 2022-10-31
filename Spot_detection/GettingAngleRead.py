
def get_angle_read(file_path="."):
    """
    This is a function to read angle measured by ImageJ in a csv file. 
    If there is no csv file in the folder it will return 0 
    Else it will calculate the average of the angle measured and return an averaged number of measured angles 
    Input: File_path, where file is stored. Default is current folder 
    Return: If there is a csv file in the folder, then return measured angle 
            Else return 0 
    """
    import os
    import glob
    import pandas as pd
    import statistics
    os.chdir(file_path)
    csv_name = glob.glob("*.csv")
    if csv_name:
        angle_read = pd.read_csv(csv_name[0])
        angle = 90 - statistics.mean(angle_read["Angle"])
        return angle
    else:
        return 0





