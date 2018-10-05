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

# conexión a la base de datos #
cliente = pymongo.MongoClient()

# Base de datos: MovieDB #
db = cliente.escuelaMusica

def mostrarTodos():
    estu = db.estudiantes.find()
    for document in estu:
        pprint(document)



#-----Consultas-----#
