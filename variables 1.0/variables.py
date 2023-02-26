#Definiendo una variable

nombre = input("Ingrese su nombre ")

#Concatenar con +

bienvenida = "Hola " + nombre + " ¿Como estas?"
print(bienvenida)

#Concatenar con f-strings

fString = f"Hola {nombre} ¿Como estas?"
print(fString)

# Operadores de pertenencia (in / not in)

print("Hola" in bienvenida) # Arroja un valor booleano (True or False)

print("Hola" not in bienvenida)
