import numpy as np

def max_of_row_mins(matrix):
    arr = np.array(matrix)
    row_mins = np.min(arr, axis=1)
    return np.max(row_mins)
