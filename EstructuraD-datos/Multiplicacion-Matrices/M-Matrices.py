import random

filas = int(input("numero de filas"))
columnas = int(input("Numero de columnas"))
def matriz(filas,columnas):
    a = []
    for i in range(filas):
        fila = []
    for j in range (columnas):
         fila.append(random.randint(0,10))
    a.append(fila)
    return a

def suma(a,b):
    c = []
    for i in range (len(a)):
       fila = []
       for j in range(len(a[0])):
           suma = a[i][j] + b[i][j]
           fila.append(suma)
    c.append(fila)
    return c

def matrix_multiply(a, b):
    c = [[] for _ in range(len(a))]
    for i in range(len(a)):        
        for j in range(len(a)):
            sum = 0
            for k in range(len(a)):
                sum += a[i][k] * b[k][j]
            c[i].append(sum)
    return c

a = matriz(filas, columnas)
print (f"\n matriz")
for fila in a:
 print(fila)

 b = matriz(filas,columnas)
 print (f"\n matriz 2")
 for fila in b:
  print(fila)

m_final = suma(a,b)
print (f"\n suma")
for fila in m_final:
   print(fila)

m3 = matriz(filas,columnas)
print (f"\n m3")
for fila in m3:
 print(fila)

m_final = matrix_multiply(m3)
print (f"\n final resultado")
for fila in m_final:
   print(fila)





