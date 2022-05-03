import os
import fnmatch

abecedario = "abcdefghijklmnñopqrstuvwxyz"

cadena = "el pato volo por la mañana"

result = list(filter(lambda x: not x in cadena, abecedario))
print(result)
print(len(result))
if len(result) == 0:
    print("Estan todas las letras")
else:
    print("no estan todas las letras")