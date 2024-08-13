from ntpath import join
import os

def punto1(archivo):
    with open(archivo, "r") as f:
        lineas = f.readlines()
        print("Cantidad de lineas:", len(lineas))

# Fuente: https://www.w3schools.com/python/ref_file_readlines.asp

punto1("nombres.txt")

def punto2(archivo1, archivo2):
    with open(archivo1, "r") as f:
        lineas = f.readlines()
    
    with open(archivo2, "a") as f:
        f.writelines(lineas)
    return archivo1, archivo2

punto2("nombres.txt", "copia.txt")

#Fuente: https://www.w3schools.com/python/ref_file_writelines.asp

#LA COPIA SE PUEDE VER EN EL ARCHIVO "copia.txt"

def punto3(archivo1, archivo2):
    with open(archivo1, 'r') as f1:
        lineas1 = f1.readlines()
    
    with open(archivo2, 'r') as f2:
        lineas2 = f2.readlines()
                
    with open(archivo2, 'w') as f2:
        for i in range(len(lineas1)):
            linea1 = lineas1[i]
            linea2 = lineas2[i]
            f2.write(linea2.strip() + " " + linea1)

punto3('apellidos2.txt', 'nombres.txt')

#Se puede ver en el archivo "nombres.txt" (Al archivo se le agregan los respectivos apellidos a los nombres que
# pertenecen).


