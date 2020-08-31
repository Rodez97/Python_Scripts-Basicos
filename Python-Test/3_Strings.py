mi_string = "Hola mundo! 'Danilo'" # Se puede declarar con comillas dobles("") o comillas simples('')
mi_string_salto_de_linea = """ Este string posee salto de linea:\n Linea 1\n Linea 2 """ # Se puede declarar con comillas dobles("") o comillas simples(''), pero tres al inicio y final

print(mi_string)
print(mi_string_salto_de_linea)


# Ejemplo de suma de strings
lenguaje = "Python 3"
nombre = "Danilo"

string_final = "El lenguaje es : " + lenguaje + ", El nombre es : " + nombre # Forma 1
print(string_final)

string_final = "El lenguaje es : %s, El nombre es : %s" %(lenguaje, nombre) # Forma 2
print(string_final)

string_final = "El lenguaje es : {}, El nombre es : {}".format(lenguaje, nombre) # Forma 3
print(string_final)