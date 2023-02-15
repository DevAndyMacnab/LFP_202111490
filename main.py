#Importacion de modulos de funciones
from src.controllers.LoadFile import LoadFile
from src.classes.Movies import Movies



#Informacion general del programa
print('''Lenguajes Formales y de Programacion
        Seccion B+
        Carnet: 202111490
        Nombre: Andy Roberto Jimenez Macnab''')
input("Ingrese cualquier tecla....")


#Declaramos variables globales
fileRequest=[]
movies=""

while True:
    print("-----------------------------------------------")
    print('''Ingrese la opcion que corresponda:
        
        1.Cargar archivo de entrada
        2.Gestionar Peliculas
        3.Filtrado
        4.Graficar
        5.Salir''')
    option=input("Ingrese la opcion que desea....  ")
    

    if option == "1":
        print("Ha seleccionado cargar archivo")
        fileDirection="./src/static/archivo prueba.lfP"
        fileRequest=LoadFile(fileDirection)
        movies=Movies(fileRequest)
        
          
    elif option =="2":
        while True:

            print('''Seleccion una de las siguientes opciones
                    a. Mostrar Peliculas
                    b. Mostrar Actores
                    c. Regresar al menu principal''')
            option = input("Ingrese la letra de la opcion que desea... ")
            if option=="a":
                movies.getData()
            elif option=="b":
                movies.showActors()
            elif option=="c":
                break
    
    
    elif option=="3":
        while True:
            print('''Seleccion una de las siguientes opciones
                a. Filtrar por actor
                b. Filtrar por año
                c. Filtrar por genero
                d. Regresar al menu principal''')
            option=input("Ingrese la letra de la opcion.... ")
            if option=="a":
                print("-----------------------------------")
                actorName=input("Ingrese el nombre del actor que desea buscar... ")
                movies.filterByActor(actorName)
        
             
    elif option=="5":
        print("Saliendo del programa....")
        break
                 
        
        
    




    

