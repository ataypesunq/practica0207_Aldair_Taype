'''Escribir un programa que acceda al fichero de internet mediante la url indicada y muestre por pantalla el número de palabras que contiene.
http://textfiles.com/adventure/aencounter.txt '''
import urllib.request
def num_palabras():
    url = "http://textfiles.com/adventure/aencounter.txt"
    file1 = urllib.request.urlopen(url)
    num = 0
    for line in file1:
        linea = line.decode("utf-8")
        palabras = linea.split()
        num += len(palabras)
    print(f"El fichero contiene {num} palabras.")