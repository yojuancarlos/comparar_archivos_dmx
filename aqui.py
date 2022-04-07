import re

prueba="03290926.dmx"
prueba2="03290926.dmx"
#print (prueba.endswith(".dmx"))

# Expresiones regulares
#   ^ Inicia
#   $ Termina
#   . Cualquier caracter
#   \. punto
#  () Hace un grupo
#  (|) Grupos con opciones
pattern="(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])([0-1][0-9]|2[0-3])([0-5][0-9])\.dmx$"
m = re.match(pattern, prueba)
m2=re.match(pattern,prueba2)
#por fechas
#print(m.groups()[0])

if m.groups()== m2.groups():
    print(m.groups())






#lista = [4,2,7]

# Almacena n**2 cuando despues de recorrer lista en n se determina cuando n es par
#print ( [n**2 for n in lista if n % 2 == 0] )