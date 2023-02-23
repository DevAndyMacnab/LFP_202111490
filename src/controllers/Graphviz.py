import os
data = '''
digraph main {
    graph [pad="0.5", nodesep="0.5", ranksep="2"];
    node [shape=plain]
    rankdir=LR;\n
'''

iteracion = 0
iteracion_2 = 1

peliculas = {
    'Avengers': 
    {
        'Actores':['Robert Dw. Jr', 'Chris Hermswor', 'Chris Evans', 'Mark Bufalo'], 
        'Anio': 2012, 
        'Genero': 'Accion'
    }, 
    'Spiderman Homecoming':
    {
        'Actores':['Robert Dw. Jr', 'Tom Holland', 'Zendaya'],
        'Anio':2016,
        'Genero':'Accion'
    }, 
    'Spiderman No Way Home':
    {
        'Actores':['Robert Dw. Jr', 'Tom Holland', 'Zendaya'],
        'Anio': 2018,
        'Genero': 'Accion'
    }, 
    'Avengers Infinity War':
    {
        'Actores':['Robert Dw. Jr', 'Chris Hermswor', 'Chris Evans'], 
        'Anio': 2018,
        'Genero': 'Accion'
    },
    'Thor Ragnarok':
    {
        'Actores':['Chris Hermswor', 'Mark Bufalo'],
        'Anio': 2017,
        'Genero': 'Accion'
    }}

actores = ['Robert Dw. Jr', 'Chris Hermswor', 'Chris Evans', 'Mark Bufalo', 'Tom Holland', 'Zendaya']

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

def agregar_estilo():
    data += 'node [shape=box, style=filled, fillcolor="#00c853"]\n'

# Aqui creamos los nodos de peliculas
for pelicula in peliculas.keys():
    anio = peliculas[pelicula]['Anio']
    genero = peliculas[pelicula]['Genero']
    nodo =crear_nodo(pelicula, anio, genero)
    data += nodo

# Aqui agregamos el estilo a los nodos de actores
data += 'node [shape=box, style=filled, fillcolor="#00c853"]'
# Aqui creamos los nodos de actores
for actor in actores:
    nodo = crear_actor(actor)
    data += nodo

# Aqui creamos las relaciones
for pelicula in peliculas.keys():
    for actor in peliculas[pelicula]['Actores']:
        relacion = crear_relacion(iteracion_2,actor)
        data += relacion
    iteracion_2 += 1
    
data += '}'

# Aqui creamos el archivo
with open('dataGraphic.dot', 'w') as f:
    f.write(data)

# Aqui creamos la imagen
os.system('dot -Tpdf dataGraphic.dot -o dataGraphic.pdf')


