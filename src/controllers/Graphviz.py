iteracion = 0

def crear_nodo(pelicula, anio, genero):
    global iteracion
    iteracion += 1
    return f'''\nnodo{iteracion} [label=<
    <table border="0" cellborder="1" cellspacing="0">
    <tr><td bgcolor="#0091ea" port="p1" colspan="2">{pelicula}</td></tr>
    <tr><td> {anio} </td><td> {genero} </td></tr>
    </table>>];\n\n'''

def crear_actor(actor):
    return f'\t"{actor}"\n' # Eso lo pueden omitir xd
    

def crear_relacion(nodo,actor):
    return f'''\tnodo{nodo}:p1 -> "{actor}";\n'''


def createGraphic(movies,actors):
    
    import os
    data = '''
    digraph main {
        graph [pad="0.5", nodesep="0.5", ranksep="2"];
        node [shape=plain]
        rankdir=LR;\n
    '''
    
    iteracion_2 = 1
    # Aqui creamos los nodos de peliculas

    for pelicula in movies:
        anio = pelicula["Año"]
        genero = pelicula["Categoria"]
        movie=pelicula["Pelicula"]
        nodo =crear_nodo(movie, anio, genero)
        data += nodo

    # Aqui agregamos el estilo a los nodos de actores
    data += 'node [shape=box, style=filled, fillcolor="#00c853"]'
    # Aqui creamos los nodos de actores
    for actor in actors:
        nodo = crear_actor(actor)
        data += nodo

    # Aqui creamos las relaciones
    for pelicula in movies:
        for actor in pelicula['Actores']:
            relacion = crear_relacion(iteracion_2,actor)
            data += relacion
        iteracion_2 += 1
        
    data += '}'

    # Aqui creamos el archivo
    with open('dataGraphic.dot', 'w') as f:
        f.write(data)

    # Aqui creamos la imagen
    os.system('dot -Tpdf dataGraphic.dot -o dataGraphic.pdf')


