'''Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt la tabla de multiplicar de ese número, donde n es el número introducido.'''

n = int(input("Escribe un numero(entre 1 y 10): "))
file1 = open(f'tabla-{n}.txt', 'w')
for i in range(1, 11):
    file1.write(f'{n} x {i} = {n * i}\n')
file1.close()
print(f"La tabla de este numero: {n}, se a guardado.")