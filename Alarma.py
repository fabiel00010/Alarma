from tkinter import *
import time
import pygame
from pygame.locals import*
from pygame import mixer

root = Tk()
root.title("Fabiel Tonala")
pygame.init()

root.geometry("200x300")

tiempo=StringVar()

def clock3():
    horas=time.strftime("%H")
    minutos=time.strftime("%M")
    horaL= horas + ":"+ minutos 
    miEtiquetaM.after(1000,clock3)

    if horaL==tiempo.get():
        ventanaPrin.config(bg="#00FFFF")
        mixer.init()
        mixer.music.load("alarma.mp3")
        mixer.music.play()
        miEtiqueta.config(bg="#00FFFF")
        miEtiquetaM.config(bg="#00FFFF")
    
def parar():
    tiempo.set("")
    ventanaPrin.config(bg="#00FF00")
    miEtiqueta.config(bg="#00FF00")
    miEtiquetaM.config(bg="#00FF00")

#Temporizador global
def clock4():
    horas2= time.strftime("%H")
    minutos2= time.strftime("%M")
    segundos2=time.strftime("%S")
    horalocal2= horas2 + ":" + minutos2 + ":" + segundos2
    mietiqueta2.config(text=horalocal2)
    mietiqueta2.after(1000,clock4)

mietiqueta2= Label(root,text="",font=("Roboto",30))
mietiqueta2.pack()

clock4() #Aqui termina

ventanaPrin=Frame(root)
ventanaPrin.pack(fill="both", expand=1)
ventanaPrin.config(bg="#00FF00")

titulo=Label(ventanaPrin,text="Alarma",font=("Roboto",20),bg="#FFFF00")
titulo.grid(row=2,column=3,padx=5,pady=5)

miEtiqueta=Label(ventanaPrin,text="",font=("Roboto",1),bg="#00FF00")
miEtiqueta.grid(row=4,column=3)

miEtiquetaM=Label(ventanaPrin,text="",font=("Roboto",1),bg="#00FF00")
miEtiquetaM.grid(row=4,column=5)

Am=Entry(ventanaPrin,textvariable=tiempo,font=("Roboto",12))
Am.grid(row=5,column=3,padx=5,pady=5)

Alarma=Label(ventanaPrin,text="ESTABLECE \nALARMA",font=("Roboto",20),bg="#109420")
Alarma.grid(row=12,column=3,padx=5,pady=5)

boton1= Button(ventanaPrin,text="PARAR",bg="#1DD4AA",fg="#FBFBFB",
    font=("Roboto",18,"bold"),width=6,height=1,command=parar).grid(row=80,column=3)

clock3()
clock4()

root.mainloop()