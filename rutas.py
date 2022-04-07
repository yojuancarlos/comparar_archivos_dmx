import json
import os
import re
import pickle

#-------------------------------------------------------------------
#aqui van las rutas
carpeta1 = "C:\pruebas\carpeta1"
carpeta2="C:\pruebas\carpeta2"


list_Carpeta1= os.listdir(carpeta1)
list_Carpeta2= os.listdir(carpeta2)

#conjunto
m=set(list_Carpeta1)

m2=set(list_Carpeta2)
#---------------------------------------------------------------------------------
#utilizo teoria de conjuntos
archivosrepetidos=m&m2
print(list(archivosrepetidos))
print(f"los archivos repetidos son {archivosrepetidos}")

archivosdiferentes=m-m2
print(f"los archivos que estan en la carpeta 1 pero no en la carpeta 2 son {archivosdiferentes}")
archivosdiferentes2=m2-m
print(f"los archivos que estan en la carpeta 2 pero no en la carpeta 1 son {archivosdiferentes2}")

#    diferencia    "-"

#--------------------------------------------------------------------------------------------------
# aqui mero el peso de cada archivo
variable_dict = {}
contador = 0
for filename in archivosrepetidos:
 #   --------------------------
    variable_dict[filename] = contador
    contador = contador + 1
    print(variable_dict)
    with open('algo.json', 'w') as file:
# file.write(aux)
        json.dump(list(variable_dict), file, indent=4)
    print("---"*20)
    variable_de_rutas_de_la_carpeta1 =(f"{carpeta1}\{filename}")
    file_size = os.path.getsize(variable_de_rutas_de_la_carpeta1)
    #print('el tamaño del archivo',filename,' de la carpeta 1 es ', file_size, 'bytes')
    variable_de_rutas_de_la_carpeta2 = (f"{carpeta2}\{filename}")
    file_size2 = os.path.getsize(variable_de_rutas_de_la_carpeta2)

    #print('el tamaño del archivo', filename, ' de la carpeta 2 es ', file_size2, 'bytes')
#-----------------------------------------------------------------------------------------------------
#aqui miro cual es el mas pesado cuando los archivos se repiten
    if file_size > file_size2:

        print(f"el archivo {filename} mas pesados esta en la {variable_de_rutas_de_la_carpeta1}  y su peso es {file_size}")
        aux=print(f"el archivo {filename} mas pesados esta en la {variable_de_rutas_de_la_carpeta1}  y su peso es {file_size}")
    elif file_size2 > file_size:
        print(f"el archivo {filename} mas pesado esta en la {variable_de_rutas_de_la_carpeta2}  y su peso es {file_size2}")
    aux = f"el archivo {filename} mas pesado esta en la {variable_de_rutas_de_la_carpeta2}  y su peso es {file_size}\n"




#

#aqui aplico el json


diccionario_dearchivos_archivosrepetidos={'los archivos que estannnnnnnnnnnnnnnn repetidos son':list(archivosrepetidos),
                                          'los archivos que estan en la carpeta 1 pero no en la 2 son':list(archivosdiferentes),
                                          'los arcivos que entan en la carpeta 2 pero no en la 1 son':list(archivosdiferentes2)}


with open('data.json','w') as file:
    json.dump(diccionario_dearchivos_archivosrepetidos, file, indent=4)

#with open('algo.json', 'w') as fp:
   # json.dump(diccionario_dearchivos_archivosrepetidos, fp)
# r es lectura
#with open('algo.json', 'r') as fp:
 #   data = json.load(fp)
#print(data)
#print(type(data))
#----------------




