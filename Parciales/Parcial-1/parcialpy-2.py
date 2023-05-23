import numpy as np

#2) Crear dos matrices 3x3 con elementos aleatorios (-5 a -10)
mat2 = np.random.randint(-10, -4, size=(3, 3))
mat3 = np.random.randint(-10, -4, size=(3, 3))
#Vondicion para que tenga las mismas condiciones
if mat2.shape[1] == mat3.shape[0]:
    # Multiplicar las dos matrices e imprimir el resultado
    result = np.matmul(mat2, mat3)
    print(f"Resultado de la multiplicación de matrices: \n{result}")

    # Multiplicar el resultado por una matriz identidad e imprimir el resultado final
    identity = np.identity(3)
    final_result = np.matmul(result, identity)
    print(f"Resultado final: \n{final_result}")
else:
    print("Las dimensiones de las matrices no son compatibles para la multiplicación.")

#Nicolas Almuna
##38E