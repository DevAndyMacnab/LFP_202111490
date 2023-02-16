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
    return movies

