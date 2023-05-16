import random
##Parte 1 sin librerias
filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))

m1 = []
m2 = []
m3 = []

for i in range(filas):
    m1.append([random.randint(1, 5) for j in range(columnas)])
    m2.append([random.randint(1, 5) for j in range(columnas)])
    m3.append([0] * columnas)

for i in range(filas):
    for j in range(columnas):
        m3[i][j] = m1[i][j] + m2[i][j]

print("Matriz 1:")
for i in range(filas):
    print(m1[i])

print("Matriz 2:")
for i in range(filas):
    print(m2[i])

print("Matriz resultante:")
for i in range(filas):
    print(m3[i])

##Parte 2 utilizando la libreria numpy
import numpy as np 

m3 = np.array([m3])

escalar = int(input("ingrese un escalar entero del 1 al 10: "))
if escalar < 1 or escalar > 10:
    print("El número ingresado no está dentro del rango permitido.")
else:
    m_resultante = m3 * escalar

print("La matriz resultante es: ")
print(m_resultante)

##Parte 3 utilizando libreria numpy 
import numpy as np
filasm4 = int(input("Ingrese la cantidad de filas: "))
columnasm4 = int(input("Ingrese la cantidad de columnas: "))
m4 = []
m_resultante = np.array([m_resultante])

resultado = np.matmul(m_resultante, m4)

print("El resultado de la multiplicacion de matrices es: ")
print(resultado)