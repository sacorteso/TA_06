#ADVERTENCIA
# En la opción 7.2, ingrese fecha INICIAL 20210305 Y fecha final 20210423
# En la opción 7.5, ingrese fecha INICIAL 20210513 Y fecha final 20210513
# En la opción 7.7, ingrese fecha INICIAL 20210513 Y fecha final 20210513
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

def bodegafecha():    # Se crea función para compras en la bodega con fecha específica
  while True:         # Se crea ciclos para activar la función para compras en la bodega con fecha específica
    print("\n\n\n\n Pagina de costos en dinero por compra en bodega")  # Titulo de la sección
    print("\n\n Sistema por fechas \n\n\n\n")                          # Subtitulo de la sección

    co=pd.read_csv("BDATOS/bodega1.csv")                               # Se lee la base de datos de Bodega y se crea DataFrame
    co2=co.iloc[:,3]                                                   # Se crea una lista con los valores de los productos por paca                                      
    co3=co.iloc[:,6]                                                   # secrea una lista con la fecha de compras de los productos
    F=[co2,co3]                                                        # Se crea una nueva lista con los datos anteriores
    F1=pd.DataFrame(F)                                                 # Se crea un nuevo dataFrame con los valores anteriores
    F2=F1.transpose()                                                  # Se transpone el DataFrame anterior
    print(F2)                                                          # Se imprime el nuevo DataFrame

    
    f1= int(input("\n\n\n\nIngrese la fecha inicial: "))               # Sirve para ingresar la fecha inicial para crear un intervalo de búsqueda
    f2= int(input("\n\nIngrese la fecha final: "))                     # Sirve para ingresar la fecha inicial para crear un intervalo de búsqueda
    
    F3= F2[(F2['Fcompra']>=f1) & (F2['Fcompra']<=f2)]                  # Se crea un filtro para localizar los datos en el intervalo de tiempo específicado
    F4=pd.DataFrame(F3)                                                # Se crea un nuevo DataFrame con los datos encontrados

    F5=F4['Ppaca'].sum()                               # valor en dinero de compras en la bodega entre un intervalo de tiempo
    
    print("\n\n\n\nEntre las fechas  ", f1," y ",f2)   # se imprime el intervalo de la fechas

    print("\n\n\n\nEl total pagado por bodega es:     $",F5,"\n\n\n\n") # Total de costos por compras para bodega

    break                                             # Finalización del ciclo de función



def ingcostosf():        # se crea función para ingresar datos adicionales para la base de datos de costos fijos
  while True:            # Se crea un ciclo para activar esta función
    print("\n\n\n\n Página de Ingreso de datos de costos fijos\n\n\n\n")  # se imprime Titulo de sección
    
    g11= input("\n\nIngrese el valor Total de nómina: ")             # Para ingresar los datos de pago de nómina
    
    g21= input("\n\nIngrese el valor Total de servicios públicos: ") # Para ingresar los datos de pago de servicios públicos
    
    g31= input("\n\nIngrese el valor Total de arriendo: ")           # Para ingresar los datos de pago de arriendo
    
    g41= input("\n\nIngrese el valor Total de seguros: ")            # Para ingresar los datos de pago de seguros
    
    g51= input("\n\nIngrese el valor Total de mantenimiento: ")      # Para ingresar los datos de pago de mantenimiento
    
    g61= input("\n\nIngrese el valor Total de impuestos: ")          # Para ingresar los datos de pago de impuestos
    
    g71= input("\n\nIngrese el valor Total de transporte: ")         # Para ingresar los datos de pago de transporte
    
    g81= input("\n\nIngrese el valor Total de otros gastos: ")       # Para ingresar los datos de pago de otros gastos
    
    
    g= [f55,g11,g21,g31,g41,g51,g61,g71,g81]   # se crea una lista con los valores antes mencionados
    gb=pd.DataFrame(g)                         # Se crea un DataFrame con estos avlores
    gb1=pd.DataFrame.transpose(gb)             # Se transpone el DataFrame
    # Se coloca nombres a las columnas
    gb1.columns=['Fecha','Nómina','Spúblicos','Arriendo','Seguros','mantenimiento','Impuestos','Transporte','Otroscostos']
    gb1.to_csv("BDATOS/costosm.csv",  mode="a", index="", header="") # Se graba los nuevos datos en la base costos fijos
    gb2=pd.read_csv("BDATOS/costosm.csv")                            # Se lee la base de datos de costos fijos con los nuevos cambios
    print("\n\n\n\n                Página de Ingreso de datos de costos fijos\n") # Se imprime titulo de l sección
    print("\n\n",gb2.iloc[:,0:5])    # Se imprime la primer parte de los resultados
    print("\n\n",gb2.iloc[:,5:9])    # Se imprime la segunada parte de los resultados
    break                            # Se finaliza el ciclo de esta función

def costosf():    # SE crea una función para los costos fijos completos
  while True:     # Se crea un ciclo para activar la función de costos fijos completos
       ## Informe mensual
    #para costos fijos
    print("\n\n\n\n              Página de costos fijos en dinero")  # Titulo de la sección
    print("\n\n                   Sistema completo\n\n\n\n")         # subtitulo de la sección
    gb2=pd.read_csv("BDATOS/costosm.csv")        # se lee la base de datos de costos fijos y se crea un DataFrame
    print(gb2)                                   # Se imprime la base de datos

    
    st1=gb2['Nómina'].sum()           # Suma todos los costos de nómina
    st2=gb2['Spúblicos'].sum()        # Suma tosdos los valores de servicios públicos
    st3=gb2['Arriendo'].sum()         # Suma todos los valores de arriendo
    st4=gb2['Seguros'].sum()          # Suma todos los valores de seguros
    st5=gb2['mantenimiento'].sum()    # Suma todos los valores de mantenimiento
    st6=gb2['Impuestos'].sum()        # suma todos los valores de impuestos
    st7=gb2['Transporte'].sum()       # suma todos los valores de transporte
    st8=gb2['Otroscostos'].sum()      # suma todos los valores de otros costos


    TotalCF= st1+st2+st3+st4+st5+st6+st7+st8  # Suma el valor en dinero de todos los costos fijos 
   

    print("\n\n\n\n Subtotales")              # mensaje de subtitulos

    print("\n\n\n\nHasta la Fecha: ",f55)     # fecha en el momento del reporte
    print("\n\nEstos son los costos fijos")   # mensaje
    # totales por área en costos fijos
    print("\n\nNómina: $",st1,"\n\nSpúblicos: $",st2,"\n\nArriendo: $",st3,"\n\nSeguros: $",st4,
           "\n\nmantenimiento: $",st5,"\n\nImpuestos: $",st6,"\n\nTransporte: $",st7,"\n\nOtros costos: $",st8)

    
    print("\n\n\n\n Total de costos fijos: $",TotalCF) # Total de costos fijos
    break                                              # Se finaliza el ciclo de esta función
      
  

def costosff():            # Se crea función para costos fijos por fecha específica
  while True:              # Se cre ciclo para activar la función de costsos fijos por fecha específica
    print("\n\n\n\n             Página de costos fijos en dinero")    # Título de esta sección
    print("\n\n                   Sistema por fechas\n\n\n\n")        # Subtitulos de esta función
    gb2=pd.read_csv("BDATOS/costosm.csv")                             # Se lee la base de datos de costos fijos
    print(gb2)                                                        # se imprime la base de datos de ventas
    fc1=int(input("\n\ningrese la fecha inicial:  "))                 # Sirve para ingresar la fecha inicial para crear un intervalo de búsqueda
    fc2=int(input("\n\ningrese la fecha final:  "))                   # Sirve para ingresar la fecha final para crear un intervalo de búsqueda

    F33=gb2[(gb2['Fecha']>=fc1) & (gb2['Fecha']<=fc2)]                # Se crea un filtro para localizar los datos en el intervalo de tiempo específicado
    F7=pd.DataFrame(F33)                                              # Se crea un nuevo DataFrame con los datos encontrados

    print("\n\n",F7)                                                  # Seimprime el nuevo Dataframe


    st11=F7['Nómina'].sum()                  # Suma todos los costos de nómina
    st21=F7['Spúblicos'].sum()               # Suma tosdos los valores de servicios públicos
    st31=F7['Arriendo'].sum()                # Suma todos los valores de arriendo
    st41=F7['Seguros'].sum()                 # Suma todos los valores de seguros
    st51=F7['mantenimiento'].sum()           # Suma todos los valores de mantenimiento
    st61=F7['Impuestos'].sum()               # suma todos los valores de impuestos
    st71=F7['Transporte'].sum()              # suma todos los valores de transporte
    st81=F7['Otroscostos'].sum()             # suma todos los valores de otros costos


    print("\n\n\n\n Subtotales")             # Se imprime menasje de Subtotales

    print("\n\n\n\nEntre las fechas: ",fc1, " y ",fc2) # se imprime el intervalo de la fechas
    # Se imprime el valor de dinero localizado por costos fijos
    print("\n\nNómina: $",st11,"\n\nSpúblicos: $",st21,"\n\nArriendo: $",st31,"\n\nSeguros: $",st41,
          "\n\nmantenimiento: $",st51,"\n\nImpuestos: $",st61,"\n\nTrnasporte: $",st71,"\n\nOtros costos: $",st81)

    TotalCFF= st11+st21+st31+st41+st51+st61+st71+st81  # Suma el valor en dinero de costos fijos entre un intervalo de tiempo

    print("\n\n\n\n Total de costos fijos: ",TotalCFF)   # Total de costos fijos por fecha específica

    break            # Finalización del ciclo de esta función




def ingventasT():     # Se crea función para sumar el total ingresos en dinero por ventas por forma completa
  while True:         # Se activa el ciclo para ejecutar la función de ingreso de dinero por ventas por forma completa

    print("\n\n\n\n Página de ingresos en dinero por ventas\n\n")   # Se imprime titulo de esta sección
    print("\n\n Sistema completo\n\n\n\n")                          # Se imprime subtitulo de esta scción
    

    cv=pd.read_csv("BDATOS/ventas.csv")       # Se lee l base de datos de ventas
    print(cv)                                 # Se imprimen los datos
    cv1=cv.iloc[:,1]                          # Se crea una lista con los valores en dinero por ventas
    cv2=cv.iloc[:,2]                          # Se crea una lista con las fechas


    CE=[cv1,cv2]                               # Se crea una lista principal con las antriores listas

    cce2=pd.DataFrame(CE)                      # Se crea una nuevo DataFrame con los datos anteriores
    cce3=cce2.transpose()                      # Se transpone el DataFrame

    Vtotalventas=cce3['Vtotal'].sum()          # Se suma todos los valores de la ventas

    print("\n\n\n\nHasta fecha actual ", f55)  # Se imprime la fecha del informe

    print("\n\nEl total de dinero ingresado por ventas: $",Vtotalventas,"\n\n") # Se imprime el valor total en dinero de todas las ventas
    break                                      # Finaliza el ciclo de esta función


def ingventasTF():    # Se crea función para sumar el total ingresos en dinero por ventas por fecha específica
  while True:         # Se activa el ciclo para ejecutar la función de ingreso de dinero por ventas por fecha específica
    print("\n\n\n\n Página de ingresos en dinero por ventas\n\n")   # Se imprime titulo de esta sección
    print("\n\n Sistema para fechas\n\n\n\n")                      # Se imprime subtitulo de esta scción


    ing=pd.read_csv("BDATOS/ventas.csv")   # Se lee la base de datos de ventas   
    print(ing)                             # Se imprime la base de datos de ventas

    if1=int(input("\n\n\n\nIngrese la fecha inicial: "))  # Sirve para ingresar la fecha inicial para crear un intervalo de búsqueda
    if2=int(input("\n\n\n\nIngrese la fecha final: "))    # Sirve para ingresar la fecha final para crear un intervalo de búsqueda


    ing2=ing[(ing['Fecha']>=if1) & (ing['Fecha']<=if2)]   # Se crea un filtro para localizar los datos en el intervalo de tiempo específicado
    ing3=pd.DataFrame(ing2)                               # Se crea un nuevo DataFrame con los datos encontrados


    ing5=ing3['Vtotal'].sum()                 # Suma el valor en dinero de ventas entre un intervalo de tiempo

    print("\n\n\n\nEntre las fechas ", if1," y ",if2) # Se imprime las fechas del intervalo
    print("\n\nEl total de dinero ingresado por ventas es: $",ing5,"\n\n\n\n") # Se imprime el valor de dinero localizado por ventas


    
    break                                    # Se termina el ciclo de esta función


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



    ing=pd.read_csv("BDATOS/ventas.csv")    # Se lee la base de datos de ventas 
    print(ing)                              # Se imprime la base de datos de ventas



    ing2= ing[(ing['Fecha']==IF)]           # En la base de datos de ventas se busca la información con referencia a una fecha especifica
    ing3=pd.DataFrame(ing2)                 # Se crea un nuevo DataFrame con los datos encontardos anteriormente


    ing5=ing3['Vtotal'].sum()               # Se suman  el valor en dinero de todas las ventas entre un intervalo de tiempo


    cont2=pd.read_csv("BDATOS/contabilidad1.csv")  # Se lee la base de datos de contabilidad
    kq=len(cont2)                                  # se halla la cantidad de filas y se convierte en una constante
    print(kq)                                      # Se imprime la cantidad de filas
    capbase=cont2.iloc[kq-1,1]                     # SE encuentra la última fila de la base de datos para la fecha
    aux1=cont2.iloc[kq-1,5]                        # Se encuentra la ultima fila de la base de datos para entradas de dinero extra
    porc=cont2.iloc[kq-1,6]                        # se encuentra la ultima fila para el porcentaje de ganancia
    ganancianeta= ing5*porc/100     # operación matemática para hallar la ganancia diaria

    aux=ing5-ganancianeta           # operación matemática para extraer el capital para reinvertir

    cap=capbase+aux+aux1            # Se actualiza el capital base del negocio
    Disponible= cap-F5-TotalCFF     # Se resta al capital los costos de compras de productos y costos fijos de funcionamiento diarios
    cap= Disponible                 # Se actualiza el capital base del negocio

    cont=[]                         # Se crea una lista
    cont=[IF,cap,F5,TotalCFF,ing5,Ent,porc,ganancianeta,Disponible]  # Se ingresa a las lista la fecha seleccionada, capital base, compras en bodega,
                                                                     # costos fijos, entrada de dinero extra, porcentaje de ganancia, Dinero disponibe después de pagar facturas y costos

    cont1=pd.DataFrame(cont)                                         # Se crea un nuevo DataFrame con los valores anteriores
    cont2=pd.DataFrame.transpose(cont1)                              # Se transpone el DataFrame anterior
    # Se coloca nombre a  las columnas del nuevo DataFrame
    cont2.columns=['IF','capitalbase','CBodega','Cfijos','Ventas','EntradaExtra','porc','ganancianeta','Disponible']
    cont2.to_csv("BDATOS/contabilidad1.csv", mode="a", index="", header="") # Se graba los nuevos datos a la base del contabilidad
    cont2=pd.read_csv("BDATOS/contabilidad1.csv")                           # Se lee la base de datos de contabilidad
    print(cont2.iloc[:,0:5])                                                # Se imprime la primer parte de los datos de la base contabilidad
    print(cont2.iloc[:,5:9])                                                # Se imprime la segunad parte de los dtos de la base contabilidad
    break



   


    
print("\t\t\t\t PÁGINA PRINCIPAL DE CONTABILIDAD \n\n")    # se imprime el titulo de la página del menu del manejo operativo del negocio


def menu():                                                # se crea un menu para el manejo operativo del negocio
    
    print("\n\n\n\nSelecciona una opción \n")              # se imprime mensaje del menú
    print("\t7.1 - Costos de Bodega completa ")            # se imprime registro de costos de bodega forma completa
    print("\t7.2 - Costos de bodega por fechas")           # se imprime registro de costos de bodega forma fechas específicas
    print("\t7.3 - Ingreso de datos para costos fijos")    # se imprime opción para anexar datos de costsos fijos
    print("\t7.4 - Costos fijos completos")                # se imprime el registro de costos fijos la base completa
    print("\t7.5 - Costos fijos por fecha")                # se imprme el registro  de costos fijos la base por fecha específica
    print("\t7.6 - Ingresos por ventas - completa")        # se imprime el registro de ventas la base completa
    print("\t7.7 - Ingresos por ventas - manejo por fechas") # Se imprime el registro de ventas la base por fecha específica
    print("\t7.8 - CONTABILIDAD")                          # se imprime la opción del control toal de la contabilidad
    print("\t9 - Terminar con uso de menu")              # se imprime finalizacón de menú
          
# Se crea un una iteración con while mientras se cumpla la condición
while True:                                              # se activa el ciclo while para activar el menú
      menu()                                             # se activa la función menú
      opcionMenu = input("\n Inserte el número de la opción: ")   # sirve para ingresar el valor de la opción seleccionada
                  
      if opcionMenu == "7.1":                            # Para activar la función costos de bodega forma completa
          print("\n\nhola\n\n")                          # imprime mensaje de saludo
          bodegacom()                                    # la función costos de bodega de forma completa se ejecuta
     
           

        
      elif opcionMenu == "7.2":                          # Para activar la función costos de bodega forma por fechas específicas
             bodegafecha()                               # la función costos de bodega de forma por fechas específicas se ejecuta
      

      elif opcionMenu == "7.3":                          # se activa la función ingresos de datos para costos fijos
             ingcostosf()                                # Se ejecuta la función ingresos de datos para costos fijos
        
      elif opcionMenu == "7.4":                          # se activa la función costos fijos forma completa
            costosf()                                    # Se ejecuta la función costos fijos forma completa

      elif opcionMenu == "7.5":                          # se activa la función costos fijos forma fecha específica
             costosff()                                  # Se ejecuta la función costos fijos forma fecha específica


      elif opcionMenu == "7.6":                          # se activa la función ventas en forma completa
             ingventasT()                                # se ejecuta la función ventas en forma fechas específica

      elif opcionMenu == "7.7":                          # se activa la función ventas en forma fechas específica
              ingventasTF()                              # se ejecuta la función ventas en forma fechas específica

      elif opcionMenu == "7.8":                          # se activa la función contabilidad total del negocio
             contabilidad()                              # se ejecuta la función contabilidad total del negocio

      #elif opcionMenu == "9":                           # se elige la activa la opción finalizar menú
          #print("\n\n\t\tSistema finalizado")           # mensaje que confirma la finalización del menu
         # break                                         # se finaliza el ciclo if del menú
            


