def saveMass(nparray, fn, b_1st_time=False):
    """ Save mass and fractions to file
    Args:
        nparray -- the data to be saved
        b_1st_time -- if True, write to a new file; otherwise append to the existing file
    """
    # --------------------------------------------------------------------------------------------------------------
    import numpy as np
    # --------------------------------------------------------------------------------------------------------------
    if b_1st_time:
        file = open(fn, 'w')
    else:
        file = open(fn, 'a')

    if type(nparray) is np.ndarray:
        nd = len(nparray)
        for i in range(nd):
            file.write("{:.6e}".format(nparray[i]))
            if i < nd - 1:
                file.write(",")
                # print("nparray", file)
    else:
        file.write("{:.6e}".format(nparray))
    file.write('\n')
    file.close()