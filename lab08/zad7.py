import numpy as np

def getMatrix(n, m):
    matrix = np.random.randint(2, 22, (n, m))
    for i in range(0, n):
        for j in range(0, m):
            if(matrix[i, j] %2 == 0):
                matrix[i, j] = -100
            else:
                matrix[i, j] = 100
    return matrix

M = getMatrix(4,6)
print(M)
