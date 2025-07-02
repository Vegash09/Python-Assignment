import numpy as np

def calculate_determinant(matrix):
    arr = np.array(matrix)
    det = np.linalg.det(arr)
    return round(det, 2)
