import numpy as np

#1) Calcular el determinante de una matriz 3x3 con elementos aleatorios del (5 a 10)
mat1 = np.random.randint(5, 11, size=(3, 3))
det = np.linalg.det(mat1)
print(f"Determinante de la matriz: {det}")
