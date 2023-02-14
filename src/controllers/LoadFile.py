def LoadFile(FileDirection):
    loadFile=open(FileDirection,"r", encoding="utf-8")
    content=loadFile.read()
    content=content.split("\n")


    movies=[]
    for line in content:
        splittedLine=line.split(";")
        actorsList=splittedLine[1].split(",")
        
        movies.append({
            "Pelicula":splittedLine[0],
            "Actores":actorsList,
            "Año":splittedLine[2],
            "Categoria":splittedLine[3]
            
        })

    print("Archivo Cargado correctamente")
    return movies
