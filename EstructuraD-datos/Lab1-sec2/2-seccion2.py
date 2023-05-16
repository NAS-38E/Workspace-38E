##Ejercicio 2
import random

filas = int(input("Ingrese la cantidad de filas de la matriz: "))
columnas = int(input("Ingrese la cantidad de columnas de la matriz: "))
escalar = int(input("Ingrese un escalar: "))

a = []
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(random.randint(0,10))
    a.append(fila)

##Multiplicacion por el escalar
    for i in range(filas):
        fila = []
        for j in range(columnas):
            a[i][j]*=escalar
##Imprimir Resultado
print(f'\nMultiplicación de matriz por el escalar: ')
for fila in a:
    print(fila)
##Codigo realizado por Alex Hernandez y Nicolas Almuna 
