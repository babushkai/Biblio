def matrixReshape(mat, r, c):
    import numpy as np
    """
    :type mat: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    try:
        return np.reshape(mat, (r, c)).tolist()
    except:
        return mat