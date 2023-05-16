import numpy as np
import random

##Multiplicacion de matrices con numpy

##Para m1

filasm1 = int(input("el numero de filas es: "))
columnasm1 = int(input("el numero de columnas es: "))
m1 = []

for i in range(filasm1):
    m1.append ([0] * columnasm1)

for i in range(filasm1): 
    for j in range (columnasm1):
     m1 [i][j]= float((random.randint(1,5)))
print(f"\n primera matriz {m1}")
m1_np = np.array(m1)

#Para m2
filasm2 = int(input("El numero de filas es :"))
columnasm2 = int(input("El numero de columnas es: "))

m2= []
for i in range(filasm2):
   m2.append ([0] * columnasm2)

for i in range(filasm2):
   for j in range (columnasm2):
      m2[i][j] = float((random.randint(1,5)))
print(f"\n segunda matriz {m2}")
m2_np = np.array(m2)

if columnasm1 == filasm2:
   matriz_mult = np.matmul(m1_np,m2_np)
   print(f"\n El resultado es : {matriz_mult} ") ##np.matmul multiplica las matrices
else: 
   print ("No se pueden multiplicar las columnas ")