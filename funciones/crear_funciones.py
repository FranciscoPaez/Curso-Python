#Funcion simple
def saludar():
    print("Hola, bienvenido.")
#Ejecuntando la funcion simple    
saludar()


#Funciones con parametros
def saludar_paramatro(nombre):
    print(f"Hola {nombre}, bienvenido.")
saludar_paramatro("Francisco")

#Funciones que retornan valores
def crear_comtrasena_random(num):
    caracteres = "sajhgfdk"
    num_entero = str(num)
    num = int(num_entero[0])
    caracter1 = num -2
    caracter2 = num 
    caracter3 = num - 6
    contrasena = f"{caracteres[caracter1]}{caracteres[caracter2]}{caracteres[caracter3]}{num*2}"
    print(contrasena)
    
crear_comtrasena_random(55)