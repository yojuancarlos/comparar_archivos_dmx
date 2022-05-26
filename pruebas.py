import json
import os
import re
import os.path, time
import tkinter.filedialog as fd
import tkinter.messagebox as mb
# -------------------------------------------------------------------
mb.showinfo('mensaje','seleccione la primera carpeta')
carpeta1= fd.askdirectory(title='abrir carpeta...',initialdir='/')
if carpeta1:
    mb.showinfo('mensaje','usted selecciono la carpeta  '+ carpeta1)
print(carpeta1)

mb.showinfo('mensaje','seleccione la segunda carpeta')
carpeta2= fd.askdirectory(title='abrir carpeta...',initialdir='/')
if carpeta2:
    mb.showinfo('mensaje', 'usted selecciono la carpeta  '+ carpeta2)
print(carpeta2)

# aqui van las rutas
#carpeta1 = "C:\pruebas\carpeta1"
#carpeta2 = "C:\pruebas\carpeta2"

lista_carpeta1 = os.listdir(carpeta1)
lista_carpeta2 = os.listdir(carpeta2)
print(lista_carpeta1)
exprecion_regular = "(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])([0-1][0-9]|2[0-3])([0-5][0-9])\.dmx$"
# conjunto
m = set(lista_carpeta1)
m2 = set(lista_carpeta2)
#---------
# ---------------------------------------------------------------------------------
# utilizo teoria de conjuntos
# archivos repetidos
archivosrepetidos= m & m2
# archivos que estan en una carpeta pero no en otra
archivosdiferentes = m - m2
archivosdiferentes2 = m2 - m
#    diferencia    "-"
# para que solo me muestre archivos dmx
# --------------------------------------------------------------------------------------------------
# filtrar archivos dmx
archivos_dmx_repetidos = [f for f in archivosrepetidos if re.match(exprecion_regular, f)]
archivos_dmx_diferentes = [f for f in archivosdiferentes if re.match(exprecion_regular, f)]
archivos_dmx_diferentes2 = [f for f in archivosdiferentes2 if re.match(exprecion_regular, f)]
# --------------------------------------------------------------------------------------------------
# aqui mero el peso de cada archivo
archivos_con_pesos_iguales = []
rutasypeso = []

for filename in archivos_dmx_repetidos:
    variable_de_rutas_de_la_carpeta1 = os.path.join(carpeta1,filename)
    peso_archivo_carpeta1 = os.path.getsize(variable_de_rutas_de_la_carpeta1)

    variable_de_rutas_de_la_carpeta2 = os.path.join(carpeta2, filename)
    peso_archivo_carpeta2 = os.path.getsize(variable_de_rutas_de_la_carpeta2)
    print(time.ctime(os.path.getmtime(variable_de_rutas_de_la_carpeta1)))
# -----------------------------------------------------------------------------------------------------
# aqui miro cual es el mas pesado cuando los archivos se repiten
    if peso_archivo_carpeta1 >peso_archivo_carpeta2:
        # print(f"el archivo {filename} mas pesados esta en la {variable_de_rutas_de_la_carpeta1}  y su peso es {peso_archivo_carpeta1}")
        rutasypeso.append((variable_de_rutas_de_la_carpeta1,peso_archivo_carpeta1))
    elif peso_archivo_carpeta2 > peso_archivo_carpeta1:
       # print(f"el archivo {filename} mas pesado esta en la {variable_de_rutas_de_la_carpeta2}  y su peso es {peso_archivo_carpeta12}")
        rutasypeso.append((variable_de_rutas_de_la_carpeta2,peso_archivo_carpeta2))
    if peso_archivo_carpeta1==peso_archivo_carpeta2:
       archivos_con_pesos_iguales.append(filename)
# aqui aplico el json
diccionario_de_respuesta={'ambas_carpetas':list(archivos_dmx_repetidos),
                        'solo_carpeta1':list(archivos_dmx_diferentes),
                        'archivos_con peso igual':list(archivos_con_pesos_iguales),
                        'solo_carpeta2':list(archivos_dmx_diferentes2)}
# aqui adiciono a json el peso
diccionario_de_respuesta['archivosconmayorpeso']={}
for elemento in rutasypeso:
    key=elemento[0]
    value=elemento[1]
    diccionario_de_respuesta['archivosconmayorpeso'][key]=value
with open('data.json','w') as file:
    json.dump(diccionario_de_respuesta, file, indent=4)






