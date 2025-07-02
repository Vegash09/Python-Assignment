import numpy as np

def compute_statistics(arr):
    ans = np.array(arr, dtype=float)
    mean = np.mean(ans, axis=1)
    var = np.var(ans, axis=0)
    std = round(np.std(ans, axis=None), 11)
    return mean, var, std
