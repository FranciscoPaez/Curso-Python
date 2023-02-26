cadena1 = "Hola soy Francisco"
cadena2 = ", bienvenido al curso de Python."

mayuscula = cadena1.upper() #Convierte el string a mayusculas

minuscula = cadena1.lower() #Convierte el string a minuscula

primer_letra_mayus = cadena1.capitalize() #Convierte la primer letra en mayuscula

busqueda_find = cadena1.find("f") #Buscamos en la cadena, devuelve la posicion. Si no hay coincidencia devuelve -1

#Buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index("h")


es_numerico = cadena1.isnumeric() #Si es numerico, devuelve True, sino False

es_alfanumerico = cadena1.isalpha() #Si es alfanumerico, devuelve True, sino False

#Buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincide
contar_coincidencias = cadena1.count("a")

#Contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada, si es asi devueve True
empieza_con = cadena1.startswith("H")

#Verificamos si una cadena termina con otra cadena dada, si es asi devueve True
empieza_con = cadena1.endswith("H")


print(mayuscula, minuscula, primer_letra_mayus)
print(busqueda_find)
print(busqueda_index)
print(es_numerico)
print(es_alfanumerico)
print(contar_coincidencias)