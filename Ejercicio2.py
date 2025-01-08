'''Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número, donde n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.'''
import os
def tabla_multiplicar():
    n = int(input("Escribe un numero(entre 1 y 10): "))
    file1 = f"tabla-{n}.txt"
    if os.path.isfile(file1):
        with open(file1, 'r') as file:
            info = file.read()
        print(f"Informacion del fichero: {file1}: {info}")
    else:
        print(f"{file1} no existe")