import numpy as np

def getMatrix(n):
    matrix = np.zeros((n, n), dtype = int)
    start = 1; stop = n+1
    for i in range(0, n):
        matrix[i] = np.arange(start, stop, 1)
        start += n; stop += n
    return matrix

M = getMatrix(5)
print(M)