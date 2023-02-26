import re

texto = '''Hola. esta es la cadena 1. Cadena
Esta es la linea 234 de texto.
Y esta es la ultima linea'''

#search()
resultado_search = re.search("Hola",texto)#Busca las coincidencias en el texto
print(resultado_search)

#findball()
resultado_findball = re.findall("esta",texto,flags=re.IGNORECASE)#Busca todas las coincidencias, aplicamos otro parametro flags para que ignore las mayusculas y minusculas
print(resultado_findball)

#\d -> Busca digitos numericos del 0 - 9
resultado_d = re.findall(r"\d", texto)
print(resultado_d)

#\D -> Busca todo menos digitos numericos
resultado_d_mayus = re.findall(r"\D", texto)
print(resultado_d_mayus)

#\w -> Busca caracteres alfanumericos [a-z A-Z 0-9]
resultado_w = re.findall(r"\w", texto)
print(resultado_w)

#\W -> Busca todo menos caracteres alfanumericos
resultado_w_mayus = re.findall(r"\W", texto)
print(resultado_w_mayus)

#\s Busca espacios en blanco -> espacios, tabs, saltos de linea
resultado_s = re.findall(r"\s", texto)
print(resultado_s)

#\S Busca todo menos espacios en blanco -> espacios, tabs, saltos de linea
resultado_s_mayus = re.findall(r"\S", texto)
print(resultado_s_mayus)

#. Busca todo menos saltos en linea
resultado_punto = re.findall(r".", texto)
print(resultado_punto)

#\n Busca los saltos en linea
resultado_salto_en_linea = re.findall(r"\n", texto)
print(resultado_salto_en_linea)

#\ Cancelamos caracteres especiales
cancelar_car_especiales = re.findall(r"\.", texto) #Cancelamos la funcion de puntos y buscamos puntos
print(cancelar_car_especiales)

#Armando una cadena que busque en el texto un numero, un punto y un espacio.
busqueda_compleja = re.findall(f'\d\.\s', texto) 
print(busqueda_compleja)

#^ Busca el comienzo de una linea
busqueda_comienzo_linea = re.findall(f'^Esta', texto, flags=re.M) #En caso de no ser la palabra correcta que este al inicio nos da un resultado vacio
#re.M es para que busque el comienzo multilinea
print(busqueda_comienzo_linea)

#$ Busca el final de una linea
final = re.findall(r'linea$', texto, flags=re.M)
print(final)

#{n} Busca n cantidad de veces el valor de la izquierda
buscar_condicion = re.findall(r'\d{3}', texto) #Buscamos tres digitos que cumplan la condicion
print(buscar_condicion)