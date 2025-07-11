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
        
    def insertar_sublista(self):
        valor1 = input("Ingrese el primer valor del dato: ")
        valor2 = input("Ingrese el segundo valor del dato: ")
        dato_numero = [valor1, valor2] 
        posicion = int(input("Digite la posición donde desea insertar el dato: "))
        objLista.insertar_dato(posicion, dato_numero)
        return posicion
       
    def añadir_sublista(self, dato_numero):
        objLista.incluir_lista([dato_numero]) 
        
    def eliminar_Numero(self):
        posicion = int(input("Ingresa la posicion a eliminar (0-{}): ".format(len(objLista.lista_numero)-1)))
        elemento_eliminado =objLista.eliminar_dato(posicion)
        return elemento_eliminado
    
    def mostrar_elemento(self, posicion):
        posicion = int(input("Ingresa la posicion a ver (0-{}): ".format(len(objLista.lista_numero)-1)))
        elemento = objLista.lista_numero[posicion]
        print(f"La posición {posicion} es: {elemento}")
        return elemento
    
    def busqueda_por_indice(sublista):
        sublista=(input("Digite los valores excatos de la lista a buscar: "))
                
#Codigo Principal
objCalculadora=Calculadora()

print("Bienvenido, seleccione la opcion a realizar: ")

while True:
    

        print("Selecciona '1' para guardar numeros en una lista. ")
        print("Selecciona '2' para insertar sublista en posicion especifica. " )
        print("Selecciona '3' para agregar una sublista a la lista existente. ")
        print("Selecciona '4' para Eliminar una sublista. ")
        print("Seleccione '5' para ver una sublista especifica. ")
        opcion=(input("Seleccione una opcion: "))
        
        match opcion:
            
            case "1":
                opcion=='1'
                auxnum1, auxnum2=objCalculadora.pedir_numero() 
                objCalculadora.almacenar_numero(auxnum1,auxnum2)
                
            case "2":
                opcion=='2'
                auxPosicion=objCalculadora.insertar_sublista()
                
            case "3":
                opcion=='3'
                dato_numero=objCalculadora.pedir_numero()
                objCalculadora.añadir_sublista([dato_numero])
                
            case "4":
                opcion=='4'
                objCalculadora.eliminar_Numero()
                
            case "5":
                opcion=='5'
                objCalculadora.mostrar_elemento()
        
        
        
    