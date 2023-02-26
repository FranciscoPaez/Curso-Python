import csv

with open ("archivos\\datos.csv") as archivo_csv:
    reader = csv.reader(archivo_csv)
    for row in reader:
        print(row)