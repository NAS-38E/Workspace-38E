import random

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

m1 = [[random.randint(1, 5) for j in range(columnas)] for i in range(filas)]
m2 = [[random.randint(1, 5) for j in range(columnas)] for i in range(filas)]

matriz_suma = [[m1[i][j] + m2[i][j] for j in range(columnas)] for i in range(filas)]
matriz_resta = [[m1[i][j] - m2[i][j] for j in range(columnas)] for i in range(filas)]

import random

def crear_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(1, 5))
        matriz.append(fila)
    return matriz

def sumar_matrices(m1, m2):
    filas = len(m1)
    columnas = len(m1[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            suma = m1[i][j] + m2[i][j]
            fila.append(suma)
        resultado.append(fila)
    return resultado

def restar_matrices(m1, m2):
    filas = len(m1)
    columnas = len(m1[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            resta = m1[i][j] - m2[i][j]
            fila.append(resta)
        resultado.append(fila)
    return resultado

# Pedimos la cantidad de filas y columnas por consola
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

# Creamos las dos matrices aleatorias
m1 = crear_matriz(filas, columnas)
m2 = crear_matriz(filas, columnas)

# Imprimimos las matrices creadas
print("Matriz 1:")
for fila in m1:
    print(fila)

print("Matriz 2:")
for fila in m2:
    print(fila)

# Sumamos las dos matrices y mostramos el resultado
print("Matriz resultante de la suma:")
matriz_suma = sumar_matrices(m1, m2)
for fila in matriz_suma:
    print(fila)

# Restamos las dos matrices y mostramos el resultado
print("Matriz resultante de la resta:")
matriz_resta = restar_matrices(m1, m2)
for fila in matriz_resta:
    print(fila)
