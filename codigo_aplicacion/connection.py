"""
----------------------------------------------------------------------

Área Académica de Administración de Tecnología de Información

Curso:
    Bases de Datos Avanzados - TI4601

Tarea:
    Laboratorio MongoDB

Fecha:
    7 de octubre, 2018
    Semestre II

Estudiante:
	Randy Martínez Sandí

Carnet: 2014047395

Índice:
    1. Importación de la librerías utilizadas.
    2. Declaración de funciones y variables a utilizar. 

Nota:
    El siguiente código corresponde únicamente a la parte de la
    conexión, manejo y control de la base datos (lógica).

----------------------------------------------------------------------
"""
#-------------------------------------------------------------------#
#-----------------------Bilbiotecas Utilizadas----------------------#
#-------------------------------------------------------------------#

# Librería para la conexión entre MongoDB y Python3 #
import pymongo

# Librería para mostra los resultados de manera bonita #
from pprint import pprint

#-------------------------------------------------------------------#
#----------------------Variables y Funciones------------------------#
#-------------------------------------------------------------------#

# Conexión a la Base de Datos #
cliente = pymongo.MongoClient()

# Base de Datos: MovieDB #
db = cliente.movieDB

#-------------------------------------------------------------------#
#---------------------------------CRUD------------------------------#
#-------------------------------------------------------------------#

#-----Consultas-----#

# Consultar toda la Información de una Película por su Nombre #
def consultarPeliculaNombre(nombre):
    pipeline = ({"nombrePelicula": nombre})
    cursor = db.peliculas.find(pipeline)
    infoPelicula = list(cursor)
    pprint(infoPelicula)
    return infoPelicula
    
# Consultar toda la Información de todas las Pelícuals de una Franquicia #
def consultarPeliculaFranquicia(nombre):
    pipeline = ({"franquicia": nombre})
    cursor = db.peliculas.find(pipeline)
    infoPelicula = list(cursor)
    pprint(infoPelicula)
    return infoPelicula


# Consultar la información de una película estrenada en un rango de años #
def consultarPeliculaAhnos(anUno,anDos):
    print(anUno,anDos)
    pipeline = ({"estreno" : {"$gt": anUno, "$lt": anDos}})
    cursor = db.peliculas.find(pipeline)
    infoPelicula = list(cursor)
    for document in infoPelicula:
        pprint(document)
    return infoPelicula

# Consultar nombre, género, estreno de las peliculas producidas por una #
# por una productar en particular #
def consultarPeliculaProductora(productora):
    cursor = db.peliculas.find({"productora": productora}, {"nombrePelicula": 1, "genero": 1, "estreno":1, "_id": 0})
    infoPelicula = list(cursor)
    for document in infoPelicula:
        pprint(document)
    return infoPelicula


# Consultar la Película con Menor Duración #
def consultarDuracionMinima():
    cursor = db.peliculas.find({}, {"nombrePelicula": 1, "duracion": 1, "_id": 0}).sort("duracion",1).limit(1)
    duracionMinima = list(cursor)
    for document in duracionMinima:
        pprint(document)
    return duracionMinima


# Consultar la Película con Mayor Duración #
def consultarDuracionMaxima():
    cursor = db.peliculas.find({}, {"nombrePelicula": 1, "duracion": 1, "_id": 0}).sort("duracion",-1).limit(1)
    duracionMaxima = list(cursor)
    for document in duracionMaxima:
        pprint(document)
    return duracionMaxima
        
# Consultar la Duración Promedio de las Películas #
def consultarDuracionPromedio():
    pipeline = [{"$group": {"_id": 0, "PromedioDuracion": {"$avg": "$duracion"}}}]
    cursor = db.peliculas.aggregate(pipeline)
    duracionPromedio = list(cursor)
    for document in duracionPromedio:
        pprint(document)
    return duracionPromedio

#-------------------#

#-----Insertar------#

# Insertar una nueva Película a la Base de Datos #
def insertarPelicula(nombre,director,genero,franquicia,pais,estreno,duracion,productora,listaActores):
    db.peliculas.insert_one({
        "nombrePelicula": nombre,
        "nombreDirector": director,
        "genero": genero,
        "franquicia": franquicia,
        "pais": pais,
        "estreno": estreno,
        "duracion": genero,
	"productora": productora,
	"actores": listaActores
    })
#-------------------#

#-----Eiminar------#

# Eliminar todas las pelícualas #
def eliminarTodo():
    db.peliculas.drop()

# Borrar una Película #
def eliminarPelicula(nombre):
    pipeline = ({"nombrePelicula": nombre})
    db.peliculas.delete_one(pipeline)
#-------------------#
