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
    
