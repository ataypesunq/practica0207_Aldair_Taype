'''Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.'''
import os
def linea_file():
    n = int(input("Escribe un numero(entre 1 y 10) para n: "))
    m = int(input("Escribe un numero(entre 1 y 10) para m: "))
    file1 = f"tabla-{n}.txt"
    if os.path.infile(file1):
        with open (file1, 'r') as file:
            linea = file.readlines()
        if 1 <= m <= len(linea):
            print(f"La linea {m} del fichero {file1}: {linea[m-1].strip()}")
        else:
            print(f"El fichero {file1} no tiene linea.")
    else:
        print(f"{file1} no existe")