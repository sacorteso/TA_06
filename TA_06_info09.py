from datetime import date as dt
from datetime import datetime as dtt
from datetime import timedelta
import pandas as pd  # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os  # Librerías para realizar funciones internas del software
import csv  # Librería para manipular archivos excel y con extensión .csv
import time
#import tkinter as tk
import matplotlib.pyplot as plt
import openpyxl




os.system('clear') 
print("\n\nPÁGINA PRINCIPAL DE ADMINISTRADOR")
print("\n\n")
today = dt.today()
print(today)
print("\n\n")
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


#informe 3
with open('CLAVES/Global.txt', 'r') as Ltexto:
  L = Ltexto.readline()
# inicio de la función menú
def menu():
    1
    print("Selecciona una opción \n")
    print("\t1   -   Cambio de clave Global")
    print("\t2   -   Login y clave para nuevo empleado")
    print("\t2.1 -   Base de dtos de empleados")
    print("\t3   -   Otras opciones")
    print("\t9   -   Terminar con uso de menu")
          
# Se crea un una iteración con wile mientras se cumpla la condición

while True:
      menu()
      opcionMenu = input("\n Inserte el número de la opción: ")
      
      
      Ltexto.close()
      if opcionMenu == "1": # Opción para cambiar la clave global
          print("\nhola\n") # saludo
          input("Se ha pulsado la opción 1...\n pulsa enter para continuar") #confirmación que lselecciono opción 1
          T = input("\nIngrese clave Global: ") #solicitud de ingreso de clave global
          if L == T: # Comparador de claves
            K=input("\nIngrese nueva clave: ") # solicitud para nueva clave
            K1=input("\nIngrese nuevamente la nueva clave: ") # Solicitud para nueva clave
            if K == K1: # compara que la nueva clave si la recuerda el usuario
              L = K1 # variable adicional
              Ltexto=open("CLAVES/Global.txt","w+") # se activa la función para eliminar la clave vieja del archivo txt
              Ltexto.write(L) # se escribe la nueva clave global en el archivo txt
              Ltexto.close() # se cierra el archivo txt que guarda la clave global.
              
              print(" \n Clave Global modificada\n") # anuncio que la clave global fue modificada
          else:
            break               # opción si no se ingresa la clave global correcta.
            print("\nregrese a menú e intentelo de nuevo\n")  


          
      elif opcionMenu == "2": # Opción para ingresar los datos de los empleados, generar login de usuario y claves.
          
         
          input("\nSe ha pulsado la opción 2...\n pulsa enter para continuar ") 
          k= input("\nIngrese clave Global: ") # ingresa clave global para permiti hacer actualizaciones
          
         
          while(L==k):# permite crear un cilclo para ingresar nuevos empleados
            for i in range(1):
               nombre= input("\ningrese el nombre: ")  # para ingresar nombre del empleado
               apellido= input("\nIngrese el apellido: ") # para ingresar el apellido
               clave = creaciondecontrase() # para ingresar una clave manual a gusto del empleado
               usuario= nombre[0:3]+apellido[0:3] #+str(i) # permite creae el login de usuario
               os.system('clear') # limpia la pantalla
               listacontras.append(clave)
               
               # confirma visualmente los datos ingrsados por el administrador
               print("\n", "Su nombre es: ", nombre,"\n")
               print("\n", "Su apellido es: ", apellido, "\n")
               print("\n", "Su clave es: ", clave, "\n")
               print("\n", "Su Login es: ", usuario,"\n")
               
               # para crear bases datos (nombre) para dataframe
               LNombre=open("BDATOS/Nombre.txt", "a+")
               LNombre.write(nombre)
               LNombre.write("\n")
               LNombre.close()
               with open('BDATOS/Nombre.txt', 'r') as Nom:
                    LN = Nom.readlines()
                    #print(LN)
               LNombre.close()
                            
               # para crear bases datos (apellido) para dataframe                
               LApellido=open("BDATOS/Apellido.txt", "a+")
               LApellido.write(apellido)
               LApellido.write('\n')
               LApellido.close()
               with open('BDATOS/Apellido.txt', 'r') as Ape:
                    LA = Ape.readlines()
                   # print(LA)
               LApellido.close()
                            
               # para crear bases datos (clave de usuario) para dataframe
               LClave=open("CLAVES/Clave.txt", "a+")
               LClave.write(clave)
               LClave.write("\n")
               LClave.close()
               with open('CLAVES/Clave.txt', 'r') as Cla:
                    LC = Cla.readlines()
                   # print(LC)
               LClave.close()

               # para crear bases datos (login de usuario) para dataframe
               LUsuario=open("BDATOS/Usuario.txt", "a+")
               LUsuario.write(usuario)
               LUsuario.write("\n")
               LUsuario.close()
               with open('BDATOS/Usuario.txt', 'r') as Usu:
                    LU = Usu.readlines()
                    #print(LU,"\n")
                    print("\n")
               LUsuario.close()
            break
      elif opcionMenu == "2.1":      
               os.system('clear')                      # Sirve para limpiar la pantalla
               print("\t\t\t\t BASE DE DATOS CON LOS EMPLEADOS \n\n")   
               
               with open('BDATOS/Nombre.txt', 'r') as Nom: # se lee base da datos con los nombres
                    LN = Nom.readlines()                   # lista con los nombres
               with open('BDATOS/Apellido.txt', 'r') as Ape:# se lee base de datos con los apellidos
                    LA = Ape.readlines()                    # lista con los apellidos
               with open('CLAVES/Clave.txt', 'r') as Cla:   # se lee base de datos con las claves de los empleados
                    LC = Cla.readlines()                    # lista con las claves

               #Se crea DataFrame para los datos de los empleados           
               df= pd.DataFrame(list(zip(LN,LA,LC)), columns =['Nombre','Apellido','Clave'])
               print(df)
               
               break

      elif opcionMenu == "3":
              print("por el momento no hay opciones")
              input("\nSe ha pulsado la opción 3...\n pulsa enter para finalizar")
              break  
               
              # finalización del ciclo del menú
      elif opcionMenu == "9":
              print("fin del programa")
              input("\nSe ha pulsado la opción 9...\n pulsa enter para finalizar")
              break


  


def menu(): 
  #os.system('clear') #limpiar pantalla
  print("\n\n")
  tituloG = "PÁGINA PRINCIPAL DE ADMINISTRADOR"
  print(tituloG.center(100," "))
  print("\n\n")
                                           # se crea un menu para el manejo operativo del negocio
    
  print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
  print("                                  \t3 - Empleados ")                  # se imprime registro de compras
  print("                                  \t4 - Compras y Bodega")              # se imprime registro total acumulado
  print("                                  \t5 - Mostrador")  
  print("                                  \t6 - Ventas y Clientes") 
  print("                                  \t7 - Contabilidad") 
  print("                                  \t8 - Reportes") 
  print("                                  \t9 - Terminar con uso de menu")              # se imprime finalizacón de menú
          
# Se crea un una iteración con while mientras se cumpla la condición
while True: 
  menu()                                             # se activa la función menú
  opcionMenu = input("\n Inserte el número de la opción del menú: ")   # sirve para ingresar el valor de la opción seleccionada
  if opcionMenu == "3": 
    #os.system('clear') #limpiar pantalla
    print("\n\n") 
        
    subtitulo = " SUBMENÚ DE EMPLEADOS"
    print("\n\n")
    print(subtitulo.center(100," "))
    print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
    print("                                  \t3.1 - ")                  # se imprime registro de compras
    print("                                  \t3.2 - ")              # se imprime registro total acumulado
    print("                                  \t3.3 - ")  
    print("                                  \t3.4 - ") 
    print("                                  \t3.5 - ") 
    print("                                  \t3.6 - ") 
    print("                                  \t3.7 - ")
    print("                                  \t3.8 - ")
    print("                                  \t9   - ")              # se imprime finalizacón de menú
          
    opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
    if opcionmenu== "3.1":
      print("\n\nhola\n\n")                          # imprime mensaje de saludo
      #bodegacom()   
      #mensaje="HOLA"
      #os.system('clear') #limpiar pantalla
      print("\n\n")
      print("3.1".center(100," "))                                  # la función compra se ejecuta
        

       
    elif opcionmenu == "3.2":
          print("3.2")
                                                 # se ejecuta la función total
      

    elif opcionmenu == "3.3":                            # se activa la función bodega
             print("3.3")
            
    elif opcionmenu == "3.4":                            # se activa la función bodega
              print("3.4")
              

    elif opcionmenu == "3.5":                            # se activa la función bodega
             print("3.5")
           
              


    elif opcionmenu == "3.6":                            # se activa la función bodega
             print("3.6")
             
             

    elif opcionmenu == "3.7":                            # se activa la función bodega
             print("3.7") 
            
              

    elif opcionmenu == "3.8":                            # se activa la función bodega
             print("3.8") 
             

# informe 4
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
       break    
                                                # se finaliza este ciclo while

#informe 5
# Para cambiar el porcentaje de forma individual
def ganancia(): # Función para modificar el porcentaje de ganancia en las ventas de los productos.
  while True:   # Activa el ciclo para modificar el porcentaje de ganancia en las ventas de los productos.
    print("\n\n\t\tPÁGINA PARA CAMBIAR EL PORCENTAJE DE GANANCIA EN FORMA INDIVIDUAL") # Titulo para cambiar el porcentaje de ganancia del producto
    print("\n\n\t\tReferencia en productos en Bodega\n\n")      # Subtitulo para ver las referencia de los productos

    m2=pd.read_csv("BDATOS/mostrador.csv") # Para leer la base de datos mostrador
    m22=m2.iloc[:,0:2]                     # De la base de datos mostrador se escoge los nombres y las referencias de los productos                   
    print(m22)                             # Se imprime el nombre y la referencia de los productos

    g2=input("\n\n\n\ningrese la referencia del producto: ")  # mensaje para ingresar la referencia del producto
    g3= str(g2)                                               # se transforma el tipo de datos a string

    m5= m2[m2['Referencia']==g3]          # Se crea una lista para guardar las referencias elegidas
    print("\n\n\n\n   Datos de  Referencia ingresada \n\n",  m5) # Confirma que la referencia ingresada es seleccionada


    mg=input("\n\n\n\nIngrese el nuevo porcentaje de ganancia del producto: ")  # Mensaje para ingresar el nuevo porcentaje
    mg1= (mg)                                                                   # Se crea una lista con el nuevo porcentaje
    print("\n\n\n\n            Porcentaje de ganancia ingresado:",  mg1)        # Confirma que el porcentaje de ganancia ingresado es seleccionado


    float()           # se tranforma los datos a tipo float
    z1= 97            # Se crea una variable para operaciones matemáticas
    for TM in range(len(m2)):   # Se crea una iteración para revisar todas las referencias
     # ciclo para comparar con todas las claves con la base de datos
     #TM=m2.iloc[TM,5]
     #print(TM)                  # Permite hallar una clave  en una posición determinada
     if (m2.iloc[TM,1]==g3):     # Se crea un ciclo de confirmación de referencia seleccionada
          m2.iloc[TM, 5]=mg      # Se selecciona la columna de ganancia en la base de datos mostrador y se cambia por la nuevo porcentaje de ganancia
          m2.to_csv('BDATOS/mostrador.csv', mode="w",index="", header="True") # Se graba los nuevos datos en el archivo mostardor
          m2.iloc[TM, 6]= z1     # Se actualiza el precio de venta de los productos en mostrador
          m2=pd.read_csv("BDATOS/mostrador.csv") # Se lee la base de datos de mostrador
          z1=m2.iloc[TM,3]       # Se selecciona la columna precio de compra
          z2=m2.iloc[TM,5]       # Se selecciona la columna de ganancia de producto
          zz= (z1*z2/100)+z1     # Se calcula el precio de venta
          m2.iloc[TM,6]=zz       # Se actualiza el precio de venta en la base de datos mostrador
          m2.to_csv('BDATOS/mostrador.csv',mode="w", index="", header="True") # Se graba los nuevos datos de el archivo mostrador.
          #print(zz)
          
          aa5 =pd.read_csv("BDATOS/mostrador.csv")   # Se lee la base de datos mostardor con la información actualizada
          print(aa5)                                 # Se imprime la base de datos mostrador actualizada
                                                     # otra opción en el ciclo
    break                                             # cierra el ciclo


#listo para funcionamiento
# Para cambiar las unidades de forma individual
def unidades():  # función para elegir la cantidad de productos para la venta según la referencia
  while True:    # Activar el ciclo para elegir la cantidad de productos para la venta según la referencia
    os.system('clear') # para limpiar la pantalla
    print("\n\nPAGINA MOSTRADOR") # Titulo para la página principal de mostrador
    print("\n\n\t\t PAGINA PARA CAMBIAR LAS UNIDADES EN FORMA INDIVIDUAL") # subtitulos para cambiar las unidades en forma individual
    print("\n\n\t\t Referencia en productos en Bodega\n\n")   # Subtitulos para referencia

    mm2=pd.read_csv("BDATOS/mostrador.csv")   # Se lee base de datos mostrador
    LL5=pd.read_csv('BDATOS/bodega1.csv')     # Se lee la base de datos de bodega
    print(LL5)                                # Se imprime la bese de datos de bodega

    print("\n\n\n\n Mostrador actual")        # Se imprime mensaje
    print("\n\n",mm2)                         # Se imprime los productos que están listos para la venta


    g2=input("\n\n\n\nIngrese la referencia del producto: ") # Se imprime mensaje para referencia de producto
    g3=str(g2)                                               # se crea una variable tipo string


    g4=input("\n\ningrese la fecha de compra del producto: ")   # Se ingresa la fecha de compra del producto
    g5=int(g4)                                                  # Se convirta la variable anterior en una variable tipo entero
    m5= LL5[LL5['Referencia']==g3]                              # Se buscan las referencias correspondientes en el DataFrame
    m6= LL5[LL5['Fcompra']==g5]                                 # Se buscan la fecha de compra en el DataFrame
    os.system('clear')                                          # Se limpia la pantalla
    print("\n\n\n\nDatos de la bodega \n\n", m5)                # Se imprime los resultados de las referencias encontradas

    # Se ingresa la cantidad de productos de una referencia determinada que van para el mostrador de ventas
    mu=input("\n\n\n\nIngrese la nueva cantidad de unidades del producto para mostrador: ")  
    mu1= int(mu)                                # El anterior valor se convierte en entero


    mt=0                                        # Se crea variable para guardar la cantidad de productos acumulados en mostrador                                                                
    for TM in range (len(mm2)):                 # Se crea un ciclos para recorrer el DataFrame mostrador
      if (LL5.iloc[TM,2]==g3 and LL5.iloc[TM,6]==g5):  # En la base de datos de bodega se busca la respectiva referencia  y fecha de compra del producto
        LL5=pd.read_csv('BDATOS/bodega1.csv')          # Al cumplir la condición anterior se lee nuevamente la base de datos de bodega
        mm2=pd.read_csv("BDATOS/mostrador.csv")        # Se lee la base de datos de mostrador

        mt= mm2.iloc[TM, 7]                            # Se escoge el valor del acumulado en el mostrador y se crea una nueva variable
        g6= LL5.iloc[TM, 4]                            # Se escoge la cantidad de unidades disponibles en la bodega 
        mm2.iloc[TM, 4]=mu1                            # Se actualiza la cantidad  de unidades en el mostrador
        mt=mu1+mt                                      # Se suma la nueva cantidad de unidades al acumulado
        mm2.iloc[TM, 7]=mt                             # Se actualiza el acumulado en la base de datos de mostrador
        mm2.to_csv('BDATOS/mostrador.cvs', mode="w", index="", header="True") # Se graba las nuevas modificaciones en la base de datos mostrador
        g7=g6-mu1                                      # Las unidades que se llevan para el mostrador se descuentas al inventario de la bodega
        LL5.iloc[TM, 4]=g7                             # Se actualiza las nuevas cantidades de unidades del producto en la bodega
        mm2.iloc[TM, 2]=g7                             # La unidaes del productos actualizadas en la bodega se informa en la base de datos de mostrador
        mm2.to_csv('BDATOS/mostrador.csv',mode="w", index="", header="True") # Se graba las nuevas actualizaciones en la base de datos de mostrador
        LL5.to_csv('BDATOS/bodega1.csv', mode="w", index="", header="True")  # Se graba las nuevas actualizaciones en la base decdatos de bodega
        LL5=pd.read_csv('BDATOS/bodega1.csv')          # Se lee la base de datos de bodega para confirmar los cambios
        mm2=pd.read_csv('BDATOS/mostrador.csv')        # Se lee la base de datos de mostardor para confirmar los cambios
        


    print("\n\n\n\n***************   Bodega actualizada    *******************") # Mensaje de confirmación de datos actualizados en bodega
    print("\n\n\n\n", LL5)
    print("\n\n\n\n***************   Mostrador actualizado   ****************")  # Mensaje de confirmación de datos de actualizados en mostrador
    print("\n\n",mm2)
    break

def agotado():  # Se crea función para controlar el agotamiento de productos en la bodega
  while True:   # Se activa función para controlar el agotamiento de productos en la bodega
    os.system('clear')  # para limpiar pantalla 
    print("\n\n*******************************************************************************************************") # Decoración de titulo de pantalla
    print("\n\n******************************        ALERTA DE PRODUCTO AGOTADO         ******************************") # Titulo de alerta de producto agotado
    print("\n\n*******************************************************************************************************") # Decoración de titulo de pantalla
    L5=pd.read_csv('BDATOS/bodega1.csv')   # Se lee la base de datos de bodega
    for i in range(len(L5)):               # Se crea un ciclo para recorrer la base de datos bodega
       if(L5.iloc[i,4]==0):                # Se activa el ciclo con la condición que la cantidad de los productos están agotados

         #print("\n\nProducto con nombre: ", L5.iloc[i,1], " y referencia: ",L5.iloc[i,2],"       con fecha de compra: ",L5.iloc[i,6] )
         #print("\n\n")
         #print("\n\n                                                                             Está agotado")
         print("\nProducto con nombre: ", L5.iloc[i,1])  # Se muestra el nombre del producto que está agotado
         print("\n         referencia: ", L5.iloc[i,2])  # Se muestra la referencia del producto que está agotado
         print("\ncon fecha de compra: ", L5.iloc[i,6])  # Se muestra la fecha de compra del producto que está agotado
         print("\n\n                                   Está agotado")  # Mensaje que confirma que está agotado
         print("\n\n------------------------------------------------------------------------------------------------")  # Decoración de pantalla para la sección
         
         
    break    # Finalización de este ciclo



  while True: # Se activa función para controlar el agotamiento de productos en la bodega
    print("\n\n*******************************************************************************************************") # Decoración de titulo de pantalla
    print("\n\n*******************************************************************************************************") # Decoración de titulo de pantalla
    print("\n\n************************      ALERTA DE PRODUCTO CERCANO A AGOTARSE    ********************************") # Titulo de alerta de producto cercano a agotarse
    print("\n\n*******************************************************************************************************") # Decoración de titulo de pantalla
    L5=pd.read_csv('BDATOS/bodega1.csv')   # Se lee la base de datos de bodega 
    for i in range(len(L5)):               # Se crea un ciclo para recorrer la base de datos bodega
        if(L5.iloc[i,4]==2):               # Se activa el ciclo con la condición que la cantidad de los productos están agotados
          #print("\n\nProducto con nombre: ", L5.iloc[i,1], " y referencia: ",L5.iloc[i,2],"       con fecha de compra: ",L5.iloc[i,6] )
          #print("\n\n                                                                                      Está cercano a agotarse  ")
          print("\nProducto con nombre: ", L5.iloc[i,1]) # Se muestra el nombre del producto que está cercano a agotarse
          print("\n         referencia: ", L5.iloc[i,2]) # Se muestra la referencia del producto que está cercano a agotarse
          print("\ncon fecha de compra: ", L5.iloc[i,6]) # Se muestra la fecha de compra del producto que está cercano a agotarse
          print("\n\n                                    Está cercano a agotarse") # Mensaje que confirma que está cercano a agotarse
          print("\n\n-------------------------------------------------------------------------------------------------") # Decoración de pantalla para la sección
                                                                                     
    break   # Finalización de este ciclo

def vencimiento():   # Función para avisar cuando hay un producto cercano para vencerse  o  vencido
  while True:        # Activa el ciclo para avisar cuando hay un producto cercano para vencerse  o  vencido
    os.system('clear')  # para limpiar pantalla    
    today=dt.today() # Muestra la fecha actual
    #print(today)
    f5=today.strftime('%Y%m%d') # Cambia el foramato de la fecha
    f55=int(f5)                 # Convierte el nuevo formato de fecha en entero
    #print(f55)
    f25=today-timedelta(15)     # A la fecha actual se restan 15 días
    f255=f25.strftime('%Y%m%d') # A la nueva fecha se le cambia formato
    f257=int(f255)              # A la anterior fecha se convierte en entero
    
    
    print("\n\n*****************************************************************************************************") # Decoración de titulo de pantalla
    print("*************************       ALERTA DE PRODUCTO VENCIDO     ******************************************") # Titulo de alerta de producto vencido
    print("*********************************************************************************************************") # Decoración de titulo de pantalla
    L5=pd.read_csv('BDATOS/bodega1.csv')   # Se lee la base de datos bodega
    
    for i in range(len(L5)):               # Se crea un ciclo para recorrer la base de datos bodega
      if(L5.iloc[i,7]<=f55):               # Se activa el ciclo con la condición de la fecha de vencimiento del producto es igual o mayor a la fecha actual
        #print("\n\nProducto con nombre: ", L5.iloc[i,1], " y referencia: ",L5.iloc[i,2],"       con fecha de compra: ",L5.iloc[i,6] )
        print("\n\n")                      # Salto de línea
        print("\nProducto con nombre: ", L5.iloc[i,1])     # Se muestra el nombre del producto que está vencido
        print("\n         referencia: ", L5.iloc[i,2])     # Se muestra la referencia del producto que está vencido
        print("\ncon fecha de compra: ", L5.iloc[i,6])     # Se muestra la fecha de compra del producto que está vencido
        print("\n\n                                   Está vencido - reemplazar")  # Mensaje que confirma que está vencido
        print("\n\n--------------------------------------------------------------------------------------------------")   # Decoración de pantalla para la sección                                                                   
    print("\n\n******************************************************************************************************")   # Decoración de pantalla para la sección
    print("\n\n**************************       ALERTA DE PRODUCTO CERCANO A VENCERSE   *****************************")   # Titulo de alerta de producto cercano a vencerse
    print("\n\n******************************************************************************************************")   # Decoración de titulo de pantalla
    L5=pd.read_csv('BDATOS/bodega1.csv')    # Se lee la base de datos bodega
    
    
    L57=pd.DataFrame(L5['Fv'])              # Se crea un nuevo DataFRame solamnete con las fechas de vencimientos de los productos
    #print(L57)

    L57['Fv']= pd.to_datetime(L57['Fv'], format="%Y%m%d") # Utilidad de pandas para manipular formatos de fechas y se crea una nuevo DataFrame
    #print(L57)
    
    for kkk in range(1):       # Se crea un ciclo para recorrer el anterior DataFrame
      L9=L57.iloc[kkk:,0]      # Se selecciona una fecha especifica
      T4=L9-timedelta(15)      # A la antrior fecha se resta 15 días
      LL9=pd.DataFrame(T4)     # Con el anterior resultado se crea un nuevo DataFrame
      LL9.columns=['Fv1']      # SE le coloca el titulo a la columna de los datos
     


    for k9 in range(len(L57)):  # Se crea un ciclo para recorrer DataFrame con formato de fecha modificado
      if(LL9.iloc[k9,0]<=today and today<L57.iloc[k9,0]):  # Se activa el ciclo con la condición que la fecha de vencimineto con 15 días de annticipación es menor que el día  actual
                                                           # y el día actual es menor a la fecha de vencimiento del producto.
       # TT=L5.iloc[k9,2]                                  
        
        #print("\n\nProducto con nombre: ", L5.iloc[k9,1], " y referencia: ",L5.iloc[k9,2],"       con fecha de compra: ",L5.iloc[k9,6] )
        print("\n\n")                                      # Salto de linea
        print("\nProducto con nombre: ", L5.iloc[k9,1])    # Se muestra el nombre del producto que está vencido
        print("\n         referencia: ", L5.iloc[k9,2])    # Se muestra la referencia del producto que está vencido
        print("\ncon fecha de compra: ", L5.iloc[k9,6])    # Se muestra la fecha de compra del producto que está vencido
        print("\n\n                                   Está cercano a vencerse - tener cuidado")  # Mensaje que confirma que está cercano a vencerse - tener cuidado
        print("\n\n--------------------------------------------------------------------------------------------------")  # Decoración de titulo de pantalla
        
        #print("\n\n                                                                             Está cercano a vencerse - tener cuidado")
        print("\n\n")  # Salto de línea 
    break              # Finalización del ciclo de esta sección


#informe 6
today=dt.today()            # comando que muestra la fecha actual
f5=today.strftime('%Y%m%d') # para cambiar el formato de fecha y unirlo
f55=int(f5)                 # para convertir la fecha en un entero para operciones matemáticas
print(f55)                  # para imprimir la hora
f56=time.strftime('%H:%M:%S') # pra modificar el foramto de la hora
print(f56)                    # para imprimir la hora
ce=0
ff7=0
def venta():
  while True:
    ce=[] # Se crea lista para almacenar la identificación del cliente
    c1=[] # Se crea lista para almacenar la referencia del producto
    c2=[] # Se crea lista para almacenar el nombre del producto
    c3=[] # Se crea lista para almacenar el valor unitario del producto
    c4=[] # Se crea lista para almacenar la cantidad de productos que se va a comprar un cliente respecto a una referencia determinada
    c5=[] # Se crea lista para almacenar el subtotatal de la compra por referencia de producto
    c6=[] # Se crea lista para almacenar la fecha
    c7=[] # Se crea lista para almacenar la hora

    cc= input("\n\nIngrese la identificación del cliente: ") # ingreso de la identificación del cliente
    cc=int(cc)                 # se convierte el valor de la identificación en un entero
    
    z1= input("\n\ningrese la cantidad de ventas que se van a realizar: ") # para crear un ciclo en donde se estima la cantidad de productos que hay que registrar
    z=int(z1)                  # Se convierte el valor del ciclo en un entero
    zz1=0                      # para generar variable para el nombre
    zz2=0                      # para generar variable para el precio individual del producto
    subtotal=[]                # para geneerar variables del valor subtotal ed la venta


    for k in range(z):  # se crea una iteración para registrar las los productos que se van a vender.
      L6 =pd.read_csv("BDATOS/mostrador.csv") # SE lee la base de datos mostrador
      print(L6.iloc[:,0:2])    # se imprime el nombre y a referencia del producto
      Ref1= input("\n\nIngrese la referencia del producto: ") # para ingresar la respectiva referencia del producto
  
      can= input("\n\nIngrese la cantidad de producto:  ") # Para ingresar la cantidad de productos que se van a comprar de la respectiva referencia
      can= int(can)               # para convertir en entero la cantidad de productos que se van a comprar de la respectiva referencia 
      for kk in range(len(L6)):   # se crea una interación para revisar las refrencias de los productos
        if(L6.iloc[kk,1]== Ref1): # SE activa la condición de que los productos tengan la misma referencia del producto que va a comprar el cliente
          zz1= L6.iloc[kk,0]      # se busca el nombre del producto
          zz2= L6.iloc[kk,6]      # Se busca el precio unitario del producto
          subtotal= zz2*can       # se halla el subtotal de la compra de ese producto

          ce.append(cc)           # Se anexa a lista para almacenar la identificación del cliente
          c1.append(Ref1)         # Se anexa a lista para almacenar la referencia del producto
          c2.append(zz1)          # Se anexa a lista para almacenar el nombre del producto
          c3.append(zz2)          # Se anexa a lista para almacenar el valor unitario del producto
          c4.append(can)          # Se anexa a lista para almacenar la cantidad de productos que se va a comprar un cliente respecto a una referencia determinada
          c5.append(subtotal)     # Se anexa a lista para almacenar el subtotatal de la compra por referencia de producto
          c6.append(f55)          # Se anexa a lista para almacenar la fecha
          c7.append(f56)          # Se anexa a lista para almacenar la hora
          
         
          factura=(ce,c1,c2,c3,c4,c5,c6,c7) # se crea lista con los valores de las respectivas variables
          factura1=pd.DataFrame(factura)    # Se crea DataFrame para la factura
          factura2=pd.DataFrame.transpose(factura1) # Se transpone el Dataframe factura
      
         # Se coloca los nombres a las columnas
          factura2.columns=['Cedula','Referencia','Nproducto','Punitario','Cantidad','Subtotal','Fecha','Hora']
      
          temporal=pd.DataFrame.transpose(factura1)  # Se crea el DataFrame temporal que va permitir crear la factura
      
         # Se coloca los nombres a las columnas
          temporal.columns=['Cedula','Referencia','Nproducto','Punitario','Cantidad','Subtotal','Fecha','Hora']
      
         # Se graban los datos para la factura en la base de datos temporal
          temporal.to_csv('BDATOS/temporal.csv', mode="a", index="", header="")
      
         # Se graban los datos para la factura en la base de datos factura para consultas en el futuro
          factura2.to_csv('BDATOS/factura.csv', mode="a", index="", header="")
     
         # Para actualizar las unidades en el mostrador
          mm2=pd.read_csv("BDATOS/mostrador.csv")
      
         # Nueva cantidad de unidades del producto para mostrador
          mu1= can                     # Se elige la cantidad de unidades para descontar en mostrador
          mt=0                         # variable para operaciones matemáticas
          for TM in range(len(mm2)):   # se crea un ciclo para recorrer toda la base de mostrador
            if (mm2.iloc[TM, 1]==Ref1):# Se crea un filtro para eliger la referencia correcta
                   
               mm2=pd.read_csv("BDATOS/mostrador.csv") # Se lee la base de datos de mostardor
               print(mm2)                              # Se imprime la base de datos de mostardor antes de descontar las unidades del producto
               mt= mm2.iloc[TM, 7]                     # Se selecciona el acumulado disponible del producto ubicado en el mostrador
          
               mt=mt-mu1                               # se descuenta las respectivas unidades del producto
               mm2.iloc[TM, 7]=mt                      # se actualiza el acumulado con el nueva cantidad de productos
               mm2.to_csv('BDATOS/mostrador.csv', mode="w", index="", header="True") # se graba los nuevos datos en la base de datos de mostrador
                                   
               mm2=pd.read_csv("BDATOS/mostrador.csv") # se lee la base de datos de mostardor con los nuevos datos
               print("\n\n\n\n")                       # salto de línea
               print(mm2)                              # Se imprime la nueva base de datos mostrador
             
    break
       
   
    
                   



def Factura():
  while True:
    temporal22=pd.read_csv('BDATOS/temporal.csv')  # Para leer la base de datos temporal
    factura22=pd.read_csv('BDATOS/factura.csv')   # Para leer la base de datos de factura
    Vtotal=temporal22['Subtotal'].sum()  # para sumar el valor total de la compra de productos
    tem=temporal22.drop(['Fecha','Hora'], axis=1) # Para eliminar columnas de la fecha y hora
                                  # variable para la identificcaión del cliente
                              # variable para el valor total de la compra
    ventas=(ce,Vtotal,f55,f56)                     # Se crea lista para ventas totales
    ventas1=pd.DataFrame(ventas)               # Se crea dataframe para ventas totales
    ventas2=pd.DataFrame.transpose(ventas1)    # se transpone el dataframe para organizar los datos
    ventas2.columns=['Cedula','Vtotal','Fecha','Hora'] # se coloca nombres a las columnas
    ventas2.to_csv('BDATOS/ventas.csv', mode="a", index="", header="") # Se graba los datos para ventas totales en el archivo ventas.csv
    ventas2= pd.read_csv('BDATOS/ventas.csv')
    #cont=pd.read_csv('BDATOS/contador.csv')
    #cont1=cont.iloc[0:0]
    #cont2=cont1+1
    #cont2.to_csv('BDATOS/contador.csv', mode="w", index="", header="") 
    #os.system('clear')                         # para limpiar la pantalla
    print("\n\n\n\n\t\t\t\t\t                  FACTURA DE VENTA") # titulo de la página factura de venta
    print("\n\n\n\n")                          #salto de linea                    
    print("Cédula: ",ce, "\t\tFecha: " ,       f55,   "\t\tHora: ",        f56,     "Factura nro.: ") # para insertar cédula, fecha , hora
    print("\n\n\n\n")                          # salto de línea
    print(tem)                                 # Se imprime datos de la compra para la factura
    print("\n\n")                              # salto de linea
    print("\n\n\t\t           Valor total de la venta: ", Vtotal)  # se imprime el valor total de la venta\n
  #else:
    
    break
  
#c1= (c1)
#c2
#ventas=(c1,c2,f55,f56)                     # Se crea lista para ventas totales
#ventas1=pd.DataFrame(ventas)               # Se crea dataframe para ventas totales
#ventas2=pd.DataFrame.transpose(ventas1)    # se transpone el dataframe para organizar los datos
#ventas2.columns=['Cedula','Vtotal','Fecha','Hora'] # se coloca nombres a las columnas
#ventas2.to_csv('BDATOS/ventas.csv', mode="a", index="", header="") # Se graba los datos para ventas totales en el archivo ventas.csv
#ventas2= pd.read_csv('BDATOS/ventas.csv')


def Venta_acum():
  while True:
          # para limpiar la pantalla
    print("\n\n\n\n\t\t\t\t\t                 PÁGINA DE VENTAS ACUMULADAS") # titulo de la página factura de venta
    print("\n\n\n\n")                          #salto de linea                    
    print(           "\t\t\t\t\tFecha: " ,       f55,   "\t\t\t\t\tHora: ",        f56)
    #ventas=(c1,c2,f55,f56)                     # Se crea lista para ventas totales
    #ventas1=pd.DataFrame(ventas)               # Se crea dataframe para ventas totales
    #ventas2=pd.DataFrame.transpose(ventas1)    # se transpone el dataframe para organizar los datos
    #ventas2.columns=['Cedula','Vtotal','Fecha','Hora'] # se coloca nombres a las columnas
    #ventas2.to_csv('BDATOS/ventas.csv', mode="a", index="", header="") # Se graba los datos para ventas totales en el archivo ventas.csv
    ventas2= pd.read_csv('BDATOS/ventas.csv')  # para leer el contenido del archivo de ventas totales
    print("\n\n\n\n",ventas2)                  # se imprime el contenido del archivo de ventas totales
  #else:
    break

# Menú
def menu():                                              # se crea un menu para el manejo operativo del negocio
    print("\n\n\n\n\t\t\t\t\t              PÁGINA PRINCIPAL DE VENTAS Y CLIENTES\n\n") # titulo de la página factura de venta
    print("\n\n\n\n      Selecciona una opción \n")                    # se imprime mendsaje del menú
    print("\t            6.1 - Para generar venta ")                  # se imprime registro de compras
    print("\t            6.2 - Factura")              # se imprime registro total acumulado
    print("\t            6.3 - Venta acumulada")                     # se imprime ingreso abodega
    print("\t            6.4 - Página de clientes")              # se imprime finalizacón de menú
    print("\t            6.5 - Página de Compras de cada cliente")              # se imprime finalizacón de menú         
    print("\t            6.7 - Otras opciones")              # se imprime finalizacón de menú




def clientes():
  while True:

    CA=[]#se crea lista para almacenar la indentificacion del cliente
    PP1=[]#se crea lista para almacenar la referencia del producto
    PP2=[]#se crea lista para almacenar el nombre del producto
    PP3=[]#se crea lista para almacenar el valor unitario del producto
    PP4=[]#se crea lista para almacenar la cantidad de productos que se va a comprar un cliente respecto a una referencia determinada 
    PP5=[]#se crea lista para almacenar el subtotal de la compra por referencia de producto
    PP6=[]#se crea lista para almacenar la fecha
    PP7=[]#se crea lista para almacenar la hora
    print("\n\n\n\n\t\t\t\t\t              PÁGINA CLIENTES") # titulo de la página de clientes
    PPP1=input("\n\nIngrese el numero de cedula: ")          # Para ingrese la identificación
    PPP2=input("\n\nIngrese el nombre del cliente: ")        # Para ingresar el nombre del cliente
    PPP3=input("\n\nIngrese el primer apellido: ")           # Para ingresar el primer apellido del cliente
    PPP4=input("\n\nIngrese el segundo apellido: ")          # Para ingresar el segundo apellido del cliente
    PPP5=input("\n\nIngrese el numero de celular: ")         # para ingresasar el número del celular
    PPP6=input("\n\nIngrese el numero fijo: ")               # para ingresar el número del teléfono fijo
    CA.append(PPP1) #se crea lista para almacenar la identificacion del cliente
    PP1.append(PPP2) #se crea lista para almacenar la identificacion del cliente
    PP2.append(PPP3) #se crea lista para almacenar la identificacion del cliente
    PP3.append(PPP4) #se crea lista para almacenar la identificacion del cliente
    PP4.append(PPP5) #se crea lista para almacenar la identificacion del cliente
    PP5.append(PPP6) #se crea lista para almacenar la identificacion del cliente
    CL=(CA,PP1,PP2,PP3,PP4,PP5)      # se crea lista con los datos del cliente
    PL1=pd.DataFrame(CL)             # Se crea DataFrame con los datos del cliente
    PL2=pd.DataFrame.transpose(PL1)  # se transpone el DataFrame
    PL2.to_csv('BDATOS/clientes.csv', mode="a", index="", header="") # se graba la información del cliente en la base de datos clientes
    PL3=pd.read_csv('BDATOS/clientes.csv')  # se lee la base e datos de cliente
    print(PL3)                              # Se imprime la base de datos cliente
  #else:
    break

def compra_cliente():
   while True:
    print("\n\n\n\n\t\t\t\t\t              PÁGINA COMPRA DE CLIENTES") # titulo de la página de clientes
    CA=[]                   # se crea lista para almacenar la indentificacion del cliente
    PPP1=input("\n\n\n\nIngrese el numero de cedula: ")
    CA.append(PPP1)         # se crea lista para almacenar la identificacion del cliente

    PPPP = int(PPP1)        # Se convierte el valor de la identificación del cliente entero 
    print("\n\n")       # Salto de linea
    factura22=pd.read_csv('BDATOS/factura.csv')  # Para leer la base de datos de factura
    #print(factura22)                            # Para imprimir la base de datos de factura
    
    LK=0                                         # Se crea variable pata manejo de DataFrame
    for AA in range(len(factura22)):             # Se crea ciclo para leer la base datos factura respecto a la identificación de clientes
      if(factura22.iloc[AA, 0]==PPPP):           # Condición para leer la base  de adtos de factura
        factura22=pd.read_csv('BDATOS/factura.csv')  # Se lee la base de datos de factura
        LK=factura22.iloc[AA, :]                     # Se busca la identificación especifica
        LK1=pd.DataFrame(LK)                         # Se crea un DataFrame para leer los datos del cliente de las compras que ha realizado
        LK2=pd.DataFrame.transpose(LK1)              # Se transpone el DataFrame
        print("\n\n\n\n")                            # Salto de linea
        print(LK2)                                   # Se imprime los resultados de las compras del cliente.
    break
# Se crea un una iteración con while mientras se cumpla la condición
while True:                                              # se activa el ciclo while para activar el menú
      menu()                                             # se activa la función menú
      opcionMenu = input("\n Inserte el número de la opción: ")   # sirve para ingresar el valor de la opción seleccionada
                 
      if opcionMenu == "6.1":               # Para activar la función compra
          print("\n\nhola\n\n")             # imprime mensaje de saludo
          venta()                          # la función venta se ejecuta
     
           

        
      elif opcionMenu == "6.2":              # Para activar la función factura
             Factura()                       # se ejecuta la función factura
      

      elif opcionMenu == "6.3":              # se activa la función venta acunulada
             Venta_acum()                    # se ejecuta la función venta acumulada

      elif opcionMenu == "6.4":              # se activa la función clientes
             clientes()                      # se ejecuta la función clients


      elif opcionMenu == "6.5":              # Se activa la función compras de cada cliente
             compra_cliente()                # se ejecuta la  función compra de clientes

      elif opcionMenu == "6.7":    
            break      

os.system('clear')     # Para limpiar la pantalla
print("\n\n*********************************************************************************************************")   # Decoración de titulo de pantalla
print("\n\t\t\t\t                          PÁGINA PRINCIPAL DE MOSTRADOR ")                                              # se imprime el titulo de la página del menu del manejo operativo del negocio
print("\n\n*********************************************************************************************************")   # Decoración de titulo de pantalla
today=dt.today()      # Selecciona la fecha actual
print(today)          # imprime la fecha actual




os.system('clear')                                       # sirve para limpiar la pantalla
print("\t\t\t\t PÁGINA PRINCIPAL \n\n")                  # se imprime el titulo de la página del menu del manejo operativo del negocio

  if opcionMenu == "4": 

     os.system('clear') #limpiar pantalla
     print("\n\n") 
        
     subtitulo = " SUBMENÚ DE COMPRAS Y BODEGA"
     print("\n\n")
     print(subtitulo.center(100," "))
     print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
     print("                                  \t4.1 - ")                  # se imprime registro de compras
     print("                                  \t4.2 - ")              # se imprime registro total acumulado
     print("                                  \t4.3 - ")  
     print("                                  \t4.4 - ") 
     print("                                  \t4.5 - ") 
     print("                                  \t4.6 - ") 
     print("                                  \t4.7 - ")
     print("                                  \t4.8 - ")
     print("                                  \t9   - ")              # se imprime finalizacón de menú
          
     opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
     if opcionmenu== "4.1": 
       print("\n\nhola\n\n")                          # imprime mensaje de saludo
       #bodegacom()   
       #mensaje="HOLA"
       os.system('clear') #limpiar pantalla
       print("\n\n")
       print("Hola".center(100," "))                                  # la función compra se ejecuta
          

        
     elif opcionmenu == "4.2": 
        sub72()
                                                  # se ejecuta la función total
      

     elif opcionmenu == "4.3":
         print("4.3")
         
        
     elif opcionmenu == "4.4": 
        print("4.4")
           

     elif opcionmenu == "4.5":
        print("4.5")
           


     elif opcionmenu == "4.6":
        print("4.6")
        
             

     elif opcionmenu == "4.7":  
        print("4.7")
          
              

     elif opcionmenu == "4.8": 
        print("4.8")
         
             
  if opcionMenu == "5": 
    os.system('clear') #limpiar pantalla
    print("\n\n") 
        
    subtitulo = " SUBMENÚ DE MOSTRADOR"
    print("\n\n")
    print(subtitulo.center(100," "))
    print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
    print("                                  \t5.1 - ")                  # se imprime registro de compras
    print("                                  \t5.2 - ")              # se imprime registro total acumulado
    print("                                  \t5.3 - ")  
    print("                                  \t5.4 - ") 
    print("                                  \t5.5 - ") 
    print("                                  \t5.6 - ") 
    print("                                  \t5.7 - ")
    print("                                  \t5.8 - ")
    print("                                  \t9   - ")              # se imprime finalizacón de menú
          
    opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
    if opcionmenu== "5.1":
      print("\n\nhola\n\n")                          # imprime mensaje de saludo
      #bodegacom()   
      #mensaje="HOLA"
      os.system('clear') #limpiar pantalla
      print("\n\n")
      print("Hola".center(100," "))                                  # la función compra se ejecuta
           

        
    elif opcionmenu == "5.2": 
       sub72()
                                                  # se ejecuta la función total
      

    elif opcionmenu == "5.3": 
      print("5.3")
        
    elif opcionmenu == "5.4":   
       print("5.4")
             

    elif opcionmenu == "5.5":
      print("5.5")
              


    elif opcionmenu == "5.6":  
      print("5.6")
             

    elif opcionmenu == "5.7":   
      print("5.7")  
              

    elif opcionmenu == "5.8": 
      print("5.8") 
             
  if opcionMenu == "6": 
    os.system('clear') #limpiar pantalla
    print("\n\n") 
        
    subtitulo = " SUBMENÚ DE VENTAS Y CLIENTES"
    print("\n\n")
    print(subtitulo.center(100," "))
    print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
    print("                                  \t6.1 - ")                  # se imprime registro de compras
    print("                                  \t6.2 - ")              # se imprime registro total acumulado
    print("                                  \t6.3 - ")  
    print("                                  \t6.4 - ") 
    print("                                  \t6.5 - ") 
    print("                                  \t6.6 - ") 
    print("                                  \t6.7 - ")
    print("                                  \t9   - ")              # se imprime finalizacón de menú
          
    opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
    if opcionmenu== "6.1": 
      print("\n\nhola\n\n")                          # imprime mensaje de saludo
      #bodegacom()   
      #mensaje="HOLA"
      os.system('clear') #limpiar pantalla
      print("\n\n")
      print("Hola".center(100," "))                                  # la función compra se ejecuta
           

        
    elif opcionmenu == "6.2":
      sub72()
                                                  # se ejecuta la función total
      

    elif opcionmenu == "6.3":
      print("6.3")
        
    elif opcionmenu == "6.4": 
      print("6.4")
             

    elif opcionmenu == "6.5":
      print("6.5")
              


    elif opcionmenu == "6.6":  
      print("6.6")
             

    elif opcionmenu == "6.7": 
      print("6.7")  
              

                                         
  if opcionMenu == "7": 
   os.system('clear') #limpiar pantalla
   print("\n\n") 
        
   subtitulo = " SUBMENÚ DE CONTABILIDAD"
   print("\n\n")
   print(subtitulo.center(100," "))
   print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
   print("                                  \t7.1 - Costos de Bodega completa ")                  # se imprime registro de compras
   print("                                  \t7.2 - Costos de bodega por fechas")              # se imprime registro total acumulado
   print("                                  \t7.3 - Ingreso de datos para costos fijos")  
   print("                                  \t7.4 - Costos fijos completos") 
   print("                                  \t7.5 - Costos fijos por fecha") 
   print("                                  \t7.6 - Ingresos por ventas - completa") 
   print("                                  \t7.7 - Ingresos por ventas - manejo por fechas")
   print("                                  \t7.8 - CONTABILIDAD")
   print("                                  \t9   - Terminar con uso de menu")              # se imprime finalizacón de menú
          
   opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
   if opcionmenu== "7.1": 
     print("\n\nhola\n\n")                          # imprime mensaje de saludo
     os.system('clear') #limpiar pantalla
     print("\n\n")
     print("Hola".center(100," "))                                  # la función compra se ejecuta
           

        
   elif opcionmenu == "7.2":
      sub72()
                                                  # se ejecuta la función total
      

   elif opcionmenu == "7.3": 
      print("7.3")
        
   elif opcionmenu == "7.4": 
      print("7.4")
             

   elif opcionmenu == "7.5": 
     print("7.5")
              


   elif opcionmenu == "7.6":
      print("7.6")
             

   elif opcionmenu == "7.7": 
     print("7.7")  
              

   elif opcionmenu == "7.8":
      print("7.8") 
             
  if opcionMenu == "8": 
    os.system('clear') #limpiar pantalla
    print("\n\n") 
        
    subtitulo = " SUBMENÚ DE REPORTES"
    print("\n\n")
    print(subtitulo.center(100," "))
    print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
    print("                                  \t8.1 - ")                  # se imprime registro de compras
    print("                                  \t8.2 - ")              # se imprime registro total acumulado
    print("                                  \t8.3 - ")  
    print("                                  \t8.4 - ") 
    print("                                  \t8.5 - ") 
    print("                                  \t8.6 - ") 
    print("                                  \t8.7 - ")
    print("                                  \t8.8 - ")
    print("                                  \t9   - ")              # se imprime finalizacón de menú
          
    opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
    if opcionmenu== "8.1": 
      print("\n\nhola\n\n")                          # imprime mensaje de saludo
      #bodegacom()   
      #mensaje="HOLA"
      os.system('clear') #limpiar pantalla
      print("\n\n")
      print("Hola".center(100," "))                                  # la función compra se ejecuta
           

        
    elif opcionmenu == "8.2": 
        sub72()
                                                  # se ejecuta la función total
      

    elif opcionmenu == "8.3": 
        print("7.3")
        
    elif opcionmenu == "7.4":
        print("8.4")
             

    elif opcionmenu == "8.5":  
         print("8.5")
              


    elif opcionmenu == "8.6": 
         print("8.6")
             

    elif opcionmenu == "8.7":
         print("8.7")  
              

    elif opcionmenu == "8.8":     
         print("8.8") 
             
          
  elif opcionMenu == "9": 
   print("\n\n\t\tSistema finalizado")
  # break 
    
