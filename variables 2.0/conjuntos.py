#Creando un conjunto con set()
conjunto = set(["Dato 1"])
print(conjunto)

#Metiendo un conjunto dentro de otro conjunto
conjunto_uno = frozenset(["dato 1","dato 2"])
conjunto_dos = {conjunto_uno, "dato 3"}
print(conjunto_dos)

#Teoria de conjuntos
#Sunconjuntos
conjunto1 = {1,2,3,4}
conjunto2 = {1,2,4}
resultado = conjunto2.issubset(conjunto1)#Verificampos si es un sunconjunto
print(resultado)#Arroja un valor booleano

#Otra forma de hacer lo mismo
resultado1 = conjunto2 <= conjunto1
print(resultado1)

#Superconjuntos
resultado_superconjunto = conjunto1.issuperset(conjunto1)
resultado_superconjunto = conjunto2 > conjunto1

print(resultado_superconjunto)

#Verificar si hay algun numero en comun
resultado_en_comun = conjunto2.isdisjoint(conjunto1)
print(resultado_en_comun)#Arroja valor booleano, si hay algun numero en comun devuelve false

