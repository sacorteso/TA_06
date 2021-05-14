#ADVERTENCIA
# En la opción 7.8, ingrese fecha operación utilizar 20210513

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





























































































































































































def contabilidad():       # se crea la función que controla toda la contabilidad general del negocio
  while True:             # Se activa el ciclo para que funcione la función contabilidad
    print("\n\n\n\n PÁGINA PRINCIPAL DE CONTABILIDAD")  # Titulo de la sección completa de contabilidad
    print("\n\n\n\n")     # Salto de linea

    IF = int(input("\n\n\n\nIngrese la fecha de la operación contable: ")) # Sirve para ingresar la fecha de operación contable diaria

    Ent=int(input("\n\nIngrese otras entradas de dinero: "))               # Sirve para ingresar dinero extra

    print("\n\n\n\n Página de costos en dinero por compra en bodega")      # Subtitulos de la páginas que se van a utilizar
    print("\n\n Sistema por fechas\n\n\n\n")                               # sistema de fechas para ser más específico

    co=pd.read_csv("BDATOS/bodega1.csv")     # Se crea un nuevo DataFrame con la base de datos de bodega
    co2=co.iloc[:,3]                         # Se extrae el precio de los productos por pacas
    co3=co.iloc[:,6]                         # Se extrae la fecha de la compra
    F=[co2,co3]                              # Se crea una lista con precio por paca y fecha de compra
    F1=pd.DataFrame(F)                       # Se crea un nuevo DataFarme con los datos anteriores
    F2=F1.transpose()                        # Se transpone el DataFrame anterior
    print(F2)                                # Se imprime el nuevo DataFrame


   
    F3=F2[(F2['Fcompra']==IF)]               # Se crea un filtro para localizar las compras realizadas en una fecha específica
    F4=pd.DataFrame(F3)                      # Se crea un nuevo DataFrame con los nuevos productos seleccionados
    F5=F4['Ppaca'].sum()                     # Valor en dinero de compras en la bodega entre un intervalo de tiempo

    
    gb2=pd.read_csv("BDATOS/costosm.csv")    # Se lee la base de datos de costos fijos
    print(gb2)                               # Se lee la base de datos de costos fijos

    F33= gb2[(gb2['Fecha']==IF)]             # Se crea un filtro que busca las fechas solicitadas
    F7=pd.DataFrame(F33)                     # Se crea un nuevos DataFrame con los costos fijos en las respectivas fechas solicitadas

    print("\n\n",F7)                         # Se imprime los resultados


    st11=F7['Nómina'].sum()                  # Suma todos los costos de nómina
    st21=F7['Spúblicos'].sum()               # Suma tosdos los valores de servicios públicos
    st31=F7['Arriendo'].sum()                # Suma todos los valores de arriendo
    st41=F7['Seguros'].sum()                 # Suma todos los valores de seguros
    st51=F7['mantenimiento'].sum()           # Suma todos los valores de mantenimiento
    st61=F7['Impuestos'].sum()               # suma todos los valores de impuestos
    st71=F7['Transporte'].sum()              # suma todos los valores de transporte
    st81=F7['Otroscostos'].sum()             # suma todos los valores de otros costos


    TotalCFF= st11+st21+st31+st41+st51+st61+st71+st81 # Se suman todas las variables de costos



    ing=pd.read_csv("BDATOS/ventas.csv")
    print(ing)



    ing2= ing[(ing['Fecha']==IF)]
    ing3=pd.DataFrame(ing2)


    ing5=ing3['Vtotal'].sum()    # Valor en dinero de ventas entre un intervalo de tiempo


    cont2=pd.read_csv("BDATOS/contabilidad1.csv")
    kq=len(cont2)
    print(kq)
    capbase=cont2.iloc[kq-1,1]
    aux1=cont2.iloc[kq-1,5]
    porc=cont2.iloc[kq-1,6]
    ganancianeta= ing5*porc/100     # operación matemática para hallar la ganancia diaria

    aux=ing5-ganancianeta           # operación matemática para extraer el capital para reinvertir

    cap=capbase+aux+aux1            # Se actualiza el capital base del negocio
    Disponible= cap-F5-TotalCFF     # Se resta al capital los costos de compras de productos y costos fijos de funcionamiento diarios
    cap= Disponible                 # Se actualiza el capital base del negocio

    cont=[]
    cont=[IF,cap,F5,TotalCFF,ing5,Ent,porc,ganancianeta,Disponible]


    cont1=pd.DataFrame(cont)
    cont2=pd.DataFrame.transpose(cont1)

    cont2.columns=['IF','capitalbase','CBodega','Cfijos','Ventas','EntradaExtra','porc','ganancianeta','Disponible']
    cont2.to_csv("BDATOS/contabilidad1.csv", mode="a", index="", header="")
    cont2=pd.read_csv("BDATOS/contabilidad1.csv")
    print(cont2.iloc[:,0:5])
    print(cont2.iloc[:,5:9])
    break



   


    
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

      elif opcionMenu == "7.8":                            # se activa la función bodega
             contabilidad()   

      #elif opcionMenu == "9":                            # se elige la activa la opción finalizar menú
          #print("\n\n\t\tSistema finalizado")                    # mensaje que confirma la finalización del menu
         # break                                          # se finaliza el ciclo if del menú
            


