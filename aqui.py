import re

prueba ="03290926.dmx"
prueba3="03290925.dmx"
prueba4= "0329092dad8.dmx"
prueba2="03290929.dmx"



# Expresiones regulares
#   ^ Inicia
#   $ Termina
#   . Cualquier caracter
#   \. punto
#  () Hace un grupo
#  (|) Grupos con opciones
pattern="(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])([0-1][0-9]|2[0-3])([0-5][0-9])\.dmx$"
tal=[]
tal.append(prueba)
tal.append(prueba2)
tal.append(prueba3)
tal.append(prueba4)


m2=re.match(pattern,prueba2)



files = [f for f in tal if re.match(pattern, f)]

print(files)


#if m.groups()
#









#lista = [4,2,7]

# Almacena n**2 cuando despues de recorrer lista en n se determina cuando n es par
#print ( [n**2 for n in lista if n % 2 == 0] )