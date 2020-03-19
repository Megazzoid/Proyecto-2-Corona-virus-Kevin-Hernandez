from Candidato import *       #Se importan todas las clases de candidato
from modulo2 import *         #Se importan todas las funciones de modulo2
lista_3 = []
lista_1 = []           #Estas listas son lista globales para mas adelante almacenar los datos de los pacientes y despues enseñar los datos en una funcion
lista_2 = []
import sys         #se importa sys para terminar el programa en ciertos caos

#------------------------------------------------------------------------Funcion--------------------------------------------------------------------------------
def Modulo1():
    Acumulador = 0

    print("Hola porfavor rellene los los siguientes datos:")

    nombre = input("Ingrese Su nombre Completo")  #Se ingresa el nombre completo del panciente

    bloqueo = True                   
    while bloqueo == True:
                edad= input("Porfavor diga su edad")   #Se ingresa la edad del paciente
                try:
                    edad=int(edad)                                   #Se verifica si la edad es valida o no
                    bloqueo= False
                    break
                except ValueError:
                    print ("Porfavor introdusca una edad valida")
                


    print("A continuacion se la hara unas preguntas para conocer su situacion actual:")  #Se comienzan hacer las preguntas para saber si el usuario
                                                                                         #Es No infecta , infectado o en revision
   
    bloqueo = True 
    while bloqueo == True:  #Un while para asegurarnos que el paciente responda correctamente  la pregunta 1
        Secreciones = input("¿Ha tenido secreciones nasales? Escriba si o no en minuscula")
        if Secreciones == "si":
            bloqueo = False
            Acumulador = Acumulador + 1   #La variable acumulador es para saber cuantos sintomas lleva el paciente
        elif Secreciones == "no":
            bloqueo = False
        else:
            print("Error: Porfavor escriba si o no")

    bloqueo = True
    while bloqueo == True:  #Un while para asegurarnos que el paciente responda correctamente  la pregunta 2
        Dolor_garganta = input("¿Tienes dolor de garganta? Escriba si o no en minuscula")
        if Dolor_garganta == "si":
            bloqueo = False
            Acumulador = Acumulador + 1
        elif Dolor_garganta == "no":
            bloqueo = False
        else:
            print("Error: Porfavor escriba si o no")

    bloqueo = True
    while bloqueo == True: #Un while para asegurarnos que el paciente responda correctamente  la pregunta 3
        Tos = input("¿Tienes Tos? Escriba si o no en minuscula")
        if Tos == "si":
            bloqueo = False
            Acumulador = Acumulador + 1
        elif Tos == "no":
            bloqueo = False
        else:
            print("Error: Porfavor escriba si o no en minuscula")

    bloqueo = True
    while bloqueo == True: #Un while para asegurarnos que el paciente responda correctamente  la pregunta 4
        fiebre = input("¿Tienes fiebre?? Escriba si o no en minuscula")
        if fiebre == "si":
            bloqueo = False
            Acumulador = Acumulador + 1
        elif fiebre == "no":
            bloqueo = False
        else:
            print("Error: Porfavor escriba si o no")

    bloqueo = True
    while bloqueo == True: #Un while para asegurarnos que el paciente responda correctamente  la pregunta 5
        respirar = input("¿Esta  teniendo dificultad para respirar?? Escriba si o no")
        if respirar == "si":
            bloqueo = False
            Acumulador = Acumulador + 1
        elif respirar == "no":
            bloqueo = False
        else:
            print("Error: Porfavor escriba si o no") 


    print("Procesando Datos!")  #Dependiendo de cuantos sintomas registro la variable acumulador el paciente es REGISTRADO como infectado, no infectado o posible infectado

    if Acumulador == 0:
        print("Usted ha sido clasificado como persona no infectada para terminar rellene este dato final:") #Se le piden unos datos adicionales si es no infectados
        bloqueo = True                   
        while bloqueo == True:  #Nos aseguramos que el paciente responda correctamente si pone un dato malo
            telefono= input("Porfavor introdusca su numero de telefono")  
            try:
                telefono=int(telefono)
                if len(str(telefono)) > 12:
                    print("ERRO: Porfavor introdusca un telefono valido")  
                else:
                    bloqueo = False
                break
            except ValueError:
                    print ("ERROR: porfavor introdusca un telefono valido")
        lista_1.append(No_infectado(nombre,edad,telefono))    #Se suben los datos a la lista global de no infectados
        return No_infectado(nombre,edad,telefono) #Se retorna en forma de clase los datos
        

                    


                    

    elif Acumulador == 1:
        print("Usted ha sido clasificado como persona EN REVISION para terminar rellene este dato final") #Se piden datos adicionales si es registrado como persona en revision
        bloqueo = True                   
        while bloqueo == True: #Usamos un while para asegurarnos que registre bien los datos el paciente
            telefono= input("Porfavor introdusca su numero de telefono")  
            Pais = input("Ingrese un Pais")

        print("-----------------subiendo Datos A la base de datos-------------------------------------")    

        print("Sus Datos han sido subidos a la base de datos para ver la base de datos regrese al menu")    

        lista_1.append(No_infectado(nombre,edad,telefono))   #Se suben los datos a la lista de no infectado
        return No_infectado(nombre,edad,telefono)   #Se retorna los datos en forma de clase
        
        


    elif Acumulador > 1 and Acumulador < 5: # Se clasifica la persona Como posible infectados y se le piden datos adicionales
        print("Usted ha sido clasificado como POSIBLE INFECTADO para terminar rellene estos datos finales")

        direccion = input("Porfavor ingrese la direccion donde vive")
        
        cuidad = input("Porfavor introdusca la Cuidad donde vive")                 #Le pedimos unos datos adicionales
        
        estado = input("Porfavor introdusca El estado donde vive")
        print("-----------------subiendo Datos A la base de datos-------------------------------------")

        
        print("Sus Datos han sido subidos a la base de datos para ver la base de datos regrese al menu")  


        lista_2.append(Posible_infectado(nombre,edad,cuidad,direccion,estado))  #Se suben los datos a la lista de Posible infectados
        return Posible_infectado(nombre,edad,cuidad,direccion,estado)  #Devolvemos los datos en forma de clase

        


    elif Acumulador == 5: #Se clasifica la persona como infectada

        print("Usted ha sido clasificado como INFECTADO para terminar rellene estos datos finales")

        direccion = input("Porfavor ingrese la direccion donde vive")
        
        cuidad = input("Porfavor introdusca la cuidad donde vive") #Se le piden datos adicionales

        estado = input("Porfavor introdusca el estado donde vive")             

        medico = input("Porfavor ingrese el nombre completo del medico tratante") 
        print("-----------------subiendo Datos A la base de datos-------------------------------------")

        
        print("Sus Datos han sido subidos a la base de datos para ver la base de datos regrese al menu")  


        lista_3.append(Infectado(nombre,edad,cuidad,direccion,estado,medico)) # Se suben sus datos a la lista de infectados   
        return Infectado(nombre,edad,cuidad,direccion,estado,medico)  # Se devuelven los datos en forma de clase

def MenuPrincipal(): # Menu principal que conecta todos las funciones para que corra el programa
    

    bloqueo_inicial=True 

    while bloqueo_inicial == True: #Utilizamos un while para que el programa se repita si es que lo desea el usuario
        print("-------------------------------------------------------------------------------------------------------------")
        bloqueador = True                  
        while bloqueador == True: #Utiizamos aqui otro while para se repita la primera parte del menu si lo desea el usuario
            #Le pedimos al usuario que seleccione una opcion
            seleccion= input('''¿Qué operación desea realizar? 
 1 - Registrar un infectado
 2 - Ver pacientes registrados en este formulario     
 3 - Ver Estadisticas Globales
 Seleccione 1/2/3
''')
            try:
                seleccion=int(seleccion)  #Verificamos si el usuario introduce un numero valido 
                bloqueo = False
                break
            except ValueError:
                print ("ERROR: porfavor introdusca un numero valido")
        
        if seleccion == 1: #Si la seleccion es 1 llamamos la funcion del modulo 1 para registrar un usuario
            print("------------------------------------------------------------------------------------------------------------------------------------------------")
            Modulo1()
            bloqueo = True                   
            while bloqueo == True: #usamos un while para saber si el paciente quiere seguir usando el programa o salir
                print("----------------------------------------------------------------------------------------------------------------------------")
                seleccion= input('''
1 -Salir del programa
2 -Volver Al menu
Seleccione 1/2''')  
                try:
                    seleccion=int(seleccion)  #Nos aseguramos que ponga una opcion valida
                    if seleccion == 1:
                        bloqueo= False
                        bloqueo_inicial = False
                        print("Adios!")
                        sys.exit()
                    elif seleccion == 2:
                        bloqueo = False
                        break
                except ValueError:
                        print ("ERROR: porfavor introdusca un numero valido")

        elif seleccion == 2: # Aqui revisamos los datos registrados en la lista 
            print("------------------------------------------------------------------------------------------------------------------------------------------------")
            while bloqueador == True: #un while para que el usuario seleccione la lista que desea ver y nos aseguramos que eliga una opcion correcta
                seleccionnn= input('''¿Qué operación desea realizar?
    1 - Ver NO INFECTADOS
    2 - Ver POSIBLES INFECTADOS
    3 - ver INFECTADOS
    Seleccione 1/2/3
    ''')
                try:
                    seleccionnn=int(seleccionnn)
                    bloqueo = False
                    break
                except ValueError:
                    print ("ERROR: porfavor introdusca un numero valido")
            if seleccionnn == 1:         # si la seleccion es 1 revisamos la lista de no infectados 
                bloqueo = True 
                if len(lista_1) > 0: 
                    h = 0                      #con un for se revisan los datos de la lista de no infectados 
                    for buscar in lista_1:
                        z= 1 + h
                        print("-------------------",z,"--------------------------------")
                        print(buscar.informacion()) #Llamando a la clase con su funcion se imprimen los datos
                        h = h + 1  
                else:
                    print("-----------------------------------------------------------")
                    print("Todavia no hay personas registradas") 
                while bloqueo == True:
                    print("----------------------------------------------------------------------------------------------------------------------------")
                    seleccionn= input('''     
 -Escriba 1  para salir del programa
 -Escriba cualquier otra tecla para volver Al menu principal ''') # Se revisa si el usuario quiere salir del programa o seguir usandolo

                    
                    if seleccionn == "1":
                        bloqueo= False
                        bloqueador = False
                        bloqueo_inicial = False
                        print("Adios!")
                        sys.exit()
                        
                    else:
                        bloqueo= False
                        bloqueador = False
                        break
                        
                    

                
            elif seleccionnn == 2: # Se revisan los datos de la lista posibles infectados 
                    bloqueo = True
                    if len(lista_2) > 0:
                        h = 0  
                        for buscar2 in lista_2: #Se abren los datos de la lista posibles infectados con un for
                            z= 1 + h
                            print("-------------------",z,"--------------------------------")
                            print(buscar2.informacion2()) #Se imprimen los datos llamando la clase y la funcion
                            h = h + 1 
                    else:
                        print("-----------------------------------------------------------")
                        print("Todavia no hay personas registradas")                       
                    while bloqueo == True:
                        print("----------------------------------------------------------------------------------------------------------------------------")
                        seleccionn= input('''
 -Escriba 1  para salir del programa 
 -Escriba cualquier otra tecla para volver Al menu principal ''') # El usuario eliga la opcion si quiere salir o seguir usando el programa

                        if seleccionn == "1":
                            bloqueo= False
                            bloqueador = False
                            bloqueo_inicial = False
                            print("Adios!")
                            sys.exit()
                            
                            
                        else:
                            bloqueo= False
                            bloqueador = False
                            break
                        
                           

                        
            elif seleccionnn == 3: #Se leera y escribiran los datos de la lista de infectados
                    bloqueo = True  
                    if len(lista_3) > 0: 
                        h= 0
                        for buscar3 in lista_3: #Se abre la lista a traves de un for
                            z= 1 + h
                            print("-------------------",z,"--------------------------------")
                            print(buscar3.informacion3()) # Se imprimen los datos de la lista a traves llamando la clase y su funcion
                            h = h + 1  
                    else:
                        print("-----------------------------------------------------------")
                        print("Todavia no hay personas registradas")                 
                    while bloqueo == True:
                        print("----------------------------------------------------------------------------------------------------------------------------")
                        seleccionn= input('''
 -Escriba 1  para salir del programa
 -Escriba cualquier otra tecla para volver Al menu principal ''')  # A traves de este while el paciente decide si seguir usando el programa o salir 

                        if seleccionn == "1":
                            bloqueo= False
                            bloqueador = False
                            bloqueo_inicial = False
                            print("Adios!")
                            sys.exit()
                        
                        else:
                            bloqueo= False
                            bloqueador = False 
                            break
            else:
                    print("ERROR: seleccione una opcion valida")                                  

        elif seleccion == 3: # Se revisan las estadisticas globales llamando la funcion modulo que contiene todas las funciones relacionadas a las estadisticas
            print("------------------------------------------------------------------------------------------------------------------------------------------------")
            Modulo2_index()
            bloqueo = True   

        else:
            print("ERROR: seleccione una opcion valida")
    


MenuPrincipal() #Se llama la funcion del menu principal para comenzar el programa