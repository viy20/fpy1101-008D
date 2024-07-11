import csv
import time
from random import randint

# Genera un número de pedido inicial aleatorio entre 1 y 1000
pedido_inicial = randint(1, 1000)

# Lista inicial de pedidos (temporal para pruebas)
lista_de_pedidos = [
    [pedido_inicial, "juan", "av lo blanco", "san bernardo", 1, 2, 1]
]

# Función para generar un nuevo número de pedido incremental
def numero_pedido():
    global pedido_inicial
    pedido_inicial += 1
    return pedido_inicial

# Función para registrar un nuevo pedido
def registrar_pedido():
    print("Registrar pedido")
    pedido = numero_pedido()
    cliente = input("Ingrese su nombre y apellido: ")
    direccion = input("Ingrese su dirección: ")
    sector = input("Ingrese su sector o comuna: ")
    try:
        saco_5 = int(input("Ingrese cuántos sacos de 5 kg quiere: "))
        saco_10 = int(input("Ingrese cuántos sacos de 10 kg quiere: "))
        saco_20 = int(input("Ingrese cuántos sacos de 20 kg quiere: "))
    except ValueError:
        print("Ingrese un número válido para los sacos.")
        return
    
    nuevo_pedido = [pedido, cliente, direccion, sector, saco_5, saco_10, saco_20]
    lista_de_pedidos.append(nuevo_pedido)

    # Escribir el nuevo pedido en el archivo CSV
    with open("pedido.csv", "w", newline="") as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerow(nuevo_pedido)

    print("Pedido registrado correctamente.\n")

# Función para listar todos los pedidos
def listar_pedidos():
    print("Listado de pedidos:")
    headers = ["Pedido", "Cliente", "Dirección", "Sector", "Sacos 5kg", "Sacos 10kg", "Sacos 20kg"]
    print("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}".format(*headers))

    # Mostrar cada pedido en lista_de_pedidos
    for pedido in lista_de_pedidos:
        print("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}".format(*pedido))

    
    # Leer los pedidos del archivo CSV
    try:
        with open("pedido.csv", "r", newline="") as archivo_csv:
            lector_csv = csv.reader(archivo_csv)
            next(lector_csv)  # Saltar la primera fila (encabezados) en el archivo CSV
            for fila in lector_csv:
                print("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}".format(*fila))
    except FileNotFoundError:
        print("No se encontró el archivo 'pedido.csv'.")
    except Exception as e:
        print(f"Error al intentar leer el archivo CSV: {e}")

# Función para eliminar un pedido por número de pedido
def eliminar_pedido():
    numero_pedido_eliminar = int(input("Ingrese el número de pedido que desea eliminar: "))
    
    # Buscar el pedido en lista_de_pedidos y eliminarlo
    for pedido in lista_de_pedidos:
        if pedido[0] == numero_pedido_eliminar:
            lista_de_pedidos.remove(pedido)
            print(f"Pedido número {numero_pedido_eliminar} eliminado de lista_de_pedidos.")
            break
    else:
        print(f"No se encontró el pedido número {numero_pedido_eliminar} en lista_de_pedidos.")
        return
    
    # Actualizar el archivo CSV sin el pedido eliminado
    try:
        with open("pedido.csv", "w", newline="") as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(["Pedido", "Cliente", "Dirección", "Sector", "Sacos 5kg", "Sacos 10kg", "Sacos 20kg"])
            for pedido in lista_de_pedidos:
                escritor_csv.writerow(pedido)
            print(f"Archivo 'pedido.csv' actualizado sin el pedido número {numero_pedido_eliminar}.")
    except Exception as e:
        print(f"Error al intentar actualizar el archivo CSV: {e}")

# Función para imprimir la hoja de ruta por sector
def imprimir_hoja_ruta():
    sector = input("Ingrese el sector a buscar: ").lower()
    encontrados = [pedido for pedido in lista_de_pedidos if sector in pedido[3].lower()]

    if encontrados:
        print(f"Hoja de ruta para el sector '{sector}':\n")
        headers = ["Pedido", "Cliente", "Dirección", "Sector", "Sacos 5kg", "Sacos 10kg", "Sacos 20kg"]
        print("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}".format(*headers))
        for pedido in encontrados:
            print("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}".format(*pedido))

        with open(f'hoja_ruta_sector_{sector}.txt', 'w') as archivo_txt:
            archivo_txt.write(f"Hoja de ruta para el sector '{sector}':\n\n")
            archivo_txt.write("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}\n".format(*headers))
            for pedido in encontrados:
                archivo_txt.write("{:<10} {:<20} {:<20} {:<15} {:<10} {:<10} {:<10}\n".format(*pedido))
        
            print(f"Hoja de ruta guardada en 'hoja_ruta_sector_{sector}.txt'")
    else:
        print(f"No se encontraron pedidos para el sector '{sector}'.")

# Función principal del programa
def menu():
    print("Bienvenido a CatPremium\n")
    while True:
        print("-" * 20)
        print("Menú de opciones:")
        print("1. Registrar pedido")
        print("2. Listar todos los pedidos")
        print("3. Imprimir hoja de ruta por sector")
        print("4. Eliminar pedido")
        print("5. Salir del programa")
        
        try:
            opc = int(input("Ingrese la opción a realizar: "))
        except ValueError:
            print("Por favor, ingrese un número válido.")
            continue
        
        if opc == 1:
            registrar_pedido()
            time.sleep(1)
        elif opc == 2:
            listar_pedidos()
            time.sleep(1)
        elif opc == 3:
            imprimir_hoja_ruta()
            time.sleep(1)
        elif opc == 4:
            eliminar_pedido()
            time.sleep(1)
        elif opc == 5:
            print("Gracias por usar este programa. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Seleccione una opción del 1 al 5.")

menu()
