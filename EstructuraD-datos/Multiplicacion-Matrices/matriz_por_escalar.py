import random

filas_matriz_uno = int(input("Introduzca el número de filas para su primera matriz: "))
columnas_matriz_uno = int(input("Introduzca el número de columas para su primera matriz: "))


# Matriz uno

matriz_uno = []

for i in range(filas_matriz_uno):
	matriz_uno.append( [0] * columnas_matriz_uno)
	
for i in range(filas_matriz_uno):
	for j in range(columnas_matriz_uno):
		matriz_uno[i][j] = float((random.randint(1,5)))
		
print(f"Primera matriz {matriz_uno}")

# Matriz uno por escalar k

mult_matriz_k = []

k = int(input("Ingrese el número escalar: "))
for i in range(filas_matriz_uno):
    mult_fila = []
    for j in range(columnas_matriz_uno):
        mult_fila.append(matriz_uno[i][j] * k)
    mult_matriz_k.append(mult_fila)

# Resultado

print(f"La multiplicación de {k} por {matriz_uno} es {mult_matriz_k}")