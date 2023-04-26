##Ejercicio 1
import random

filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
def matriz(filas,columnas):
    a = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(random.randint(0,5))
    a.append(fila)
    return a
def suma(m,m2):
    mf = []
    for i in range(len(m)):
        fila = []
        for j in range(len(m[0])):
            suma = m[i][j] + m2[i][j]
            fila.append(suma)
        mf.append(fila)
    return mf

def resta(m,m2):
    mf = []
    for i in range(len(m)):
        fila = []
        for j in range(len(m[0])):
            res = m[i][j] - m2[i][j]
            fila.append(res)
        mf.append(fila)
    return mf

m = matriz(filas,columnas)
print(f"\nMatriz 1:")
for fila in m:
    print(fila)

m2 = matriz(filas,columnas)
print(f"\nMatriz 2:")
for fila in m2:
    print(fila)

m_final = suma(m, m2)
print(f"\nSuma matrices (1+2): ")
for fila in m_final:
    print(fila)

m3 = matriz(filas,columnas)
print(f"\nMatriz 3:")
for fila in m3:
    print(fila)

m_final = resta(m_final, m3)
print(f"\nResta matrices (1+2-3): ")
for fila in m_final:
    print(fila)
##Codigo realizado por Alex Hernandez y Nicolas Almuna 
