import os
clean="cls"
os.system(clean)

cant_kilos=0
camiones=0
valor_total=0
cant_kilos=0
camion=765000
camionkilos=450
transporte=100000
ok_nombre=True
compra=True
pedido= True
tienda= True

while tienda:
    os.system(clean)
    print("Bienvenido a la tienda de gas")
    try:
         while compra:
             #nombre cliente
             nombre_cliente=input("ingrese su nombre por favor: ")
             cant_dig=len(nombre_cliente)
             if cant_dig>=3:
                 print("bienvenido sr/sra",nombre_cliente)
             else:
                 print("su nombre tiene que tener mas de 3 caracteres")
                 continue

             while ok_nombre:
                 #telefono cliente
                 telefono=input("ingrese su numero de telefono: ")
                 cant_dig2=len(telefono)
                 if cant_dig2>=8 and cant_dig2<=10:
                     print("su numero de telefono es:", telefono)
                     break
                 else:
                     print("su numero de telefoo tiene que tener entre 8 y 9 digitos")
                     continue
            
             while pedido:
                 #hacer pedido
                 os.system(clean)
                 print("Que desea comprar:")
                 print(f" camion completo con 450 kilos = $ {camion} pesos \n si pide menos de 450 kilos = $1700 por kilo + $100000 de transporte ")
                 pedido_completo=input("desea pedir uno o mas camiones completos?  si=1 no=2  ")
                 if pedido_completo=="1":
                     # pedido de camiones completos
                     camiones=int(input("cuantos camiones desea pedir? "))
                     valor_total=camion*camiones
                     cant_kilos=camiones*camionkilos
                     print(f"Detalle del pedido")
                     print(f"Cliente: {nombre_cliente} \n Telefono: {telefono} \n Cantidad de kilos: {cant_kilos} \n Camiones: {camiones} \n Valor total: {valor_total}")
                 elif pedido_completo=="2":
                     kilos=int(input("cuantos kilos desea pedir? "))
                     if kilos>450:
                         #pedido mas de 1 camion
                         entero=kilos//450
                         resto=kilos%450
                         valor_total=resto*1700+entero*camion+transporte
                         camiones+=entero
                         cant_kilos+=kilos
                         print(f"Detalle del pedido")
                         print(f"Cliente: {nombre_cliente} \n Telefono: {telefono} \n Cantidad de kilos: {cant_kilos} \n Camiones: {camiones} \n Valor total: {valor_total}")
                     elif kilos<450:
                         #pedido menos de 1 camion
                         valor_total=kilos*1700+transporte
                         cant_kilos+=kilos
                         camiones+=1
                         print(f"Detalle del pedido")
                         print(f"Cliente: {nombre_cliente} \n Telefono: {telefono} \n Cantidad de kilos: {cant_kilos} \n Camiones: {camiones} \n Valor total: {valor_total}")
                 else:
                     print("ingrese una opcion valida")
                 #hacer otro pedido
                 op=input("desea hacer otro pedido? si=1  no=2 ")
                 if op=="1":
                     os.system(clean)
                     cant_kilos=0
                     camiones=0
                     valor_total=0
                     cant_kilos=0
                     camion=765000
                     camionkilos=450
                     transporte=100000
                     continue
                 elif op=="2":
                  print("MUCHAS GRACIAS POR SU COMPRA, ADIOS")
                  pedido=False
         compra=False
    except ValueError:
         print("datos invalidos")
tienda= False