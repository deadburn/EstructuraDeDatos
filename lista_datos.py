class Lista_numeros:
    def __init__(self):
        self.lista_numero=[]
        
    def guardar_numero(self, dato_numero):
        self.lista_numero.append(dato_numero)
        print(self.lista_numero)
        
    def incluir_lista(self, dato_numero):
        self.lista_numero.extend(dato_numero)
        print(self.lista_numero)
        
    def insertar_dato(self,posicion, dato_numero):
        self.lista_numero.insert(posicion, dato_numero)
        print(self.lista_numero)

    
    def eliminar_dato(self, posicion):
       elemento_eliminado= self.lista_numero.pop(posicion)
       print(f"La lista {self.lista_numero} ha sido actualizada")
       print(f"El elemento {elemento_eliminado} ha sido eliminado")
       return elemento_eliminado
    
    def buscarPorIndice(self, sublista):
        indice=self.lista_numero.index(sublista)
        return indice
        
        
    
    
        
    