def cluster_decomposition(imarray,spots,resolution,spot_size,greeks,filepath = "."):
    """
    Decomposition of clusters 
    :param imarray: Image array 
    :param spots: spots detected 
    :param resolution: resolution 
    :param spot_size: spot size 
    :param greeks: greeks alpaha beta gamma 
    :return: 
    """
    import os
    import bigfish.detection
    import bigfish.plot as plot
    import bigfish.stack as stack
    os.chdir(filepath)
    alpha = greeks[0]
    beta = greeks[1]
    gamma = greeks[2]
    spots_post_decomposition, dense_regions, reference_spot = bigfish.detection.decompose_dense(
    image=imarray,
    spots=spots,
    voxel_size= resolution,
    spot_radius= spot_size,
    alpha=alpha,  # alpha impacts the number of spots per candidate region
    beta=beta,  # beta impacts the number of candidate regions to decompose
    gamma=gamma)  # gamma the filtering step to denoise the image
    max_imarray = stack.maximum_projection(imarray)
    with open("results/spots_info_Decomposition.txt","w") as file :
        file.write("detected spots before decomposition")
        file.write("\r shape: {0}".format(spots.shape))
        file.write("\r dtype: {0}".format(spots.dtype))
        file.write("\n")
        file.write("detected spots after decomposition")
        file.write("\r shape: {0}".format(spots_post_decomposition.shape))
        file.write("\r dtype: {0}".format(spots_post_decomposition.dtype))
    plot.plot_detection(max_imarray,
                        spots_post_decomposition,
                        contrast=True,
                        path_output="results/detectionmap2D_rotated_post_decomposition",
                        ext="tif",
                        show=False)
    return spots_post_decomposition,dense_regions,reference_spot

def declustering(imarray, spots_post_decomposition,resolution,deculstering_parameters):
    """
    Declustering code
    :param spots_post_decompositions: spots
    :param resolution: resolution
    :param deculstering_parameters:declustering parameters
    imarray: image array
    :return: spts and clusters
    """
    radius = deculstering_parameters[0]
    nb_min_spots = deculstering_parameters[1]
    import bigfish.detection
    import bigfish.stack as stack
    import bigfish.plot as plot
    spots_post_clustering, clusters = bigfish.detection.detect_clusters(
        spots=spots_post_decomposition,
        voxel_size=resolution,
        radius=radius,
        nb_min_spots=nb_min_spots)
    with open("results/Cluster_info.txt", "w") as file:
        file.write("detected spots after clustering")
        file.write("\r shape: {0}".format(spots_post_clustering.shape))
        file.write("\r dtype: {0}".format(spots_post_clustering.dtype))
        file.write("\n")
        file.write("detected clusters")
        file.write("\r shape: {0}".format(clusters.shape))
        file.write("\r dtype: {0}".format(clusters.dtype))
    max_imarray = stack.maximum_projection(imarray)
    # Plot declustering
    plot.plot_detection(max_imarray,
                        spots=[spots_post_decomposition, clusters[:, :3]],
                        shape=["circle", "polygon"],
                        radius=[3, 6],
                        color=["red", "blue"],
                        linewidth=[1, 2],
                        fill=[False, True],
                        contrast=True,
                        path_output='results/detectionmap2D_clustered',
                        ext='tif',
                       show=False)
    return spots_post_clustering, clusters