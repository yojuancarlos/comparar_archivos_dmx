variable_dict = {}
print(variable_dict)
contador = 0
set_files = {'1.txt', '2.txt', '3.txt', '4.txt'}
for archivo in set_files:
  variable_dict[archivo] = contador
  contador = contador - 1
print(variable_dict)