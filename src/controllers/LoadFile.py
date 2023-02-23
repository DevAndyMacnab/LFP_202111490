def LoadFile(FileDirection):
    loadFile=open(FileDirection,"r", encoding="utf-8")
    content=loadFile.read()
    content=content.split("\n")

    
    movies=[]
    for line in content:
        splittedLine=line.split(";")
        actorsList=splittedLine[1].strip().split(",")
        
        
        movies.append({
            "Pelicula":splittedLine[0].strip(),
            "Actores":actorsList,
            "Año":splittedLine[2].strip(),
            "Categoria":splittedLine[3].strip()
            
        })
    
    print("Archivo Cargado correctamente")
     
    #Testing
    indexArrays=[]
    
    for i, element in enumerate(movies):
       nameMovie=element["Pelicula"]
       
       for j in range(len(movies)):
           if i==j:
               continue
           elif nameMovie== movies[j]["Pelicula"] and i!=j and j not in indexArrays:
               indexArrays.append(i)
                     
    #Esta variable almacena el indexArray sin los elementos repetidos
    newSet=set(indexArrays)
    
    #Invierte la lista de index que debe borrar para posteriormente comenzar a borrarlos de la lista de peliculas
    for x in sorted(newSet, reverse=True):
        del movies[x]
    
    #-----
    loadFile.close()
    return movies




