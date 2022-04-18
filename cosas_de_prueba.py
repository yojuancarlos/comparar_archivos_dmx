import pprint

set_archivo = {'1.txt', '2.txt', '3.txt', '4.txt', '1.txt'}
set_vacio = set()
dict_var2 = {}
dict_var3 = {'1.txt': {'mod': 10, 'tam': 5}, '2.txt': -1}

# dict_var2 = {
#   '1.txt': {
#     'tam': 5,
#     'mod': 10
#     'detalles': {
#       'campo1': 1,
#     }
#   },
#   '2.txt': -1
# }


import json

numero_elementos = 10
list_1 = ["archivo"+str(n) for n in range(numero_elementos) ]
list_2 = [n for n in range(numero_elementos) ]
list_3 = [["archivo"+str(n),n] for n in range(numero_elementos) ]


respuesta = {'k1': 'v1', 'k3': 'v3', 'k3': 'v4'}
"""
respuesta = {
  'k1': 'v1',
  'k2': {
    'archivo0': 0,
    ...
    'archivo9': 9,
  },
  'k3': 'v3'
}
"""

# Generar el segundo nivel
#   respuesta['k2']['archivo0'] = 0
#   ...
#   respuesta['k2']['archivo9'] = 9

respuesta['k2'] = {}
for elemento in list_1:

  respuesta['k2'][elemento] = 0
  for elemento in list_2:
    pass
    #print(elemento)

respuesta['k4'] = {}
for elemento in list_3:
  #key, value = elemento
  key = elemento[0]
  value = elemento[1]

  respuesta['k4'][key] = value

respuesta_bonita = json.dumps(respuesta, indent=4)
print(respuesta_bonita)