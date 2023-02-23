from src.controllers.Graphviz import createGraphic

class Movies:
    def __init__(self,listMovies):
        self.listMovies=listMovies
        
        
    def filterByActor(self, actorName):
        countdown=0
        actorName=actorName
        for element in self.listMovies:
            if actorName in element["Actores"]:
                countdown+=1
                print("PELICULA:",element["Pelicula"])
        if countdown==0:
            print("No se encontro el ACTOR que ha ingresado... \n")
            return False
        else:
            print("--------------------------------")
            return True
        
    def filterByYear(self,yearInput):
        countdown=0
        yearInput=yearInput
        for element in self.listMovies:
            if yearInput in element["Año"]:
                countdown+=1
                print("PELICULA:",element["Pelicula"], "| CATEGORIA: " , element["Categoria"])
        if countdown==0:
            print("El año ingresado no posee peliculas en nuestra base de datos...")
            return False
        else:
            print("--------------------------------")
            return True
        
    def filterByGenre(self,genreName):
        countdown=0
        genreName=genreName
        for element in self.listMovies:
            if genreName in element["Categoria"]:
                countdown+=1
                print("PELICULA:",element["Pelicula"])
        if countdown==0:
            print("No se encontró la CATEGORIA que ha ingresado...")
            return False
        else:
            print("--------------------------------")
            return True
        
    
    
    def getData(self):
        countdown=0
        listCopy=self.listMovies.copy()
        for element in self.listMovies:
            countdown+=1
            print(countdown ,"PELICULA:",element["Pelicula"] ,"| ACTORES:",element["Actores"] ,"| AÑO:",element["Año"] ,"| CATEGORIA:",element["Categoria"])
            print("--------------------------------")    
        
        return listCopy
    
    
    def showActors(self):
        countdown=0
        for element in self.listMovies:
            countdown+=1
            print(countdown ,"PELICULA:",element["Pelicula"] )
            print("--------------------------------") 
        try:    
            option=int(input("Seleccione el numero de la pelicula... "))
            print("Los actores de la pelicula seleccionada son: ")
            
            
        
        
            for element in self.listMovies[option-1]["Actores"]:
                print(element)
        except:
            print("ERROR: EL VALOR INGRESADO NO ES VALIDO!!!")
            
            
    def graphicData(self):
        actors=[]
        for element in self.listMovies:
            for actor in element["Actores"]:
                actors.append(actor)
        actors=set(actors)
        
        createGraphic(self.listMovies,actors)