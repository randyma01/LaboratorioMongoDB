#Se importan todas las bibliotecas necesarias para poder trabajar
from tkinter import *           #Biblioteca para interfaces gráficas
import time                     #Biblioteca que interactúa con la hora del S.O.
import random                   #Biblioteca para generar salidas de forma aleatoria
import os                       #Biblioteca que permite interactuar con el sistema operativo
import winsound                 #Biblioteca necesaria para reproducir audios de windows
import pygame                   #Biblioteca necesaria para la parte lógica del juego
from tkinter import messagebox

from Game import *


#Carga de imagenes
def CargarImagen(Nombre):
    ruta    = os.path.join('Imagenes',Nombre)   #Busca la imagen dentro del sistema operativo
    imagen  = PhotoImage(file=ruta)
    return imagen

def cerrarPrincipal():
    VentanaPrincipal.destroy()
    winsound.PlaySound(None, winsound.SND_ASYNC)


#Creación de la ventana principal
VentanaPrincipal = Tk()
VentanaPrincipal.title("Ticopoly")               #Se añade un título a la ventana principal
VentanaPrincipal.minsize(900,650)                #Se establece un tamaño mínimo para la ventana
VentanaPrincipal.maxsize(900,650)                #Se establece un tamaño máximo para la ventana
VentanaPrincipal.resizable(width=YES,height=YES)   #Se establece que la ventana no sea expandible
