import numpy as np

A = np.array([[4, -8, 1],[-5, -2, -9],[2, 8, 11],[-5, 4, 3]])
print(A)

B = np.zeros((4, 4), dtype = int)
print(B)

C = np.arange(2, 20, 2)
print(C)

D = np.linspace(10, 100, 12)
print(D)

E = np.random.rand(4, 5)
print(E)

F = np.random.randint(1, 9, (4, 5))
print(F)

G = np.concatenate((E, F), axis=0)
print(G)