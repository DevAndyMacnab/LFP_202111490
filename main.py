#Importacion de modulos de funciones
from src.controllers.LoadFile import LoadFile
from src.classes.Movies import Movies



#LoadFile(fileDirection)
print('''Lenguajes Formales y de Programacion
        Seccion B+
        Carnet: 202111490
        Nombre: Andy Roberto Jimenez Macnab''')
input("Ingrese cualquier tecla....")
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
    fileDirection="./src/static/archivo prueba.lfp"
    fileRequet=LoadFile(fileDirection)
print(fileRequet)
print("--------------")
movies=Movies(fileRequet)

    

