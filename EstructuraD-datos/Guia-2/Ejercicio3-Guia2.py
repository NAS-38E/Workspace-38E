import math

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
# A) Agrega un nuevo dato a la lista, este metodo crea un nuevo nodo con el dato
#y lo agrega al final de la lista enlazada simple
    def agregar_dato(self, dato):
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

# B) Calcula y devuelve la media de los datos almacenados en la lista
#este metodo recorre la lista enlazada desde la cabeza hasta el final
    def calcular_media(self):
        if not self.cabeza:
            return 0
        suma = 0
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            suma += nodo_actual.dato
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return suma / contador
    
# C) Calcula y devuelve la desviacion estandar 
#el metodo es igual al anterior
    def calcular_desviacion_estandar(self):
        if not self.cabeza:
            return 0
        media = self.calcular_media()
        suma_cuadrados = 0
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            suma_cuadrados += (nodo_actual.dato - media) ** 2
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return math.sqrt(suma_cuadrados / contador)
    
# D) Imprime la lista en pantalla
#este método recorre la lista enlazada simple desde la cabeza hasta el final e imprime cada dato.
    def imprimir_lista(self):
        if not self.cabeza:
            print("La lista está vacía")
            return
        print("Datos en la lista:")
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente

# E) verifica si la lista esta vacia
    def verificar(self):
        return not bool(self.cabeza)

# Ejemplo de uso
lista_enlazada= ListaEnlazada()
lista_enlazada.agregar_dato(1)
lista_enlazada.agregar_dato(2)
lista_enlazada.agregar_dato(3)
lista_enlazada.imprimir_lista()
print("La Media de los datos es: ", lista_enlazada.calcular_media())
print("La Desviación estándar de los datos es: ", lista_enlazada.calcular_desviacion_estandar())
print("¿La lista está vacía?", lista_enlazada.verificar())

##Nicolas Almuna, Alex Hernandez, Ignacio Soto##
