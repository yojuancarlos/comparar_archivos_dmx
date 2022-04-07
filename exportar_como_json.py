import json
archivo=2
peso=21
c={"a","b","c"}

my_dict = { 'el acrivo mas grande es':archivo,
            'supeso es ':peso, 'archivos':c, 'Sim': 12, 'Pooja': 4, 'Jen': 2}

#w es escritura
with open('algo.json', 'w') as fp:
    json.dump(my_dict, fp)
# r es lectura
with open('algo.json', 'r') as fp:
    data = json.load(fp)
print(data)
print(type(data))
#-----------------------------------


variable_dict = {}
print(variable_dict)
contador = 0
set_files = {'1.txt', '2.txt', '3.txt', '4.txt'}
for archivo in set_files:
  variable_dict[archivo] = contador
  contador = contador - 1
print(variable_dict)

set_archivo = {'1.txt', '2.txt', '3.txt', '4.txt', '1.txt'}
set_vacio = set()
dict_var2 = {}
dict_var3 = {'1.txt': {'mod': 10, 'tam': 5}, '2.txt': -1}
print(dict_var2)
# dict_var2 = {
#   '1.txt': {
#     'tam': 5,
#     'mod': 10
#   }
# }
dict_var2['1.txt'] = {}
dict_var2['1.txt']['mod'] = 10
dict_var2['1.txt']['tam'] = 5
dict_var2['2.txt'] = -1
print(dict_var2)
print(dict_var3)
print(dict_var2['1.txt'])

for item in dict_var3:
  print(item)
  print(dict_var3[item])

for key, value in dict_var3.items():
  print(f"{key} {value}")