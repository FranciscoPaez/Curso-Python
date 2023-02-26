#AND (Para que el valor que nos devuelva sea TRUE se deben cumplir las dos condiciones)

resultado = True & True #True
resultado2 = False & True #False
resultado3 = True & False #False
resultado4 = False & False #False

#OR (Nos va a devolver falso solo si las dos condiciones no se cumplen)

resultado5 = True | True #True
resultado6 = False | True #True
resultado7 = True | False #True
resultado8 = False | False #False

#NOT ()

resultado9 = not True #False
resultado10 = not False #True

print("AND")
print(resultado)
print(resultado2)
print(resultado3)
print(resultado4)
print("OR")
print(resultado5)
print(resultado6)
print(resultado7)
print(resultado8)
print("NOT")
print(resultado9)
print(resultado10)
