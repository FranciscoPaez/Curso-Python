#Creando funcion de sumar numeros
def sumar():
    #Iniciando un bucle
    while True:
        #Pedimos que ingresen los numeros a sumar
        a = input("Ingrese primer numero: ")
        b = input("Ingrese segundo numero: ")
        try:
            #Convertimos los numeros a enteros y los sumamos
            resultado = int(a) + int(b)
        #Si el programa lanzo una excepcio entonces....print()
        except Exception as e:
            print(f'ERROR: {e}')
            print("Debes ingresar un numero para que la operacion sea realizada")
        #Si todo salio bien finalizamos el bucle
        else:
            break
        #Se ejecuta siempre, rara vez se utiliza
        finally: 
            print("En caso del resultado ser un numero, programa ejecutado con exito.")
    return resultado

print(sumar())