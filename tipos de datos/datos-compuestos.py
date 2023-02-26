lista = ["Francisco", "Paez", True, 178]
tupla = ("Francisco", "Paez", True, 178) # Es lo mmismo que una lista pero no se puede modificar.

print(lista[2])

#Ejemplo
lista[1] = "Messi"
print(lista) 

#Creando un conjunto (set)
conjunto = {"Francisco", "Paez", True, 178} # No podemos acceder a datos por su indice ni duplicarlos, por ej: conjunto[2]

#Creando un Diccionario (dict)
diccionario = {
    'nombre': "Francisco",
    'apellido': "Paez",
    'estado_emocional' : True,
    'altura' : 178
}

print(diccionario['nombre']) #Manera de acceder a los datos

