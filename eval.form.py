import os
os.system("cls")

valor_totalpedido=0
valordescuento=0
totalproductos=0
total=0
pikachu=0
otaku=0
pulpo=0
anguila=0
opc=0

print("bienvenido a sushi roll")
pedido=input("¿desea hacer un pedido? si=x no=1: ")

while pedido== "x":
     print("1.Pikachu Roll $4500      2.Otaku Roll $5000       3.Pulpo Venenoso Roll $5200     4.Anguila Eléctrica Roll $4800  ")
     opc=int(input("¿que opcion desea pedir?  "))
     cant=int(input("¿que cantidad desea de ese roll?  "))
     if opc==1:
         valor_totalpedido+=(4500*cant)
         pikachu+=1*cant
         totalproductos+=1*cant
     elif opc==2:
          valor_totalpedido+=(5000*cant)
          otaku+=1*cant
          totalproductos+=1*cant
     elif opc==3:
          valor_totalpedido+=(5200*cant)
          pulpo+=1*cant
          totalproductos+=1*cant
     elif opc==4:
          valor_totalpedido+=(4800*cant)
          anguila+=1*cant
          totalproductos+=1*cant
     else:
          print(("opcion no valida"))
     pedido=input("desea hacer otro pedido? si=x no=1 : ")

            


codigo=input("usted tiene codigo de descuento? si=1  no=2  ")

while codigo=="1":
     descuento=input("ingrese codigo de descuento:  ")
     if descuento=="soyotaku":
      print("usted tiene un descuento del 10% ")
      total=valor_totalpedido*0.9
      valordescuento= valor_totalpedido*0.1
     else:
         print ("codigo invalido")
         total=valor_totalpedido
         break


print("******************************")
print(f"total de productos: {totalproductos} ")
print("******************************")
print(f"1.pikachu roll: {pikachu}")
print(f"2.otaku roll: {otaku}")
print(f"3.pulpo venenoso roll: {pulpo}")
print(f"4. anguila electrica roll: {anguila}")
print("******************************")
print(f"sub total por pagar: {valor_totalpedido}")
print(f"descuento por codigo: {valordescuento} ")
print(f"TOTAL: {total}")