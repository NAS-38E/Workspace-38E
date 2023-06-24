class Cancion:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

class Nodo:
    def __init__(self, cancion):
        self.cancion = cancion
        self.siguiente = None
        self.anterior = None

class ListaReproduccion:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar_cancion(self, cancion):
        nuevo_nodo = Nodo(cancion)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo

    def mostrar_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.cancion.titulo + " - " + nodo_actual.cancion.artista)
            nodo_actual = nodo_actual.siguiente

# Ejemplo de uso
print("Mi lista de reproducción:")
mi_lista = ListaReproduccion()
mi_lista.agregar_cancion(Cancion("Love Sosa", "Chief Keef"))
mi_lista.agregar_cancion(Cancion("Self Love", "Metro Boomin, Coi Leray"))
mi_lista.agregar_cancion(Cancion("Rich Flex", "Drake, 21 Savage"))
mi_lista.mostrar_lista()