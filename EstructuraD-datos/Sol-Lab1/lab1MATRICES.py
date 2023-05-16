import numpy as np
def suma(m1, m2):
    m_final_suma = np.add(m1, m2)
    return m_final_suma

def resta(m1, m2):
    m_final_resta = np.subtract(m1,m2)
    return m_final_resta

filas = int(input("ingrese la cantidad de filas de la matriz: "))
columnas = int(input("ingrese la cantidad de columnas de la matriz: "))

## Ingresar elementos matriz 1
print("ingresando los elementos de la matriz 1: ")
m1= np.zeros((filas,columnas))
for i in range (filas):
    for j in range (columnas):
        elem = int(input(f"ingrese el elemento [{i}] [{j}]: "))
        m1[i] [j]= elem

## Ingresar elementos matriz 2
print("\ningresando los elementos de la matriz 2: ")
m2= np.zeros((filas,columnas))
for i in range (filas):
    for j in range (columnas):
        elem = int(input(f"ingrese el elemento [{i}] [{j}]: "))
        m2[i] [j]= elem

## Suma matrices
m_final_suma = suma(m1, m2)
print("\nLa matriz resultado de la suma es: ")
print(m_final_suma)

## Resta matrices
m_final_resta = resta(m1, m2)
print("\nLa matriz resultado de la resta es: ")
print(m_final_resta)





