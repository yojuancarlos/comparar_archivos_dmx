#import os
#carpetas = [imagenes for directorio, subdirectorio, imagenes in os.walk(r'E:\universidad\2022-1\Comunicación de datos')]
#print(carpetas)
import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
#---------------------------------------
#from tkinter.filedialog import askopenfilename
#archivo = askopenfilename()
#print(archivo)
#--------------------------------------
mb.showinfo('mensaje','seleccione la primera carpeta')
directorio= fd.askdirectory(title='abrir carpeta...',initialdir='/')
if directorio:
    mb.showinfo('mensaje','usted selecciono la carpeta  '+ directorio)
print(directorio)

mb.showinfo('mensaje','seleccione la segunda carpeta')
directorio2= fd.askdirectory(title='abrir carpeta...',initialdir='/')
if directorio2:
    mb.showinfo('mensaje', 'la carpeta que usted selecciono fue ', directorio2)
print(directorio2)

