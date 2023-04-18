import numpy as np

# Solicitar cantidad de filas y columnas
filas = int(input("Ingrese la cantidad de filas de las matrices: "))
columnas = int(input("Ingrese la cantidad de columnas de las matrices: "))

# Inicializar las matrices con ceros
matrix1 = np.zeros((filas, columnas))
matrix2 = np.zeros((filas, columnas))

# Añadir elementos a la matriz 1
print("Ingrese los elementos de la matriz 1:")
for i in range(filas):
    for j in range(columnas):
        matrix1[i][j] = float(input(f"Elemento ({i},{j}): "))

print("Ingrese los elementos de la matriz 2:")
for i in range(filas):
    for j in range(columnas):
        matrix2[i][j] = float(input(f"Elemento ({i},{j}): "))

        # Función para sumar las matrices
def sum_matrices(matrix1, matrix2):
    matrix1+matrix2
    return np.add(matrix1, matrix2)

# Función para restar las matrices
def resta_matrices(matrix1, matrix2):
    matrix1-matrix2
    return np.subtract(matrix1, matrix2)

# Ejemplo de uso
result_sum = sum_matrices(matrix1, matrix2)
result_subtract = resta_matrices(matrix1, matrix2)

print("Matriz 1:")
print(matrix1)
print("Matriz 2:")
print(matrix2)
print("Resultado de la suma:")
print(result_sum)
print("Resultado de la resta:")
print(result_subtract)

