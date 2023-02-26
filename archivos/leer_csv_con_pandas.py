import pandas as pd  #instalamos la libreria desde cmd comando = py -m pip, luego py -m pip install pandas
archivo = pd.read_csv("archivos\\datos.csv")
print(archivo)

#Obteniendo los datos de la columna nombre
print(archivo["nombre"])

#Slicing
cadena = "123456789"
print(cadena[1:4])#Recorremos la cadena desde su numero de indice hasta otro indice

#Ordenando el dataframe por la edad
archivo_orden_ascendente = archivo.sort_values("edad")
print(archivo_orden_ascendente)

#Ordenando de forma descendente
archivo_orden_descendente = archivo.sort_values("edad",ascending=False)
print(archivo_orden_descendente)

#Concatenamos los dos dataframes

archivo_concatenar = pd.concat([archivo,archivo_orden_descendente])
print(archivo_concatenar)

#Accediendo a la primer fila con head()
primer_fila = archivo.head(1)#Le pasamos el numero de fila que queremos ver
print(primer_fila)

#Accediendo a las ultimas 2 filas con tail()
ultimas_fila = archivo.tail(2)
print(ultimas_fila)

#Accediendo a la cantidad de columnas y filas con shape()
total_filas_columnas = archivo.shape
print(total_filas_columnas)

#Accediendo a un elemto en especifico del data frame con loc
#Accediendo a la edad de la fila 2
elemento_loc = archivo.loc[2,"edad"]#Fila,elemento.
print(elemento_loc)

#Ahora con iloc
elemento_iloc = archivo.iloc[2,2]#Accedemos por sus indices.
print(elemento_iloc)

#Accediendoa todas las filas de una columna
apellidos = archivo.iloc[:,1]
print(apellidos)