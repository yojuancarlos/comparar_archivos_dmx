import json
import os


# -------------------------------------------------------------------
# aqui van las rutas
carpeta1 = "C:\pruebas\carpeta1"
carpeta2 = "C:\pruebas\carpeta2"


list_Carpeta1 = os.listdir(carpeta1)
list_Carpeta2 = os.listdir(carpeta2)

# conjunto
m = set(list_Carpeta1)
m2 = set(list_Carpeta2)
# ---------------------------------------------------------------------------------
# utilizo teoria de conjuntos
# archivos repetidos
archivosrepetidos=m&m2


# archivos que estan en una carpeta pero no en otra
archivosdiferentes = m-m2
archivosdiferentes2 = m2-m


#    diferencia    "-"

# --------------------------------------------------------------------------------------------------
# aqui mero el peso de cada archivo
archivos_con_pesos_iguales=[]
rutasypeso=[]
for filename in archivosrepetidos:
    variable_de_rutas_de_la_carpeta1 =(f"{carpeta1}\{filename}")
    file_size = os.path.getsize(variable_de_rutas_de_la_carpeta1)
    variable_de_rutas_de_la_carpeta2 = (f"{carpeta2}\{filename}")
    file_size2 = os.path.getsize(variable_de_rutas_de_la_carpeta2)
# -----------------------------------------------------------------------------------------------------
# aqui miro cual es el mas pesado cuando los archivos se repiten
    if file_size > file_size2:

        # print(f"el archivo {filename} mas pesados esta en la {variable_de_rutas_de_la_carpeta1}  y su peso es {file_size}")
        rutasypeso.append((variable_de_rutas_de_la_carpeta1,file_size))
    elif file_size2 > file_size:
       # print(f"el archivo {filename} mas pesado esta en la {variable_de_rutas_de_la_carpeta2}  y su peso es {file_size2}")

        rutasypeso.append((variable_de_rutas_de_la_carpeta2,file_size2))
    if file_size== file_size2:
       archivos_con_pesos_iguales.append(filename)


print(rutasypeso)
# aqui aplico el json




diccionario_dearchivos_archivosrepetidos={'ambas_carpetas':list(archivosrepetidos),
                                          'solo_carpeta1':list(archivosdiferentes),
                                          'archivos_iguales':list(archivos_con_pesos_iguales),
                                          'solo_Carpeta2':list(archivosdiferentes2)}
# aqui adiciono a json el peso
diccionario_dearchivos_archivosrepetidos['archivosconpeso']={}
for elemento in rutasypeso:
    key=elemento[0]
    value=elemento[1]
    diccionario_dearchivos_archivosrepetidos['archivosconpeso'][key]=value



with open('data.json','w') as file:
    json.dump(diccionario_dearchivos_archivosrepetidos, file, indent=4)






