#Parametro args

def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"
resultado = suma("Francisco",1,2,4,5,7,11)
print(resultado)