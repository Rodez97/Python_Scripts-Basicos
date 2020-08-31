# Los strings son una cadena de caracteres, por lo que cada letra posee una posición en la lista
mi_string = "Curso de Python3!"
print(mi_string)
print(mi_string[4])
print(mi_string[-4]) # Si se utilizan números negativos el conteo comienza desde atrás (Comienza en -1)
print(mi_string[9:15]) # Tambien se puede extraer un subarray o colección indicando desde/hasta donde captorar los caracteres
print(mi_string[9:15:2]) # Tambien se pueden mostrar los caracteres de 2 en dos, saltando
print(mi_string[::-1]) # Invierte el orden del array/string


for x in mi_string:
    print(x)