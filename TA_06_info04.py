

# interfaz, usuario con clave
#Página de ingreso de productos
#dataframe bodega
#pagina de compras
#dataframe compras
# librerías para manejar base de datos
import pandas as pd
import numpy as np
import os
import csv


# función para crear la pnatalla de compras e ingreso de productos
def compra():
   while True:
   
     N=int(input("ingrese la cantidad total de productos comprados: "))
     empresa=[]
     producto=[]
     precio=[]
     unidad =[]
     fcompra =[]
     Fv =[]
     for i in range(N):
       empresa1 = input("\ningrese el nombre de la empresa: ")
       producto1= input("\ningrese el nombre del producto: ")
       precio1= input("\ningrese el precio de la paca: ")
       unidad1= input("\ningrese la cantidad de unidades de la paca: ")
       fcompra1= input("\ningrese la fecha de compra: ")
       Fv1= input("\ningrese la fecha de vencimiento: ")
       print("\n\n")
       empresa.append(empresa1)
       producto.append(producto1)
       precio.append(precio1)
       unidad.append(unidad1)
       fcompra.append(fcompra1)
       Fv.append(Fv1)
       compras=(empresa, producto, precio, unidad, fcompra, Fv)
       os.system('clear')
       print("\t\t\t\t PÁGINA DE COMPRAS \n\n")
       print("\t\t\t\t Productos comprados \n\n")
       df= pd.DataFrame(compras )
       print("\t\t\t\t Productos comprados \n\n")
       df1=pd.DataFrame.transpose(df)
       df1.columns=['empresa', 'producto', 'precio',' unidad',' fcompra', 'Fv']
       print(df1)
       df1.to_csv('compras.csv', mode="a", index="", header="")
     else:
        break
# Función para manejar el total de productos adquiridos    
def total():
      while True:
       print("\n\n\t\tTOTAL ACUMULADO EN COMPRAS\n\n")
       L1=pd.read_csv('compras.csv') #lee la base datos de compras
       print(L1)
       #with open("compras.csv", newline="") as file:
       #  reader=csv.reader(file,delimiter=",")
       #  for row in reader:
       #    print(row)
       print("\n\n")
       break 
os.system('clear')
print("\t\t\t\t PÁGINAS DE COMPRAS \n\n")
# función para activar el submenu de entrada de la página compras
def menu():
    
    print("Selecciona una opción \n")
    print("\t1 - Registro de compras ")
    print("\t2 - registro total acumulado")
    print("\t3 - Otras opciones")
    print("\t9 - Terminar con uso de menu")
          
# Se crea un una iteración con while mientras se cumpla la condición
while True:
      menu()
      opcionMenu = input("\n Inserte el número de la opción: ")
                  
      if opcionMenu == "1":
          print("\n\nhola\n\n")
          compra()
      #else:  
          #break
          print("\n regrese a menú e intentelo de nuevo\n")  

        
      elif opcionMenu == "2":
             total()
      else:                     
       break
'''
      elif opcionMenu == "3":

              print("")
              input("\nSe ha pulsado la opción 2...\n pulsa enter para continuar")  
       else:
         break
            
'''  
'''

      elif opcionMenu == "9":  
             os.system('clear')
      else:
        break
            #print("")
            #input("No has elegido ningún valor correcto...\n pulsa enter para continuar")
'''
