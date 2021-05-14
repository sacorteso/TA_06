

from datetime import date as dt #librería para manejar fechas
from datetime import datetime as dtt  #librería para manejar el tiempo
from datetime import timedelta        #librearía para realizar operaciones matemáticas con el tiempo
import pandas as pd # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os           # Librerías para realizar funciones internas del software
import csv          # Librería para manipular archivos con extensión csv
import time         # Librería para manipular el tiempo


today=dt.today()              # comando que muestra lafecha actual
f5=today.strftime('%Y%m%d')   # para cambiar el formato de fecha y unirlo
f55=int(f5)                   # para convertir la fecha en un entero para operaciones matemáticas
print(f55)                    # para imprimir la hora
#f56=time.strftime('%H:%M:%S') # para modificar el formato de la hora
#print=(f56)                   # para imprimir la hora modificada
cce=0                         # constante para operaciones matemáticas
def bodegacom():              # Se crea una función para hallar el valor total en dinero de los productos de la bodega
  while True:                 # Se crea un ciclo while que permite mantener la función activa
    print("\n\n\n\n Página de costos en dinero por compras en bodega") # Se imprime titulo de página de costos de bodega
    print("\n\n Sistema completo\n\n")     # Se imprime subtitulo para costos de bodega

    # Para Bodega
    co=pd.read_csv("BDATOS/bodega1.csv") # Se lee el archivo con la base de datos de la bodega
    print(co)                            # Se imprime la base de datos de la bodega
    co1=co.iloc[:,0]                     # Se crea una lista con los nombres de las empresas
    co2=co.iloc[:,3]                     # Se crea una lista con los valores de los productos por pacas
    co3=co.iloc[:,6]                     # Se crea una lista con la fecha de compra

    T=[co1,co2,co3]                      # Se unen todas las listas en una sola lista.

    cce=pd.DataFrame(T)                  # Se crea un DataFrame para manejar las listas antes escogidas
    cce1=cce.transpose()                 # Se transpone el DataFrame para mejorar la presentación de la información

    Vtotalbodega= int(cce1['Ppaca'].sum())     # Se selecciona la fila precio paca y se suman todos los valores para hallar el costo total de los productos comprados

   # print("\n\n\n\nHasta fecha actual: ", f55)  # Se imprime  la fecha

    print("\n\n\n\nEl total pagado por bodega es: $",Vtotalbodega,"\n\n\n\n") # Se imprime el resultado total con enunciado.
    break                                # Se termina el ciclo de la función










































    
#print("\t\t\t\t PÁGINA PRINCIPAL DE CONTABILIDAD \n\n")                  # se imprime el titulo de la página del menu del manejo operativo del negocio


def menu():                                              # se crea un menu para el manejo operativo del negocio
    
    print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
    print("\t7.1 - Costos de Bodega completa ")                  # se imprime registro de compras
    print("\t7.2 - Costos de bodega por fechas")              # se imprime registro total acumulado
    print("\t7.3 - Ingreso de datos para costos fijos")  
    print("\t7.4 - Costos fijos completos") 
    print("\t7.5 - Costos fijos por fecha") 
    print("\t7.6 - Ingresos por ventas - completa") 
    print("\t7.7 - Ingresos por ventas - manejo por fechas")
    print("\t7.8 - CONTABILIDAD")
    print("\t3 - Vencimiento de productos")            # se imprime ingreso abodega
    print("\t9 - Terminar con uso de menu")              # se imprime finalizacón de menú
          
# Se crea un una iteración con while mientras se cumpla la condición
while True:                                              # se activa el ciclo while para activar el menú
      menu()                                             # se activa la función menú
      opcionMenu = input("\n Inserte el número de la opción: ")   # sirve para ingresar el valor de la opción seleccionada
                  
      if opcionMenu == "7.1":                              # Para activar la función compra
          print("\n\nhola\n\n")                          # imprime mensaje de saludo
          bodegacom()                                     # la función compra se ejecuta
     
           

        
      #elif opcionMenu == "7.2":                            # Para activar la función total
             #bodegafecha()                                     # se ejecuta la función total
      

     # elif opcionMenu == "7.3":                            # se activa la función bodega
            # ingcostosf()
        
      #elif opcionMenu == "7.4":                            # se activa la función bodega
           # costosf()

      #elif opcionMenu == "7.5":                            # se activa la función bodega
             #costosff()


      #elif opcionMenu == "7.6":                            # se activa la función bodega
             #ingventasT()

      #elif opcionMenu == "7.7":                            # se activa la función bodega
            # ingventasTF()   

      #elif opcionMenu == "7.8":                            # se activa la función bodega
             #contabilidad()   

      #elif opcionMenu == "9":                            # se elige la activa la opción finalizar menú
          #print("\n\n\t\tSistema finalizado")                    # mensaje que confirma la finalización del menu
         # break                                          # se finaliza el ciclo if del menú
            


