class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Cometiste el siguiente error: {err}")
 
#Forma de lanzar excepciones con raise       
# raise ZeroDivisionError ("Dividiste por 0")

#Ahora vamos a lanzar nuestra propia excepcion
try:
    raise MiExcepcion("Debes revisar tu codigo")
except:
    print("No es posible cometer esos errores")