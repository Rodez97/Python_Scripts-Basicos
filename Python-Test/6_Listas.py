mi_lista = ["Danilo", 5, 5.2, True] # Las listas puedes poseer valores de diferente tipo
print(mi_lista)

# Las listas pueden crecer y decrecer
# Método Append (Añadir)
mi_lista.append("Valor añadido") # Añade un valor al final de la lista
print(mi_lista)

# Método Insert (Insertar)
mi_lista.insert(3, False) # Inserta un valor en la posición específica (El primer parámetro indica la posición)
print(mi_lista)

# Método Remove (Remover)
mi_lista.remove("Danilo") # Elimina un valor específico de la lista
print(mi_lista)

# Método Pop
ultimo_valor = mi_lista.pop()
mi_lista.pop() # Elimina el últomo valor del Stack/Pila
print(mi_lista)
print(ultimo_valor)

# Listas de un mismo tipo
# Método Sort (Ordenar)
lista_enteros = [0, 2, 10, 199, 2000, 5, 34, 569, 18]
lista_enteros.sort() # Ordena la lista de menor a mayor
lista_enteros.sort(reverse = True) # Ordena la lista de mayor a menor
print(lista_enteros)

# Método Extend (Unir dos listas)
lista_enteros = [0, 2, 10, 199, 2000, 5, 34, 569, 18]
mi_lista.extend(lista_enteros) # Une las dos listas
print(mi_lista)
