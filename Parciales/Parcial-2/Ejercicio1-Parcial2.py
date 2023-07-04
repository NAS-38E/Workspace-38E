##A) Clase Contacto, Clase ListaContactos
class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.anterior = None
        self.siguiente = None

class ListaContactos:
    def __init__(self):
        self.primero = None
        self.ultimo = None
##B) Metodo para agregar un contacto a la lista
    def agregar_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        if self.primero == None:
            self.primero = nuevo_contacto
            self.ultimo = nuevo_contacto
            nuevo_contacto.siguiente = self.primero
            nuevo_contacto.anterior = self.ultimo
        else:
            self.ultimo.siguiente = nuevo_contacto
            nuevo_contacto.anterior = self.ultimo
            nuevo_contacto.siguiente = self.primero
            self.primero.anterior = nuevo_contacto
            self.ultimo = nuevo_contacto
##C) metodo para mostrar la lista de contactos: mostrar_lista
    def mostrar_lista(self):
        if self.primero == None:
            print("La lista está vacía")
        else:
            temp = self.primero
            while temp:
                print(temp.nombre, temp.telefono, temp.email)
                temp = temp.siguiente
                if temp == self.primero:
                    break
##D) Metodo para buscar un contacto por el nombre: buscar_contacto
    def buscar_contacto(self, nombre):
        if self.primero == None:
            print("La lista está vacía")
        else:
            temp = self.primero
            while temp:
                if temp.nombre == nombre:
                    return temp
                temp = temp.siguiente
                if temp == self.primero:
                    break

##E) Método eliminar un contacto de la lista: eliminar_contacto. 
##F)Método para verificar si la lista de contacto está vacía: 
#Se puede verificar si la lista está vacía verificando si el atributo primero de la clase ListaContactos es igual a None. 
#Esto se hace en los métodos mostrar_lista, buscar_contacto y eliminar_contacto.
    def eliminar_contacto(self, nombre):
        if self.primero == None:
            print("La lista está vacía")
        else:
            temp = self.buscar_contacto(nombre)
            if temp == None:
                print("No se encontró el contacto")
            else:
                if temp == self.primero:
                    if temp.siguiente == None:
                        self.primero = None
                        self.ultimo = None
                    else:
                        siguiente_temp = temp.siguiente
                        anterior_temp = temp.anterior
                        siguiente_temp.anterior = anterior_temp
                        anterior_temp.siguiente = siguiente_temp
                        self.primero = siguiente_temp
                elif temp == self.ultimo:
                    siguiente_temp = temp.siguiente
                    anterior_temp = temp.anterior
                    siguiente_temp.anterior = anterior_temp
                    anterior_temp.siguiente = siguiente_temp
                    self.ultimo = anterior_temp
                else:
                    siguiente_temp = temp.siguiente
                    anterior_temp = temp.anterior
                    siguiente_temp.anterior = anterior_temp
                    anterior_temp.siguiente = siguiente_temp
                    
#Ejemplo
if __name__ == '__main__':
    lista_contactos = ListaContactos()
    lista_contactos.agregar_contacto('Nicolas', '56908756123', 'nicolas@alumnos.ulagos.cl')
    lista_contactos.agregar_contacto('Ana', '56976512367', 'ana@alumnos.ulagos.cl')
    lista_contactos.agregar_contacto('Gabriela', '56923561235', 'gabriela@alumnos.ulagos.cl')
    print("Lista de contactos: ")
    lista_contactos.mostrar_lista()
    lista_contactos.eliminar_contacto('Ana')
    print("Borrando a Ana de la lista de contactos")
    lista_contactos.mostrar_lista()