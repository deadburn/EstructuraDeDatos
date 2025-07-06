from lista_datos import Lista_numeros
#funciones
objLista=Lista_numeros()

class Calculadora:
    
    def pedir_numero(self):
        numero1= input("Numero 1 ")
        numero2= input("Numero 2 ")
        return numero1, numero2 
        
    def almacenar_numero(self, datonum1, datonum2):
        dato_numero =[datonum1, datonum2]
        objLista.guardar_numero(dato_numero)
       
    def añadir_Lista(self, dato_numero):
        objLista.incluir_lista([dato_numero]) 
        
        
    def insertar_Numero(self):
        posicion =int(input(f"Digite la posicion para insertar la lista predefinida: "))
        objLista.insertar_dato(posicion)
        return posicion
    
    def eliminar_Numero(self):
        posicion = int(input("Ingresa la posicion a eliminar (0-{}): ".format(len(objLista.lista_numero)-1)))
        elemento_eliminado =objLista.eliminar_dato(posicion)
        return elemento_eliminado
    
    def mostrar_elemento(self, posicion):
        posicion = int(input("Ingresa la posicion a ver (0-{}): ".format(len(objLista.lista_numero)-1)))
        elemento = objLista.lista_numero[posicion]
        print(f"La posición {posicion} es: {elemento}")
        return elemento
                
#Codigo Principal

objCalculadora=Calculadora()

auxnum1, auxnum2=objCalculadora.pedir_numero() 
objCalculadora.almacenar_numero(auxnum1,auxnum2)

auxnum1, auxnum2=objCalculadora.pedir_numero() 
objCalculadora.almacenar_numero(auxnum1,auxnum2)


auxPosicion=objCalculadora.insertar_Numero()

auxEliminar=objCalculadora.eliminar_Numero() 

auxVer=objCalculadora.mostrar_elemento(auxPosicion)
