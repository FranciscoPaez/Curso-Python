diccionario = {
    "nombre": 'Francisco',
    "apellido" : 'Paez',
    "edad" : 25 
}


#keys()
claves = diccionario.keys()#Devuelve las claves (tambien nos sirve para iterar)
print(claves)

#get()
claves_uno = diccionario.get("edad")#Devuelve el valor de la clave
print(claves_uno)

#pop
diccionario.pop("nombre")#Eliminando un elemento del diccionario
print(diccionario)

#items
diccionario_iterable = diccionario.items()#Obtenemos un elemento dict_items iterable
print(diccionario_iterable)

#clear()
diccionario.clear()#Eliminamos todo el diccionario
print(diccionario)