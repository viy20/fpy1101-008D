import os
import csv
import time
os.system=("cls")
from random import *

def numero_pedido():
    folio=1
    folio=randint(1,1000)
    return(folio)
pedido=numero_pedido()

archivo="pedido.csv"
sectores=("san bernardo", "calera de tango", "buin")
lista_de_pedidos=[
    [1, "juan","av lo blanco","san bernardo",1,2,1]
]
    
def registrar_pedido():
    print("registrar pedido")
    pedido=numero_pedido()
    pedido+=1
    with open ("pedido.csv", "w", newline="") as archivo:
        escritor_csv=csv.writer(archivo)
        escritor_csv.writerow(
            ["pedido","cliente","direccion","sector","saco_5","saco_10","saco_20"])
        escritor_csv.writerows(lista_de_pedidos)
    # no me funciona el archivo csv
    try:
        cliente=input("ingrese su nombre y apellido: ")
        direccion=input("ingrese su direccion: ")
        sectores=input("ingrese su sector o comuna: ")
        saco_5= int(input("ingrese cuantos sacos de 5 kg quiere: "))
        saco_10= int(input("ingrese cuantos sacos de 10 kg quiere: "))
        saco_20= int(input("ingrese cuantos sacos de 20 kg quiere: "))
    except ValueError:
        print("ingrese todos los datos")
    nuevo_pedido=[pedido,cliente,direccion,sectores,saco_5,saco_10,saco_20]
    lista_de_pedidos.append(nuevo_pedido)
    with open ("pedido.csv", "w", newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        escritor_csv.writerow(lista_de_pedidos)
    #no me funciona append
    print(archivo)

def listar_pedidos():
    with open("pedido.csv", "r", newline='') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            print(f"{fila[0]}\t{fila[1]}\t{fila[2]}\t{fila[3]}\t{fila[4]}\t{fila[5]}\t{fila[6]}")
            #no imprime los datos del archivo csv

def imprimir():
    sect=input("ingrese el sector a buscar: ")
    for sect in sectores:
        if sect!= sectores:
            print("sector no encontrado")
            
        for sect.join in archivo:
            secto=(f"{sect[0]},cliente:{sect[1]},direccion:{sect[2]}, sector:{sect[3]},saco de 5kg:{sect[4]}, saco de 10kg:{sect[5]},saco de 20kg:{sect[6]}")
        with open("hoja.txt", "w") as file:
            file.write(secto)
        with open("hoja.txt", "r") as file:
            contenido = file.read()
            print(contenido)
        #todavia nose porque me las pide como variable y como hacer que solo salgan las del sector especifico
        #no me acuerdo como se usa el join, pero lo useen la formativa y ahi me resulto
def menu():
    print(f"Bienvenido a CatPremium \n")
    print("-"*20)
    print("menu de opciones: ")
    print("1. registrar pedido")
    print("2. listar todos los pedidos")
    print("3. imprimir hoja de ruta")
    print("4. salir del programa")
    
    validar=True
    while validar:
         opc=int(input("ingrese la opcion a realizar: "))
         if opc==1:
            registrar_pedido()
            print("muchas gracias por registrar tu pedido")
            os.system("cls")
            time.sleep(1)
         elif opc==2:
            listar_pedidos()
            time.sleep(1)
         elif opc==3:
            imprimir()
            time.sleep(1)
         elif opc==4:
            print("muchas gracias por usar este programa, bai")
            validar=False
            break
         else:
            print("opcion invalida, selecione una entre 1 y 4")
            
            
menu()