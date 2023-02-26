#Funciones integradas en Python

numeros = [1,5,6,7,11,34,64]

#max()
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#min()
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#round()
numero = round(12.345564, 2)#Redondeamos decimales, el numero despues de la coma es la cantidad de decimales que queremos
print(numero)

#bool()
#Retorna False si le pasamos -> 0, vacio, False, None
#Retorna True si le pasamos -> numero distinto a 0, string, True, datos no vacios
resultado_bool = bool(None)
print(resultado_bool)

#all()
#Retorna True, si todos los valores son verdaderos
resultado_all = all([0,"Hola",[324,32]])

print(resultado_all) #False ya que hay un 0

