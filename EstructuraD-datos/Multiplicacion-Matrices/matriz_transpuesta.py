# (A + B)T = AT + BT
import random
import numpy as np
filas = int(input ("Introduzca el numero de filas de sus matrices: ")) # Se asume que al ser suma de matrices, estas tienen que ser de igual dimension
columnas = int(input ("Introduzca el numero de columnas de sus matrices: ")) # tanto para filas, como columnas.

matriz1 = []
matriz2 = []
matriz3 = []


for i in range (filas):
	matriz1.append( [0] * columnas)
	matriz2.append( [0] * columnas)
	matriz3.append( [0] * columnas)


for i in range(filas):
	for j in range(columnas):
		matriz1[i][j] = float((random.randint(1, 5)))
print('Su primera matriz es\n', matriz1)


for i in range(filas):
	for j in range(columnas):
		matriz2[i][j] = float((random.randint(1, 5)))
print('Su segunda matriz es\n', matriz2)

# Suma
for i in range(filas):
	for j in range(columnas):
			matriz3[i][j] = matriz1[i][j] + matriz2[i][j]


m3 = np.array(matriz3)
print(f"Su matriz suma transpuesta (A + B)T, es {np.transpose(m3)}")
m1 = np.array(matriz1)
m2 = np.array(matriz2)

m1_m2_transpose = np.transpose(m1) + np.transpose(m2)
print(f"La operación AT + BT es {m1_m2_transpose}")

print(f"Se concluye que {np.transpose(m3)} es igual a {m1_m2_transpose}")

