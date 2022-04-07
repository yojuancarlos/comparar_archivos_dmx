# -*- coding: utf-8 -*-


a={1,2,3}
b={4,5,6,2}
print (a)

print (b)
print(a.union(b))
print(a.intersection(b))


c={"a","b","c"}
d={"d","e","f","b"}

import re

prueba="03290925.dmx"
print (prueba.endswith(".dmx"))

# Expresiones regulares
#   ^ Inicia
#   $ Termina
#   . Cualquier caracter
#   \. punto
#  () Hace un grupo
#  (|) Grupos con opciones
pattern="(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])([0-1][0-9]|2[0-3])([0-5][0-9])\.dmx$"
m = re.match(pattern, prueba)
print(m.groups())

lista = [4,2,7]

# Almacena n**2 cuando despues de recorrer lista en n se determina cuando n es par
print ( [n**2 for n in lista if n % 2 == 0] )

# Almacena n**2 cuando despues de recorrer lista en n
print ( [n**2 for n in lista] )

#[file iterar_lista_de_archivos comparar_con_re_si_es_dmx]
#for file in os.listdir("."):
#    if re.match(pattern, file):
#        respuesta.append(file)

def ejecuta_funciones(lista:list, funciones:list):
  for f in funciones:
    for l in lista:
      print(f(l))
    print("-"*30)

ejemplo_1 = lambda path: "Tamaño de "+path
ejemplo_2 = lambda path: "Modificacion de "+path
ejemplo_3 = lambda path: "Determina si es directorio "+path

print (ejemplo_1('archivo 1'))
print (ejemplo_2('archivo 1'))

print("-"*30)
lista = ["a1", "a2", "a3", "a4", "a5", "a6"]
argumentos  = ['Modi']
funciones = []
for a in argumentos:
  if a == 'Size':
    funciones.append(ejemplo_1)
  if a == 'Modi':
    funciones.append(ejemplo_2)
  if a == 'Dir':
    funciones.append(ejemplo_3)
#funciones = [ejemplo_1, ejemplo_2, ejemplo_3]
#funciones = [ejemplo_1]
ejecuta_funciones(lista, funciones)