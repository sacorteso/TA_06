
#  ADVERTENCIA
# utilizar clave gabrielawad

# interfaz, usuario con clave
#Página de ingreso de productos
#dataframe bodega
#pagina de compras
#dataframe compras

# librerías para manejar base de datos
from datetime import date as dt
from datetime import datetime as dtt
import pandas as pd # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os           # Librerías para realizar funciones internas del software
import csv          # Librería para manipular archivos excel y con extensión .csv 

print("\t\t\t\t PÁGINA DE COMPRAS \n\n")

today = dt.today()
print(today)
# Para activar la autorización de claves para funcionamiento de la aplicación
#with open('CLAVES/Clave.txt', 'r') as Cla:   # se lee base de datos con las claves de los empleados
#       L2 = Cla.readlines()  
#       print(L2) 
L2=pd.read_csv("CLAVES/Clave.csv")    # Lee el archivo csv donde están las claves guardadas
L3=pd.DataFrame(L2)    # las claves leídas se covieten e dataframe para facilitar su uso
L=0                    # se define constante axiliar para ser utilizada en while del menú principal 
L4=0                   # se define constante axiliar para ser utilizada en while de ingreso de clave
z=5                    #  se define constante axiliar para ser utilizada en while del menú principal
while(z!=L4):          # ciclo para comparar las claves que se ingresan con la calves guardadas en la base de datos
 z= input("ingrese la clave de usuario:  ") # ingreso de clave para ser comparada
 print("\n\n\t\t\tclave de usuario no válida\n\n") # mensaje para que se corrija la clave
 
 for T in range(len(L3)):                   # ciclo para comparar con todas las claves con la base de datos
     L4=L3.iloc[T,0]                        # Permite hallar una clave  en una posición determinada
     if (z==L4):                            # compara la clave del dataframe con la clave ingresada
       print("usuario identificado")        # si las claves coinciden imprime mensaje positivo
       L=5                                  # constante auxiliar que servirá para activar el menú principal
       break 



def ingresoproductosbodega():  # Se crea función para ingresar los productos a la bodega
  while True:                  # ciclo while para ingresar los productos con sus respectivos datos

     ig=1                      # constante para validar variable
     #listas definidas para el dataframe de bodega
     distribuidor=[]           # para crear lista vacía para distribuidor
     producto=[]               # para crear lista vacía para producto
     referencia=[]             # para crear lista vacía para refernecia
     precio=[]                 # para crear lista vacía para precio   
     unidad=[]                 # para crear lista vacía para unidad
     valorxunidad=[]           # para crear lista vacía para valorxunidad
     fecompra=[]               # para crear lista vacía para fecha de compra

     for i in range(ig):       # ciclo for para ingressar los datos a las respectivas listas

      #ingreso de especificaciones de los productos
       distribuidor1=input("\ningrese el nombre del distribuidor: ") # se ingresa el nombre del distribuidor
       producto2= input("\ningrese el nombre del producto: ")        # se ingresa el nombre del producto
       refproducto2= input("\ningrese la referencia del producto: ") # se ingresa la referencia del producto
       precio2= input("\ningrese el precio de la paca: ")            # se ingresa el precio por paca del respectivo producto
       unidad2= input("\ningrese la cantidad de unidades de la paca: ")  # se ingresa la cantidad de unidades de la paca
       fecompra1= input("\ningrese la fecha de compra (formato: año mes dia sin espacios): ") # Se ingresa la fecha de la compra
       vxunidad = int (precio2)/int (unidad2)  # se hace la operación para halar el valor individual del producto.
     

      
#las variables que ingrese el usuario se agregaran a las listas

       distribuidor.append(distribuidor1) # sirve para anexar nuevos valores a la lista de distribuidor
       producto.append(producto2)         # sirve para anexar nuevos valores a la lista de producto
       referencia.append(refproducto2)    # sirve para anexar nuevos valores a la lista de referencia
       precio.append(precio2)             # sirve para anexar nuevos valores a la lista de precio
       unidad.append(unidad2)             # sirve para anexar nuevos valores a la lista de unidad
       fecompra.append(fecompra1)         # sirve para anexar nuevos valores a la lista de fecha de compra
       valorxunidad.append(vxunidad)      # sirve para anexar nuevos valores a la lista de valor x unidad


#las listas se convierten en datafreme
       bodega1=(distribuidor, producto, referencia, precio, unidad, valorxunidad,fecompra ) # se crea una nueva lista para que sea interpretada por el dataframe df1
       os.system('clear')                      # Sirve para limpiar la pantalla
       print("\t\t\t\t PÁGINA DE BODEGA \n\n") # para mostrae el titulo de la página bodega
       df1= pd.DataFrame(bodega1)              # se crea el dataframe Bodega para manipular operaciones con datos más facilmente.
       print("\t\t PRODUCTOS EN BODEGA \n\n")  # se crea el subtitulo de productos de bodega
       df2=pd.DataFrame.transpose(df1)         # se crea un nuevo dataframe para transponer los datos de df1, para una mejor visualización
       df2.columns=['distribuidor', 'producto','referencia', 'precio', 'unidad', 'valorxunidad', 'fecompra'] # Se anexan los titulos de las columnas del dataframe df2
       print(df2)                              # Se imprime los resultados del dataframe df2
       df2.to_csv('BDATOS/bodega1.csv', mode="a", index="", header="") # sirve para grabar los datos en la base de datos correspondiente
       print("\n\n\t\tTOTAL ACUMULADO EN COMPRAS\n\n")   # se imprime titulo de  submenú acumulados de compras
       L5=pd.read_csv('BDATOS/bodega1.csv')                     # lee la base datos de compras
       print(L5) 
     else:                                     # Se crea la segunda opción alternativa
       break                                   # fInaliza este ciclo con el for


# función para crear la pnatalla de compras e ingreso de productos
def compra():                                 # se define la función para compras
   while True:                                # se crea un ciclo white para el ingreso de los productos
   
     N=int(input("ingrese la cantidad total de productos comprados: ")) # sirve para ingresar el número de la opciones en el menú
     empresa=[]                               # se crea una lista vacía para ingresar el nombre de la empresa
     producto=[]                              # se crea una lista vacía para ingresar el nombre del producto
     precio=[]                                # se crea una lista vacía para ingresar el precio de la paca por producto
     unidad =[]                               # se crea una lista vacía para ingresar las unidades de la paca
     fcompra =[]                              # se crea una lista vacía para ingresar la fecha de la compra
     Fv =[]                                   # se crea una lista vacía para ingresar la feha de vencimiento


     for i in range(N):                       # se crea un ciclo for para ingrsar los datos de los productos que entran a la bodega
       empresa1 = input("\ningrese el nombre de la empresa: ") # se ingresa el nombre de la empresa
       producto1= input("\ningrese el nombre del producto: ")  # se ingresa el nombre del producto
       precio1= input("\ningrese el precio de la paca: ")      # se ingresa el precio del rpoducto por paca
       unidad1= input("\ningrese la cantidad de unidades de la paca: ")    # se ingresa la cantidad de unidades de la paca del respectivo producto
       fcompra1= input("\ningrese la fecha de compra: ")       # se ingresa la fecha de la compra
       Fv1= input("\ningrese la fecha de vencimiento: ")       # se ingresa la fecha del vencimiento del producto
       print("\n\n")                                           # se crean saltos de linea para mejor presentacón
       empresa.append(empresa1)  # sirve para anexar nuevos valores a la lista de distribuidor
       producto.append(producto1)# sirve para anexar nuevos valores a la lista de distribuidor
       unidad.append(unidad1)    # sirve para anexar nuevos valores a la lista de distribuidor
       precio.append(precio1)    # sirve para anexar nuevos valores a la lista de distribuidor
       unidad.append(unidad1)    # sirve para anexar nuevos valores a la lista de distribuidor
       fcompra.append(fcompra1)  # sirve para anexar nuevos valores a la lista de distribuidor
       Fv.append(Fv1)            # sirve para anexar nuevos valores a la lista de distribuidor 
       compras=(empresa, producto, precio, unidad, fcompra, Fv) # se crea una nueva lista para que sea interpretada por el dataframe df1
       os.system('clear')        # para limpiar la pantalla
       print("\t\t\t\t PÁGINA DE COMPRAS \n\n")    # imprime el titulo de la sección compras
       print("\t\t\t\t Productos comprados \n\n")  # imprime el titulo del submenú productos comprados
       df= pd.DataFrame(compras )                  # se crea dataframe para manipular más facilemnte los datos de compras
       df1=pd.DataFrame.transpose(df)              # se crea un nuevo dataframe para transponer los datos de df, para una mejor visualización
       df1.columns=['empresa', 'producto', 'precio',' unidad',' fcompra', 'Fv']
       print(df1)                                  # Se imprime los resultados del dataframe df1
       df1.to_csv('BDATOS/compras.csv', mode="a", index="", header="")   # sirve para grabar los datos en la base de datos correspondiente
     else:                                         # Se crea la segunda opción alternativa
        break                                      # fInaliza este ciclo con el for


# Función para manejar el total de productos adquiridos    
def total():                    # se crea una función para manejar los productos adquiridos
      while True:               # se crea un ciclos while para mostrar la actualización del total de los productos comprados
       print("\n\n\t\tTOTAL ACUMULADO EN COMPRAS\n\n")   # se imprime titulo de  submenú acumulados de compras
       L1=pd.read_csv('BDATOS/compras.csv')                     # lee la base datos de compras
       print(L1)                                         # imprime el dataframe de la base de datos de compras
       #with open("compras.csv", newline="") as file:
       #  reader=csv.reader(file,delimiter=",")
       #  for row in reader:
       #    print(row)
       print("\n\n")                                     # se crea saltos de linea
       break                                             # se finaliza este ciclo while
os.system('clear')                                       # sirve para limpiar la pantalla
print("\t\t\t\t PÁGINA PRINCIPAL \n\n")                  # se imprime el titulo de la página del menu del manejo operativo del negocio

# función para activar el submenu de entrada de la página compras
def menu():                                              # se crea un menu para el manejo operativo del negocio
    
    print("Selecciona una opción \n")                    # se imprime mendsaje del menú
    print("\t1 - Registro de compras ")                  # se imprime registro de compras
    print("\t2 - registro total acumulado")              # se imprime registro total acumulado
    print("\t3 - ingreso de bodega")                     # se imprime ingreso abodega
    print("\t9 - Terminar con uso de menu")              # se imprime finalizacón de menú
          
# Se crea un una iteración con while mientras se cumpla la condición
while True:                                              # se activa el ciclo while para activar el menú
      menu()                                             # se activa la función menú
      opcionMenu = input("\n Inserte el número de la opción: ")   # sirve para ingresar el valor de la opción seleccionada
                  
      if opcionMenu == "1":                              # Para activar la función compra
          print("\n\nhola\n\n")                          # imprime mensaje de saludo
          compra()                                       # la función compra se ejecuta
     
           

        
      elif opcionMenu == "2":                            # Para activar la función total
             total()                                     # se ejecuta la función total
      

      elif opcionMenu == "3":                            # se activa la función bodega
             print("¿deseas ingresar productos en bodega?")  # mensaje para confirmar la opercación que se va  a realizar
             input("presiona enter para continuar:")         # se confirma la operación
             ingresoproductosbodega()                        # se ejecuta la función ingresproductosbodega
        
     
 
      elif opcionMenu == "9":                            # se elige la activa la opción finalizar menú
          print("\n\n\t\tSistema finalizado")                    # mensaje que confirma la finalización del menu
          break                                          # se finaliza el ciclo if del menú
            

