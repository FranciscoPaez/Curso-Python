#Creando una lista con funcion list()
lista = list(["hola","Francisco",25])
print(lista)

#len
cantidad_elementos = len(lista) 
print(cantidad_elementos)#Devielve la cantidad de elementos dentro de la lista

#append
agreando_elementos_append = lista.append("Paez")#Agregamos elemento a la lista
print(lista) 

#insert
lista.insert(2, True)#Agregamos elementos a la lista en un indice especifico
print(lista)

#extend
lista.extend(["Bienvenido",43])#Agregamos varios elementos a la lista
print(lista)

#pop
lista.pop(0)#Eliminamos un elemento de la lista (por su indice)
lista.pop(-1)#Con -1 borramos el ultimo elemento de la lista, con -2 el anteultmimo y asi susecivamente
print(lista)

#remove
lista.remove("Francisco")#Removiendo un elemento de la lista por su valor
print(lista)

#clear
lista.clear()#elimina todos los elementos de la lista
print(lista)



#Agregamos elementos numericos a la lista que eliminamos para poder usar el metodo sort()
lista.extend([2,4,3,7,6,8])
print(lista)

#sort
lista.sort()#Ordena los numeros de menor a mayor
print(lista)

lista.sort(reverse=True)#Invertimos el orden
print(lista)

#reverse
lista.reverse()#invierte el orden de la lista
print(lista)


