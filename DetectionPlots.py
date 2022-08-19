def histogram(spots, imarray, spots_post_decomposition, spots_post_clustering,clusters):
    import numpy as np
    import matplotlib.pyplot as plt
    ypos = spots[:, 1]
    ylength = imarray.shape[1]
    bins_yplot = np.linspace(0, ylength, num=20)
    fig = plt.figure(figsize=(10, 7))
    plt.hist(ypos, bins_yplot)
    plt.title("Spots detection")
    plt.xlabel("position on x axis (pixel)")
    plt.ylabel("Count of mRNAs")  # plotting spot detected
    plt.savefig("results/spot_detection.png")
    # Code block 9.2
    # -----------------------------------------------------------------------
    # histogram of spot post decomposition
    ypos = spots_post_decomposition[:, 1]
    hist = plt.hist(ypos, bins_yplot)
    plt.title("Spots detection post decomposition")
    plt.xlabel("position on x axis (pixel)")
    plt.ylabel("Count of mRNAs")
    plt.savefig("results/spot_detection_post_decomposition.png")
    # Code block 9.3
    # -------------------------------------------------------------------------
    # histogram of spot post declustering
    ypos = spots_post_clustering[:, 1]
    hist = plt.hist(ypos, bins_yplot)
    plt.title("Spots detection post cluster detection")
    plt.xlabel("position on x axis (pixel)")
    plt.ylabel("Count of mRNAs")
    plt.savefig("results/spot_detection_post_cluster_detection.png")
    # Code block 9.4
    # -------------------------------------------------------------------------
    # histogram of two dimenstions
    ypos = spots[:, 1]
    xpos = spots[:, 2]
    plt.hist2d(xpos, ypos, bins=20)
    plt.xlabel("position on x axis (pixel)")
    plt.ylabel("position on y axis (pixel)")
    plt.savefig("results/2dhist.png")
    # Code block 9.5
    # --------------------------------------------------------------------------
    # Histogram of clusters
    ypos_cluster = clusters[:, :3][:, 1]
    plt.hist(ypos_cluster, bins_yplot)
    plt.title("cluster detection")
    plt.xlabel("position on x axis (pixel)")
    plt.ylabel("Count of clusters")
    plt.savefig("results/cluster_detection.png")
    plt.close(fig)
    return
