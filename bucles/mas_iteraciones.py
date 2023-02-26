celulares = ["Samsung","Iphone","Motorola","Xiaomi","LG"]

for celular in celulares:
    if celular == 'LG': #Es lo que no queremos recorrer en la lista
        continue
    print(f'Me voy a comprar un celular marca: {celular}')
    
#Evitar que el bucle siga ejecutandoce
for celular in celulares:
    if celular == 'Xiaomi':
        break #Terminamos el bucle
    print(f'Me voy a comprar un celular marca: {celular}')
    
print("Bucle terminado")

#Recorrer una cadena de texto

cadena = "Hola Francisco, bienvenido."

for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo
numeros = [1,2,3,4,5,6]

numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)