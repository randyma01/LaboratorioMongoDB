"""
----------------------------------------------------------------------

Area Academica de Administracion de Tecnologia de Informacion

Curso:
    Bases de Datos Avanzados

Tarea:
    Laboratorio MongoDB

Fecha:
    7 de octubre, 2018
    Semestre II

Estudiante:
	Randy Martinez Sandi

Carnet: 2014047395

Herramientas Utilizadas:
    -Python 3.0.7
    -tkinter
    -pymongo
----------------------------------------------------------------------
"""
#-------------------------------------------------------------------#
#-----------------------Bilbiotecas Utilizadas----------------------#
#-------------------------------------------------------------------#
import tkinter
from tkinter import *
from tkinter import messagebox
import pymongo
import os

#-------------------------------------------------------------------#
#------------------------Parte de MongoDB---------------------------#
#-------------------------------------------------------------------#


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
    ventanaConsultas.title("Consultas a MovieDB")
    ventanaConsultas.minsize(800,500)
    ventanaConsultas.resizable(width=NO,height=NO)

    # Imagen de Fondo Ventana Consultas #
    imagenConsultas = cargarImagen("sala_cine.gif")
    imagenVentanaConsultas=Label(ventanaConsultas, image=imagenConsultas, bg = "#000000")
    imagenVentanaConsultas.place (x=0, y=0)

    # Canva Consultas #
    contenedorConsultas = Canvas(ventanaConsultas , width= 1000, height = 600, bg = "#000000")
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

    def ejecutarConsultaNombre():
        temp = str(entradaNombre.get())
        print (temp)
        #messagebox.showinfo("Mensaje leido en el entry",str(entradaNombre.get()))
        #print ("Mensaje leido:"+entradaNombre.get())
        
    botonConsultaNombre = Button(ventanaConsultas, command=ejecutarConsultaNombre, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaNombre.place(x=570,y=100)
    

    #--Consultar Pelicula por Franquicia--#
    infoPeliculaFranquicia = Label(ventanaConsultas,text="-> Consultar película por franquicia: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaFranquicia.place(x=25,y=150)
    entradaFranquicia = Entry(ventanaConsultas, width=10, bg = "#FFFFFF")
    entradaFranquicia.place(x=440,y=150)
    botonConsultaFranquicia = Button(ventanaConsultas, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaFranquicia.place(x=570,y=150)

    #--Consultar Pelicula por Franquicia--#
    infoPeliculaAhnos = Label(ventanaConsultas,text="-> Consultar película por año: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaAhnos.place(x=25,y=200)
    entradaAhnos1 = Entry(ventanaConsultas, width=5, bg = "#FFFFFF")
    entradaAhnos1.place(x=370,y=200)
    entradaAhnos2 = Entry(ventanaConsultas, width=5, bg = "#FFFFFF")
    entradaAhnos2.place(x=440,y=200)
    botonConsultaAhno= Button(ventanaConsultas, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaAhno.place(x=570,y=200)

    #--Consultar Pelicula por Compañía--#
    infoPeliculaCompania = Label(ventanaConsultas,text="-> Consultar película por compañía: ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaCompania.place(x=25,y=250)
    entradaCompania = Entry(ventanaConsultas, width=10, bg = "#FFFFFF")
    entradaCompania.place(x=430,y=250)
    botonConsultaCompania= Button(ventanaConsultas, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaCompania.place(x=570,y=250)

    #--Consultar Duracion Peliculas--#
    infoPeliculaDuracion = Label(ventanaConsultas,text="-> Consultar información de la duración ", fg="#FFFFFF", bg ="#000000", font=("Courier",18))
    infoPeliculaDuracion.place(x=25,y=300)
    botonConsultaDuracion= Button(ventanaConsultas, text="Consultar", bg="#FFFFFF", fg="#000000", font=("Courier",18))
    botonConsultaDuracion.place(x=570,y=300)


    #----------------------------#


    # Funcion para regresar a Ventana Principal 
    def regresarVentanaPrincipal():
        ventanaConsultas.destroy()
        ventanaPrincipal.deiconify()

    # Boton para regresar a la Ventana Principal #
    botonReresoVentanaPrincipal = Button(ventanaConsultas, command=regresarVentanaPrincipal, text="SALIDA", bg="#FFFFFF", fg="#FE0000", font=("Courier",28))
    botonReresoVentanaPrincipal.place(x=355,y=400)


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

# Boton para terminar del Programar #
botonSalida = Button(ventanaPrincipal, command=salida(), text="SALIDA", bg="#FFFFFF", fg="#FE0000", font=("Courier",28))
botonSalida.place(x=345,y=275)

