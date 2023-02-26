animales = ["gato","perro","loro","caballo"]

#Recorremos la lista con for
for animal in animales:
    print(f'Ahora la varible animal es igual a: {animal}')
    
#Recorriendo lista de numeros
numeros = [1,2,3,4]

for numero in numeros:
    print(numero)
    
#Recorriendo dos listas al mismo tiempo con zip()
for numero,animal in zip(animales,numeros):
    print(f'Recorriendo lista 1: {numero}')
    print(f'Recorriendo lista 2: {animal}') 
    
#Recoremos los parametros con range()
for num in range(10,30): #El primero esta incluido, el ultimo no
    print(num)
    
#Forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')
    
#Usamos else
for numero in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("Fin del bucle")
    
# Todo lo anterior sirve para aplicarlo a tuplas #