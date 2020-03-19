def top_infectados(): #funcion para revisar top infectados 
    import requests

    afectados = {}

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",  # Se recibe la key para entrar al api
        'x-rapidapi-key': "19f5cfad3fmshf610a87091b967fp1fc159jsn0406ee9d5d92"
        }

    response = requests.request("GET", url, headers=headers, params=querystring) #Nos conectamos al api

    dic = response.json() #guardamos los datos del api 

    import operator

    for i in range(len(dic['data']['covid19Stats'])):  #Con un for agregamos en un nuevo diccionario los datos: Paises y sus cantidad de infectados
        afectados[dic['data']['covid19Stats'][i]['country']] = dic['data']['covid19Stats'][i]['confirmed']

    afectados["China"] = dic['data']['covid19Stats'][0]['confirmed']    
    afectados = dict(sorted(afectados.items(), key=operator.itemgetter(1)), reverse=True) # Se ordena de menor a mayor la lista 

    from collections import Counter  #Se importa collecitions para crear el top 10

    k = Counter(afectados) 
    
    # Finding 3 highest values 
    Top = k.most_common(10)  # Se agarran los top 10 datos mayores infectados
    
    
    print("Top 10 Paises Con Mas infectados:") 

    for i in Top: 
        print(i[0],":",i[1]," ")  #Se imprimen los top 10 paises con mas infectados

#-------------------------------------------------Siguiente funcion ----------------------------------------------------------------------------------------

def top_muertes():

    import requests

    afectados = {}

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",  
        'x-rapidapi-key': "19f5cfad3fmshf610a87091b967fp1fc159jsn0406ee9d5d92" #Recibimos la key para ingresar al api
        }

    response = requests.request("GET", url, headers=headers, params=querystring) # Nos conectamos al api 

    dic = response.json() #guardamos los datos de la api

    import operator

    for i in range(len(dic['data']['covid19Stats'])): # A traves de un for guardamos en un nuevo diccinario los datos: Paises y cantidad de mueres
        afectados[dic['data']['covid19Stats'][i]['country']] = dic['data']['covid19Stats'][i]['deaths'] 

    afectados["China"] = dic['data']['covid19Stats'][0]['deaths']    
    afectados = dict(sorted(afectados.items(), key=operator.itemgetter(1)), reverse=True) # Ordenamos de menor a mayor

    from collections import Counter #se abre collecions y importar counter para conseguir el top 10

    k = Counter(afectados) 
    
    
    Top = k.most_common(10)  
    
    
    print("Top 10 Paises con mas muertes:") 

    for i in Top: 
        print(i[0],":",i[1]," ") # Se imprime el top 10 muertes
  #-----------------------------------------------------------------------------------Otra funcion----------------------------------------------------------------      

def Top_recuperados(): # Funcion para conseguir el top 10 paises con mas pacientes recuperados

    import requests

    afectados = {}

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "19f5cfad3fmshf610a87091b967fp1fc159jsn0406ee9d5d92" # Se consigue la key para ingresar a la api
        }

    response = requests.request("GET", url, headers=headers, params=querystring) # Nos conectamos al api

    dic = response.json() #Guardamos los datos de la api 

    import operator

    for i in range(len(dic['data']['covid19Stats'])): #En un for agregamos en un nuevo diccionario los paises y su cantidad de recuperados 
        afectados[dic['data']['covid19Stats'][i]['country']] = dic['data']['covid19Stats'][i]['recovered']

    afectados["China"] = dic['data']['covid19Stats'][0]['recovered']    
    afectados = dict(sorted(afectados.items(), key=operator.itemgetter(1)), reverse=True) # Ordenamos de menor a mayor el diccionario 

    from collections import Counter #importamos counter para ordenar el top 10 
    k = Counter(afectados) 
    
    
    Top = k.most_common(10)  
    
    
    print("Top 10 Paises con mas recuperados:") 

    for i in Top: 
        print(i[0],":",i[1]," ")  # Se impriemen el top 10 paises con mas recuperados 

# ------------------------------------------------------------Funcion--------------------------------------------------------------------------------------------

def lista1():  #Esta funcion es solo para guardar los nombres de todos los paises en un diccionario 
    
    import requests

    lista = {}

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":""}

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "19f5cfad3fmshf610a87091b967fp1fc159jsn0406ee9d5d92" #Recibimos la key
        }

    response = requests.request("GET", url, headers=headers, params=querystring) #Nos conectamos al api

    dic = response.json() #Guardamos en un diccionario los datos 

    import operator 

    for i in range(len(dic['data']['covid19Stats'])):  #A traves de un for guardamos los datos en un diccionario
        lista[dic['data']['covid19Stats'][i]['country']] = dic['data']['covid19Stats'][i]['recovered']

    return lista #regresamos el diccionario 

# ---------------------------------------------------------------------Funcion-------------------------------------------------------------------------------
def paisEspecifico(): #Funcion para regresar datos de un pais especifico
    d= lista1() #Guardamos el diccionario que nos regresa la funcion lista1()
    bloqueo = True
    while bloqueo == True:  #Un while para que el usuario ingrese el pais correctamente
        Pais = input("Ingrese un Pais (ESCRIBA LA PRIMERA LETRA DEL PAIS EN MAYUSCULA):")
        try:
            Probar = d[Pais]
            bloqueo = False
            break
        except:
            print ("ERROR: Escriba un pais valido")

        
    import requests

    url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/stats"

    querystring = {"country":Pais} #Buscamos en la api el pais que queremos revisar

    headers = {
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
    'x-rapidapi-key': "19f5cfad3fmshf610a87091b967fp1fc159jsn0406ee9d5d92" # Recibimos la key del api
    }

    response = requests.request("GET", url, headers=headers, params=querystring) #Nos conectamos al api 

    dic = response.json() #guardamos los datos que nos regreso la api

    Cantidad_Infectados = dic['data']['covid19Stats'][0]['confirmed'] # guardamos la cantidad de infectados 
    
    print("Cantidad de infectados de" ,Pais, ":",Cantidad_Infectados) # Imprimimos la cantidad de infectados 

    Cantidad_Recuperados = dic['data']['covid19Stats'][0]['recovered'] # Guardamos la cantidad de recuperados 
    
    print("Cantidad de recuperados de" ,Pais, ":",Cantidad_Recuperados) # Imprimimos la cantidad de recuperados 

    Cantidad_Muertos = dic['data']['covid19Stats'][0]['deaths'] # Guardamos la cantidad de muertes

    print("Cantidad de muertos de" ,Pais, ":",Cantidad_Muertos) # imprimimos la cantidad de muertes 

  
# -----------------------------------------------------------------Funcion------------------------------------------------------------------------------------

def Modulo2_index(): # Funcion para crear el menu de las estadisticas globales
    Bloqueo_final = True
    while Bloqueo_final == True: #
            bloqueador = True                  
            while bloqueador == True: #  un while para asegurarnos que el usuario eliga la opcion correcta de las siguientes opciones que le mostramos 
                print("--------------------------------------------------------------------------------------------------------------------------------------")
                seleccion= input('''¿Qué operación desea realizar?
    1 - Revisar cantidad De infectados,muertos,recuperados de un pais
    2 - Ver top 10 paises Infectados
    3 - Ver top 10 paises Recuperados
    4 - Ver top 10 paises Muertos
    5 - Regresar al menu principal
    Seleccione 1/2/3/4/5
    ''')
                try:
                    seleccion=int(seleccion)
                    bloqueador = False
                    break
                except ValueError:
                    print ("ERROR: porfavor introdusca un numero valido")
            
            if seleccion == 1: # Si elige la seleccion 1 llamamos la funcion pais especifico para enseñar los datos del pais que quiera
                print("------------------------------------------------------------------------------------------------------------------------------------------------")
                print("CARGANDO PORFAVOR ESPERE")
                paisEspecifico()
                bloqueo = True                   
                while bloqueo == True:
                    print("-------------------------------------------------------------------------------------------------------------")
                    seleccion= input('''
1 -Volver al menu principal
2 -Volver Al menu de estadisticas
Seleccione 1/2''')  
                    try:
                        seleccion=int(seleccion) # Revisamos si el usuario quiere volver al menu principal o al menu de estadisticas
                        if seleccion == 1:
                            bloqueo= False
                            Bloqueo_final = False
                        if seleccion == 2:
                            bloqueo = False
                        break
                    except ValueError:
                            print ("ERROR: porfavor introdusca un numero valido")

            elif seleccion == 2: #llamamos la funcion top infectados para ver el top 10 paises infectados 
                print("------------------------------------------------------------------------------------------------------------------------------------------------")
                print("CARGANDO PORFAVOR ESPERE")
                top_infectados()
                bloqueo = True                   
                while bloqueo == True:
                    print("-------------------------------------------------------------------------------------------------------------")
                    seleccion= input('''
1 -Volver al menu principal
2 -Volver Al menu de estadisticas
Seleccione 1/2''')  
                    try:
                        seleccion=int(seleccion) # Revisamos que opcion eligio el usuario y nos aseguramos que eligio una opcion que funcione
                        if seleccion == 1:
                            bloqueo= False
                            Bloqueo_final = False
                        if seleccion == 2:
                            bloqueo = False
                        break
                    except ValueError:
                            print ("ERROR: porfavor introdusca un numero valido")

            elif seleccion == 3: # llamamos la funcion top recuperados para revisar el top 10 paises con mas recuperados 
                print("------------------------------------------------------------------------------------------------------------------------------------------------")
                print("CARGANDO PORFAVOR ESPERE")
                Top_recuperados()
                bloqueo = True                   
                while bloqueo == True:
                    print("-------------------------------------------------------------------------------------------------------------")
                    seleccion= input('''
1 -Volver al menu principal
2 -Volver Al menu de estadisticas
Seleccione 1/2''')  
                    try:
                        seleccion=int(seleccion) # Revisamos que el usuario eligio una opcion que funcione
                        if seleccion == 1:
                            bloqueo= False
                            Bloqueo_final =False
                        if seleccion == 2:
                            bloqueo = False
                        break
                    except ValueError:
                            print ("ERROR: porfavor introdusca un numero valido")

            elif seleccion == 4: #llamamos la funcion topmuertes para mostrar los top 10 paises con mas muertes
                print("------------------------------------------------------------------------------------------------------------------------------------------------")
                print("CARGANDO PORFAVOR ESPERE")
                top_muertes()
                bloqueo = True                   
                while bloqueo == True:
                    print("-------------------------------------------------------------------------------------------------------------")
                    seleccion= input('''
1 -Volver al menu principal
2 -Volver Al menu de estadisticas
Seleccione 1/2''')  
                    try:
                        seleccion=int(seleccion) #revisamos que seleccion eligio el usuario y si eligio una opcion correcta
                        if seleccion == 1:
                            bloqueo= False
                            Bloqueo_final = False
                        if seleccion == 2:
                            bloqueo == False
                        break
                    except ValueError:
                            print ("ERROR: porfavor introdusca un numero valido")
            elif seleccion == 5:
                Bloqueo_final = False
            else:
                print("ERROR: seleccione una opcion valida") 












