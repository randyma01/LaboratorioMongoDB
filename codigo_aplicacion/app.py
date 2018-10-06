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
    2. Declaración de funciones auxiliares de uso global.
    3. Desarrollo de la interfaz gráfica.

Nota:
    El siguiente código corresponde únicamente a la parte de la
    aplicación (UI).
----------------------------------------------------------------------
"""
#-------------------------------------------------------------------#
#-----------------------Bilbiotecas Utilizadas----------------------#
#-------------------------------------------------------------------#

# Libreria para la Interfaz Gr[afica #
import tkinter
from tkinter import *
from tkinter import messagebox

# Librería para utilizar los recursos del OS #
import os

# Librería de la Conexión y control de la Parte de MongoDB #
# (este archivo corresponde a la otra parte del laboratrio #
# y se encuentre en este mismo folder )                    #
from connection import *

#-------------------------------------------------------------------#
#----------------------Funciones Auxiliares-------------------------#
#-------------------------------------------------------------------#

# Cargar Imagenes #
def cargarImagen(nombre):
    ruta = os.path.join('imagenes',nombre)
    imagen = PhotoImage(file=ruta)
    return imagen

# Terminar el Programa #
def salida():
    return exit

#-------------------------------------------------------------------#
#--------------------------Parte Grafica----------------------------#
#-------------------------------------------------------------------#

#-----Ventana de Consultas-----#
def ventanaConsultas():
    ventanaPrincipal.withdraw()
    ventanaConsultas = Toplevel()
    ventanaConsultas.title("Consulta Películas a MovieDB")
    ventanaConsultas.minsize(800,550)
    ventanaConsultas.resizable(width=NO,height=NO)

    # Canva Consultas #
    contenedorConsultas = Canvas(ventanaConsultas , width= 1000, height = 800, bg = "#000000")
    contenedorConsultas.place(x=0,y=0)

    # Titulo Consultas #
    tituloConsultas = Label(ventanaConsultas,text="Ejecute sus Consultas", fg="#FFFFFF", bg ="#000000", font=("Courier",40))
    tituloConsultas.place(x=150,y=25)

    #----Opciones de Consulta----#

    #--Consultar Pelicula por Nombre--#
    infoPeliculaNombre = Label(ventanaConsultas,text="-> Consultar película por nombre: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaNombre.place(x=25,y=100)
    entradaNombre = Entry(ventanaConsultas, width=10, bg = "#FFFFFF")
    entradaNombre.place(x=400,y=100)

    # Función que Recopila los Datos e Invoca la Función que Ejecuta la Consulta#
    def ejecutarConsultaNombre():
        temp = str(entradaNombre.get())
        res = consultarPeliculaNombre(temp)
        messagebox.showinfo("Información de la Película",res)
        
    botonConsultaNombre = Button(ventanaConsultas, command=ejecutarConsultaNombre, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaNombre.place(x=570,y=100)
    

    #--Consultar Pelicula por Franquicia--#
    infoPeliculaFranquicia = Label(ventanaConsultas,text="-> Consultar película por franquicia: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaFranquicia.place(x=25,y=150)
    entradaFranquicia = Entry(ventanaConsultas, width=10, bg = "#FFFFFF")
    entradaFranquicia.place(x=440,y=150)

    # Función que Recopila los Datos e Invoca la Función que Ejecuta la Consulta#
    def ejecutarConsultaFranquicia():
        temp = str(entradaFranquicia.get())
        res = consultarPeliculaFranquicia(temp)
        messagebox.showinfo("Información de la Película",res)
        
    botonConsultaFranquicia = Button(ventanaConsultas, command=ejecutarConsultaFranquicia, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaFranquicia.place(x=570,y=150)

    #--Consultar Pelicula por Años--#
    infoPeliculaAhnos = Label(ventanaConsultas,text="-> Consultar película por año: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaAhnos.place(x=25,y=200)
    entradaAhnos1 = Entry(ventanaConsultas, width=5, bg = "#FFFFFF")
    entradaAhnos1.place(x=370,y=200)
    entradaAhnos2 = Entry(ventanaConsultas, width=5, bg = "#FFFFFF")
    entradaAhnos2.place(x=440,y=200)

    # Función que Recopila los Datos e Invoca la Función que Ejecuta la Consulta#
    def ejecutarConsultaAhnos():
        temp1 = entradaAhnos1.get()
        temp2 = entradaAhnos2.get()
        print(temp1,temp2)
        res = consultarPeliculaAhnos(temp1, temp2)
        print(res)
        messagebox.showinfo("Información de la Película",res)
        
    botonConsultaAhno= Button(ventanaConsultas, command=ejecutarConsultaAhnos, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaAhno.place(x=570,y=200)

    #--Consultar Pelicula por productora--#
    infoPeliculaProductora = Label(ventanaConsultas,text="-> Consultar película por productora: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaProductora.place(x=25,y=250)
    entradaProductora = Entry(ventanaConsultas, width=10, bg = "#FFFFFF")
    entradaProductora.place(x=440,y=250)

    # Función que Recopila los Datos e Invoca la Función que Ejecuta la Consulta#
    def ejecutarConsultaProductora():
        temp = str(entradaProductora.get())
        res = consultarPeliculaProductora(temp)
        messagebox.showinfo("Información de la Película",res)

    botonConsultaProductora= Button(ventanaConsultas, command=ejecutarConsultaProductora, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaProductora.place(x=570,y=250)

    #--Consultar Duracion Minima--#
    infoPeliculaDuracionMinima = Label(ventanaConsultas,text="-> Consultar información de la duración minima ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaDuracionMinima.place(x=25,y=300)

    # Función que Invoca la Función que Ejecuta la Consulta#
    def ejecutarConsultaDuracionMin():
        res = consultarDuracionMinima()
        messagebox.showinfo("Información de la Película",res)
        
    botonConsultaDuracionMinima= Button(ventanaConsultas, command=ejecutarConsultaDuracionMin, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaDuracionMinima.place(x=570,y=300)

    #--Consultar Duracion Maxima--#
    infoPeliculaDuracionMaxima = Label(ventanaConsultas,text="-> Consultar información de la duración maxima ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaDuracionMaxima.place(x=25,y=350)

    # Función que Invoca la Función que Ejecuta la Consulta#
    def ejecutarConsultaDuracionMax():
        res = consultarDuracionMaxima()
        messagebox.showinfo("Información de la Película",res)
        
    botonConsultaDuracionMaxima= Button(ventanaConsultas, command=ejecutarConsultaDuracionMax, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaDuracionMaxima.place(x=570,y=350)

    #--Consultar Duracion Promedio--#
    infoPeliculaDuracionPromedio = Label(ventanaConsultas,text="-> Consultar información de la duración promedio ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaDuracionPromedio.place(x=25,y=400)

    # Función que Invoca la Función que Ejecuta la Consulta#
    def ejecutarConsultaDuracionProm():
        res = consultarDuracionPromedio()
        messagebox.showinfo("Información de la Película",res)
        
    botonConsultaDuracionPromedio= Button(ventanaConsultas, command=ejecutarConsultaDuracionProm, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaDuracionPromedio.place(x=570,y=400)
    #----------------------------#

    # Funcion para regresar a Ventana Principal 
    def regresarVentanaPrincipal():
        ventanaConsultas.destroy()
        ventanaPrincipal.deiconify()

    # Boton para regresar a la Ventana Principal #
    botonReresoVentanaPrincipal = Button(ventanaConsultas, command=regresarVentanaPrincipal, text="REGRESAR", bg="#FFFFFF", fg="GREEN", font=("Courier",28))
    botonReresoVentanaPrincipal.place(x=355,y=450)
#------------------------------#


#-----Ventana de Inserciones-----#
def ventanaInsertar():
    ventanaPrincipal.withdraw()
    ventanaInsertar = Toplevel()
    ventanaInsertar.title("Insertar Películas a MovieDB")
    ventanaInsertar.minsize(800,660)
    ventanaInsertar.resizable(width=NO,height=NO)

    # Canva Inserciones #
    contenedorConsultas = Canvas(ventanaInsertar, width= 1000, height = 800, bg = "#000000")
    contenedorConsultas.place(x=0,y=0)

    # Titulo Insertar #
    tituloConsultas = Label(ventanaInsertar,text="¡Inserte una nueva película!", fg="#FFFFFF", bg ="#000000", font=("Courier",40))
    tituloConsultas.place(x=50,y=25)

    # Indicaciones para Insertar los Datos de las Películas
    nombrePelicula= Label(ventanaInsertar,text="-> Nombre de la película: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    nombrePelicula.place(x=25,y=100)
    entradaNombre = Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaNombre.place(x=300,y=100)

    nombreDirector= Label(ventanaInsertar,text="-> Nombre del director: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    nombreDirector.place(x=25,y=150)
    entradaDirector = Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaDirector.place(x=300,y=150)

    franquicia= Label(ventanaInsertar,text="-> Franquicia (si aplica): ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    franquicia.place(x=25,y=200)
    entradaFranquicia = Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaFranquicia.place(x=330,y=200)

    pais= Label(ventanaInsertar,text="-> País: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    pais.place(x=25,y=250)
    entradaPais = Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaPais.place(x=130,y=250)

    genero= Label(ventanaInsertar,text="->Género de la película: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    genero.place(x=25,y=300)
    entradaGenero = Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaGenero.place(x=300,y=300)

    estreno= Label(ventanaInsertar,text="-> Año de estreno: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    estreno.place(x=25,y=350)
    entradaEstreno = Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaEstreno.place(x=250,y=350)
    
    duracion= Label(ventanaInsertar,text="-> Duración (min): ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    duracion.place(x=25,y=400)
    entradaDuracion = Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaDuracion.place(x=250,y=400)

    productora= Label(ventanaInsertar,text="-> La principal productora: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    productora.place(x=25,y=450)
    entradaProductora = Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaProductora.place(x=330,y=450)

    actores= Label(ventanaInsertar,text="-> Tres actores principales: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    actores.place(x=25,y=500)
    entradaActorUno = Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaActorUno.place(x=350,y=500)
    entradaActorDos= Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaActorDos.place(x=470,y=500)
    entradaActorTres = Entry(ventanaInsertar, width=10, bg = "#FFFFFF")
    entradaActorTres.place(x=590,y=500)

    # Función que Recopila los Datos y los manda al a Función que los Inserta #
    def ejecutarInsercionPelicula():
        nombre = str(entradaNombre.get())
        director = str(entradaDirector.get())
        franquicia = str(entradaFranquicia.get())
        pais = str(entradaPais.get())
        genero = str(entradaGenero.get())
        estreno = entradaEstreno.get()
        duracion = entradaDuracion.get()
        productora = str(entradaProductora.get())
        actorUno = str(entradaActorUno.get())
        actorDos = str(entradaActorDos.get())
        actorTres = str(entradaActorTres.get())
        listaActores = []
        listaActores.append(actorUno)
        listaActores.append(actorDos)
        listaActores.append(actorTres)
        print(nombre,director,genero,franquicia,pais,estreno,duracion,productora,listaActores)
        insertarPelicula(nombre,director,genero,franquicia,pais,estreno,duracion,productora,listaActores)

    botonInsertarPelicula= Button(ventanaInsertar, command=ejecutarInsercionPelicula, text="Guardar", bg="#FFFFFF", fg="#000000", font=("Courier",28))
    botonInsertarPelicula.place(x=600,y=300)
    #----------------------------#

    # Funcion para regresar a Ventana Principal #
    def regresarVentanaPrincipal():
        ventanaInsertar.destroy()
        ventanaPrincipal.deiconify()

    # Boton para regresar a la Ventana Principal #
    botonReresoVentanaPrincipal = Button(ventanaInsertar, command=regresarVentanaPrincipal, text="REGRESAR", bg="#FFFFFF", fg="GREEN", font=("Courier",28))
    botonReresoVentanaPrincipal.place(x=355,y=600)

#--------------------------------#

#-----Ventana de Eliminaciones-----#
def ventanaEliminar():
    ventanaPrincipal.withdraw()
    ventanaEliminar = Toplevel()
    ventanaEliminar.title("Eliminar Películas a MovieDB")
    ventanaEliminar.minsize(900,300)
    ventanaEliminar.resizable(width=NO,height=NO)

    # Canva Inserciones #
    contenedorEliminar = Canvas(ventanaEliminar, width= 1000, height = 800, bg = "#000000")
    contenedorEliminar.place(x=0,y=0)

    # Titulo Insertar #
    tituloEliminar = Label(ventanaEliminar,text="¡Elimine una película colección!", fg="#FFFFFF", bg ="#000000", font=("Courier",40))
    tituloEliminar.place(x=50,y=25)

    #--Eliminar Pelicula por Nombre--#
    eliminadoNombre = Label(ventanaEliminar,text="-> Elimine película por nombre: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    eliminadoNombre.place(x=25,y=100)
    entradaNombre = Entry(ventanaEliminar, width=10, bg = "#FFFFFF")
    entradaNombre.place(x=400,y=100)

    # Función que Elimina una Película #
    def ejecutarEliminadoPelicula():
        temp = str(entradaNombre.get())
        eliminarPelicula(temp)
        
    botonEliminarPelicula = Button(ventanaEliminar, command=ejecutarEliminadoPelicula, text="Eliminar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonEliminarPelicula.place(x=570,y=100)

    #--Eliminar Todas las Películas--#
    eliminadoTotal = Label(ventanaEliminar,text="-> Elimine todas las películas: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    eliminadoTotal.place(x=25,y=150)

    # Función que Elimina todas las Películas #
    def ejecutarEliminadoTotal():
        eliminarTodo()
    
    botonEliminarPelicula = Button(ventanaEliminar, command=ejecutarEliminadoTotal, text="Eliminar", bg="#FFFFFF", fg="#FE0000", font=("Courier",18))
    botonEliminarPelicula.place(x=400,y=150)
    #----------------------------#

    # Funcion para regresar a Ventana Principal #
    def regresarVentanaPrincipal():
        ventanaEliminar.destroy()
        ventanaPrincipal.deiconify()

    # Boton para regresar a la Ventana Principal #
    botonReresoVentanaPrincipal = Button(ventanaEliminar, command=regresarVentanaPrincipal, text="REGRESAR", bg="#FFFFFF", fg="GREEN", font=("Courier",28))
    botonReresoVentanaPrincipal.place(x=355,y=250)
#----------------------------------#


#-----Ventana de Actualizaciones-----#
def ventanaActualizar():
    ventanaPrincipal.withdraw()
    ventanaActualizar = Toplevel()
    ventanaActualizar.title("Actualizar una Películas de MovieDB")
    ventanaActualizar.minsize(850,200)
    ventanaActualizar.resizable(width=NO,height=NO)

    # Canva Inserciones #
    contenedorActualizar= Canvas(ventanaActualizar, width= 1000, height = 800, bg = "#000000")
    contenedorActualizar.place(x=0,y=0)

    # Titulo Insertar #
    tituloEliminar = Label(ventanaActualizar,text="¡Elimine una película colección!", fg="#FFFFFF", bg ="#000000", font=("Courier",40))
    tituloEliminar.place(x=50,y=25)

    #--Eliminar Pelicula por Nombre--#
    eliminadoNombre = Label(ventanaActualizar,text="-> Actualice el nombre de una película: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    eliminadoNombre.place(x=25,y=100)
    
    entradaNombreOriginal = Entry(ventanaActualizar, width=10, bg = "#FFFFFF")
    entradaNombreOriginal.place(x=460,y=100)

    entradaNombreNuevo = Entry(ventanaActualizar, width=10, bg = "#FFFFFF")
    entradaNombreNuevo.place(x=580,y=100)

     # Función que Actualiza el Nombre de una Películas #
    def ejecutarActualizacionNombre():
        original = str(entradaNombreOriginal.get())
        nuevo = str(entradaNombreNuevo.get())
        actualizarPelicula(original,nuevo)

    botonActualizarPelicula = Button(ventanaActualizar, command=ejecutarActualizacionNombre, text="Acualizar", bg="#FFFFFF", fg="BLUE", font=("Courier",22))
    botonActualizarPelicula.place(x=690,y=100)
     #----------------------------#

    # Funcion para regresar a Ventana Principal #
    def regresarVentanaPrincipal():
        ventanaActualizar.destroy()
        ventanaPrincipal.deiconify()

    # Boton para regresar a la Ventana Principal #
    botonReresoVentanaPrincipal = Button(ventanaActualizar, command=regresarVentanaPrincipal, text="REGRESAR", bg="#FFFFFF", fg="GREEN", font=("Courier",28))
    botonReresoVentanaPrincipal.place(x=355,y=150)
#------------------------------------#

#-----Ventana Principal-----#
ventanaPrincipal = Tk()
ventanaPrincipal.title("MovieDB")
ventanaPrincipal.minsize(800,600)
ventanaPrincipal.resizable(width=NO,height=NO)
ventanaPrincipal.geometry("800x600+250+50")

# Canva Principal #
contenedorPrincipal = Canvas(ventanaPrincipal , width= 800, height = 700, bg = "#000000")
contenedorPrincipal.place(x=0,y=0)

# Imagen de Fondo Ventana Principal #
imagenPrincipal = cargarImagen("entrada_cine.gif")
imagenVentanaPrincipal=Label(ventanaPrincipal, image=imagenPrincipal, bg = "#FFFFFF")
imagenVentanaPrincipal.place (x=0, y=0)

# Titulo Ventana Principal #
tituloPrincipal = Label(ventanaPrincipal,text="MovieDB", fg="#000000", bg ="#FFFFFF", font=("Courier",55))
tituloPrincipal.place(x=285,y=95)

# Boton para ir a Ventana de Consultas #
botonConsultas = Button(ventanaPrincipal, command=ventanaConsultas, text="Consultas", bg = "#000000", fg = "#000000", font=("Courier",30))
botonConsultas.place(x=315,y=225)

# Boton para ir a Ventana de Insertar #
botonInsertar = Button(ventanaPrincipal, command=ventanaInsertar, text="Insertar", bg = "#000000", fg = "#000000", font=("Courier",30))
botonInsertar.place(x=325,y=275)

# Boton para ir a Ventana de Actualizar #
botonActualizar = Button(ventanaPrincipal, command=ventanaActualizar, text="Actualizar", bg = "#000000", fg = "#000000", font=("Courier",30))
botonActualizar.place(x=305,y=325)

# Boton para ir a Ventana de Eliminar #
botonInsertar = Button(ventanaPrincipal, command=ventanaEliminar, text="Eliminar", bg = "#000000", fg = "#000000", font=("Courier",30))
botonInsertar.place(x=325,y=375)

# Boton para terminar del Programar #
botonSalida = Button(ventanaPrincipal, command=salida(), text="SALIDA", bg="#FFFFFF", fg="#FE0000", font=("Courier",28))
botonSalida.place(x=345,y=475)

