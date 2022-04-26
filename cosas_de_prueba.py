import os
import fnmatch
import datetime
import time
carpeta1 = "C:\pruebas\carpeta1"
list_Carpeta1 = os.listdir(carpeta1)


fechas_de_creacion={}





for file in list_Carpeta1:
    variable_de_rutas_de_la_carpeta1 = (f"{carpeta1}\{file}")
    time1 = datetime.datetime(2022,4,18,0,0,0,0)
    time2 =datetime.datetime.fromtimestamp(os.stat(variable_de_rutas_de_la_carpeta1).st_ctime)
    dayCount = (time1 -time2).days
    if dayCount<0:
        print(file)