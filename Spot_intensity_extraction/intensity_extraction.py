def sot_range_identification(single_spot,spot_pixelsize,imarray_size):
    import numpy as np
    spot_sphere = []
    spot_sphere.append(single_spot)
    x_dim = imarray_size[1]
    y_dim = imarray_size[2]
    for i in range(0,int(spot_pixelsize[1])):
        a = single_spot[0]
        b = single_spot[1]-1-i
        c = single_spot[2]
        temp_up_spot = np.array([a,b,c])
        if b > 0:
            spot_sphere.append(temp_up_spot)
        d = single_spot[0]
        e = single_spot[1]+1+i
        f = single_spot[2]
        temp_down_spot = np.array([d,e,f])
        if e < x_dim:
            spot_sphere.append(temp_down_spot)
        for j in range(0,int(spot_pixelsize[1])-i):
            g = single_spot[0]
            h = b
            x = single_spot[2]-1-j
            temp_bottomright_spot = np.array([g,h,x])
            if x >0 and b>0:
                spot_sphere.append(temp_bottomright_spot)
            y = single_spot[0]
            k = b
            l = single_spot[2]+1+j
            temp_bottomleft_spot = np.array([y,k,l])
            if l < y_dim and b>0:
                spot_sphere.append(temp_bottomleft_spot)
            m = single_spot[0]
            n = e
            o = single_spot[2]+1+j
            temp_topright_spot = np.array([m,n,o])
            if o < y_dim and n < x_dim:
                spot_sphere.append(temp_topright_spot)
            p= single_spot[0]
            q= e
            r=single_spot[2]-1-j
            temp_topleft_spot = np.array([p,q,r])
            if r>0 and q < x_dim:
                spot_sphere.append(temp_topleft_spot)
    return spot_sphere

def add_intensity(spot,spot_sphere,imarray):
    import numpy as np
    sum_intensity = 0
    for i in range(np.shape(spot_sphere)[0]):
        a = spot_sphere[i][0]
        b = spot_sphere[i][1]
        c = spot_sphere[i][2]
        intensity = imarray[a,b,c]
        sum_intensity = sum_intensity + intensity
    spot_withintensity= np.append(spot,sum_intensity)
    return spot_withintensity