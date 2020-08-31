# Los strings son una cadena de caracteres, por lo que cada letra posee una posición en la lista
mi_string_uno = "Curso"
mi_string_dos = "Python3"

# Metodo Format
final_string= "{} de {}!".format(mi_string_uno, mi_string_dos) # De forma automática se asignan los valores en orden
print(final_string)

final_string= "{x} de {y}!".format(y = mi_string_uno, x = mi_string_dos) # Pero puedes ordenar las variables en caso de ser necesario
print(final_string)

# Metodo lower (todo a minúsculas)
x = final_string.lower()
print(x)

# Metodo strip (Cada inicio de palabra en Mayúsculas como un título)
x = final_string.title()
print(x)

# Metodo upper (todo a mayúsculas)
x = final_string.upper()
print(x)

# Metodo Find (Busca la posición en es string)
x = final_string.find("Curso")
print(x)

# Metodo Count (Busca cuantas veces se repite un valor)
x = final_string.count("o")
print(x)

# Metodo Replace (Remplaza un valor por otro)
x = final_string.replace("o", "X")
print(x)

# Metodo Split (Divide los valores según el criterio seleccionado y crea una lista)
x = final_string.split(" ")
print(x)





