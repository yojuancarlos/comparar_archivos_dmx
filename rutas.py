import json
import os


# -------------------------------------------------------------------
# aqui van las rutas
carpeta1 = "C:\pruebas\carpeta1"
carpeta2 = "C:\pruebas\carpeta2"


lista_carpeta1 = os.listdir(carpeta1)
lista_carpeta2 = os.listdir(carpeta2)

# conjunto
m = set(lista_carpeta1)
m2 = set(lista_carpeta2)
# ---------------------------------------------------------------------------------
# utilizo teoria de conjuntos
# archivos repetidos
archivosrepetidos=m&m2


# archivos que estan en una carpeta pero no en otra
archivosdiferentes = m-m2
archivosdiferentes2 = m2-m


#    diferencia    "-"
# para que solo me muestre archivos dmx


# --------------------------------------------------------------------------------------------------
# aqui mero el peso de cada archivo
archivos_con_pesos_iguales=[]
rutasypeso=[]
for filename in archivosrepetidos:
    variable_de_rutas_de_la_carpeta1 =(f"{carpeta1}\{filename}")
    peso_archivo_carpeta1 = os.path.getsize(variable_de_rutas_de_la_carpeta1)
    variable_de_rutas_de_la_carpeta2 = (f"{carpeta2}\{filename}")
    peso_archivo_carpeta2 = os.path.getsize(variable_de_rutas_de_la_carpeta2)
    if filename.endswith(".dmx"):
        print("exito")
    print(filename)
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


print(rutasypeso)
# aqui aplico el json




diccionario_dearchivos_archivosrepetidos={'ambas_carpetas':list(archivosrepetidos),
                                          'solo_carpeta1':list(archivosdiferentes),
                                          'archivos_iguales':list(archivos_con_pesos_iguales),
                                          'solo_carpeta2':list(archivosdiferentes2)}
# aqui adiciono a json el peso
diccionario_dearchivos_archivosrepetidos['archivosconpeso']={}
for elemento in rutasypeso:
    key=elemento[0]
    value=elemento[1]
    diccionario_dearchivos_archivosrepetidos['archivosconpeso'][key]=value



with open('data.json','w') as file:
    json.dump(diccionario_dearchivos_archivosrepetidos, file, indent=4)






