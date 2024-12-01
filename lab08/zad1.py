import numpy as np

def getMatrix(n):
    matrix = np.ones((n, n), dtype = int)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            matrix[i, j] = pow(i+1, j)
    return matrix

M = getMatrix(9)
print(M)