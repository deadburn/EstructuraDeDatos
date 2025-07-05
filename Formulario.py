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
        posicion =int(input("Digite la posicion del dato "))
        objLista.insertar_dato(posicion)
        return posicion
        
#Codigo Principal

objCalculadora=Calculadora()

auxnum1, auxnum2=objCalculadora.pedir_numero() 
objCalculadora.almacenar_numero(auxnum1,auxnum2)

auxnum1, auxnum2=objCalculadora.pedir_numero() 
objCalculadora.almacenar_numero(auxnum1,auxnum2)


auxPosicion=objCalculadora.insertar_Numero()






