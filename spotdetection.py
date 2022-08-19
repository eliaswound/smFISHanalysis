def get_elbow_curve(imarray, resolution,spot_size, filepath = "."):
    """
    Plots and saves elbow curve
    :param imarray: Image array
    :param resolution: Resolution on z,x,y as nanommeters
    :param spot_size: Spot size or spot radius
    :param filepath: Filepath, default current filepath
    :return: Filepath
    """
    import bigfish.plot as plot
    import os
    os.chdir(filepath)
    plot.plot_elbow(
        images=imarray,
        voxel_size=resolution,
        spot_radius=spot_size,
        path_output="results/Elbow",
        show=False)
    elbow_path = filepath + "results/Elbow"
    return elbow_path

def spot_detection(imarray, resolution, spot_size, kernel_size,minimal_distance):
    """
    This is the core spot detection program:
    input:
    :param imarray: Image array for spot detection
    :param resoltuion: Resolution z,x,y
    :param spot_size: Spot size
    :param kernel_size: Kernal size for LoG filter
    :param minimal_distance: Minimal distance between spots
    :return: Detected spots, threshold
    """
    import bigfish.detection
    spots, threshold = bigfish.detection.detect_spots(
        images=imarray,
        return_threshold=True,
        voxel_size= resolution,  # in nanometer (one value per dimension zyx)
        spot_radius= spot_size, # in nanometer (one value per dimension zyx)
        log_kernel_size= kernel_size,
        minimum_distance= minimal_distance)
    snr_ratio = bigfish.detection.compute_snr_spots(imarray, spots, resolution, spot_size)
    # Out put your spot detection results as txt file
    # Also added a estimation of signal-to-noise ratio
    with open ("results/spot_info.txt","w") as file :
        file.write("\r shape: {0}".format(spots.shape))
        file.write("\r dtype: {0}".format(spots.dtype))
        file.write("\r threshold: {0}".format(threshold))
        file.write("\r SNR ratio:{0}".format(snr_ratio))
    return spots, threshold
