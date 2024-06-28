import os
import time
os.system("cls")
time.sleep 

lista_trabajadores = [
    #el 00000 es sueldo bruto solo que no pude ponerlo porque me da error de tipo :v
    ["trabajador","cargo",00000],
    ["juan vasquez", "CEO", 1200000],
    ["amanda garrido", "desarrollador", 890000],
    ["alejandro gomez", "desarrollador", 890000],
    ["valentina marin", "analista de datos", 1000000],
    ["daniel gonzalez", "analista de datos", 1000000]
]

cargos = ["CEO", "desarrollador", "analista de datos"]


def calcular_sueldo_liquido(sueldo_bruto):
    sueldo_bruto = float(sueldo_bruto)
    desc_salud = sueldo_bruto * 0.07
    desc_afp = sueldo_bruto * 0.12
    sueldo_liquido = sueldo_bruto - desc_salud - desc_afp
    return desc_salud, desc_afp, sueldo_liquido


def registrar_trabajador():
    print(" registrar trabajador")
    try:
        nombre = input("ingrese nombre y apellido del trabajador: ")
        cargo = input(f"ingrese cargo del trabajador ({', '.join(cargos)}): ")
        while cargo.lower() not in map(str.lower, cargos):
            print(f"cargo '{cargo}' no válido. los cargos válidos son: {', '.join(cargos)}")
            cargo = input(f"ingrese cargo del trabajador ({', '.join(cargos)}): ")
        sueldo_bruto = float(input("ingrese sueldo bruto del trabajador: "))
    except ValueError:
        print("por favor ingrese todos los datos")
    
    lista_trabajadores.append([nombre, cargo, sueldo_bruto])
    print("trabajador registrado exitosamente.")


def listar_trabajadores(lista):
     print("Lista de trabajadores\n")
     for trabajador in lista:
        print(trabajador[0], "--", trabajador[1], "--", trabajador[2])



def imprimir_planilla():
    print("imprimir planilla de sueldos")
    print("cargos disponibles:", ', '.join(cargos))
    seleccion = input("ingrese el cargo para generar la planilla (o 'todos' para imprimir todos): ").lower()
    
    if seleccion == "todos":
        texto = "planilla_todos.txt"
        with open("texto.txt", "w") as f:
            f.write("planilla de sueldos - todos los trabajadores\n")
            for trabajador in lista_trabajadores:
                desc_salud, desc_afp, sueldo_liquido = calcular_sueldo_liquido(trabajador[2])
                f.write(f"Nombre y Apellido: {trabajador[0]},\t Cargo: {trabajador[1]},\t Sueldo Bruto: ${trabajador[2]:,.2f},\n "
                        f"Descuento Salud: ${desc_salud:.2f},\t Descuento AFP: ${desc_afp:.2f},\t Sueldo Líquido: ${sueldo_liquido:.2f}\n\n")
        print(f"Se ha generado el archivo '{texto}' con la planilla completa.")

        try:
            with open("texto.txt", "r") as f:
                contenido = f.read()
                print(f"\nContenido del archivo '{texto}':")
                print(contenido)
        except FileNotFoundError:
            print(f"No se encontró el archivo '{texto}'.")


    elif seleccion in map(str.lower, cargos):
        texto = f"planilla_{seleccion.replace(' ', '_')}.txt"
        with open("texto.txt", "w") as f:
            f.write(f"PLANILLA DE SUELDOS - CARGO: {seleccion.upper()}\n")
            for trabajador in lista_trabajadores:
                if trabajador[1].lower() == seleccion:
                    desc_salud, desc_afp, sueldo_liquido = calcular_sueldo_liquido(trabajador[2])
                    f.write(f"Nombre y Apellido: {trabajador[0]}, Cargo: {trabajador[1]}, Sueldo Bruto: ${trabajador[2]:,.2f}, "
                            f"Descuento Salud: ${desc_salud:.2f}, Descuento AFP: ${desc_afp:.2f}, Sueldo Líquido: ${sueldo_liquido:.2f}\n")
        print(f"Se ha generado el archivo '{texto}' con la planilla del cargo '{seleccion}'.")

        try:
            with open("texto.txt", "r") as f:
                contenido = f.read()
                print(f"\nContenido del archivo '{texto}':")
                print(contenido)
        except FileNotFoundError:
            print(f"No se encontró el archivo '{texto}'.")
    else:
        print("Cargo no válido.")


def menu():
    menuabierto=True
    while menuabierto:
        print("\n")
        print("menu para trabajadores\n")
        print("1. registrar trabajador")
        print("2. listar todos los trabajadores")
        print("3. imprimir planilla de sueldos")
        print("4. salir del programa")
        
        opcion = input("Ingrese el número de la opción que desea ejecutar: ")
        
        if opcion == "1":
            os.system("cls")
            registrar_trabajador()
            time.sleep(1)
            os.system("cls")

        elif opcion == "2":
            listar_trabajadores(lista_trabajadores)
            time.sleep(1)

        elif opcion == "3":
            os.system("cls")
            imprimir_planilla()
            time.sleep(1)

        elif opcion == "4":
            print("muchas gracias por usar este programa, adios")
            menuabierto=False
        else:
            print("opción no válida. Por favor, ingrese un número del 1 al 4.")

menu()
