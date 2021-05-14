


# librerías para manejar base de datos
from datetime import date as dt
from datetime import datetime as dtt
from datetime import timedelta
import pandas as pd # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os           # Librerías para realizar funciones internas del software
import csv          # Librería para manipular archivos excel y con extensión .csv 

# listo para funcionamiento
# Para cambiar el porcentaje de forma individual
def ganancia():
  while True:
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
    print("\n\n\n\n            Porcentaje de ganancia ingresado:",  mg1)        # Confirma que el porcenatje ingresado es seleccionado


    float()           # se tranforma los datos a tipo float
    z1= 97            # Se crea una variable para operaciones matemáticas
    for TM in range(len(m2)):   # Se crea una iteración para revisar todas las refrencias
     # ciclo para comparar con todas las claves con la base de datos
     #TM=m2.iloc[TM,5]
     #print(TM)                    # Permite hallar una clave  en una posición determinada
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
    else:                                            # otra opción en el ciclo
          break                                      # cierra el ciclo







#listo para funcionamiento
# Para cambiar las unidades de forma individual
def unidades():
  while True:
    os.system('clear')
    print("\n\nPAGINA MOSTRADOR")
    print("\n\n\t\t PAGINA PARA CAMBIAR LAS UNIDADES EN FORMA INDIVIDUAL")
    print("\n\n\t\t Referencia en productos en Bodega\n\n")

    mm2=pd.read_csv("BDATOS/mostrador.csv")
    LL5=pd.read_csv('BDATOS/bodega1.csv')
    print(LL5)

    print("\n\n\n\n Mostrador actual")
    print("\n\n",mm2)


    g2=input("\n\n\n\nIngrese la referencia del producto")
    g3=str(g2)


    g4=input("\n\ningrese la fecha de compra del producto:   ")
    g5=int(g4)
    m5= LL5[LL5['Referencia']==g3]
    m6= LL5[LL5['Fcompra']==g5]
    os.system('clear')
    print("\n\n\n\nDatos de la bodega \n\n", m5)


    mu=input("\n\n\n\nIngrese la nueva cantidad de unidades del producto para mostrador: ")
    mu1= int(mu)


    mt=0
    for TM in range (len(mm2)):
      if (LL5.iloc[TM,2]==g3 and LL5.iloc[TM,6]==g5):
        LL5=pd.read_csv('BDATOS/bodega1.csv')
        mm2=pd.read_csv("BDATOS/mostrador.csv")

        mt= mm2.iloc[TM, 7]
        g6= LL5.iloc[TM, 4]
        mm2.iloc[TM, 4]=mu1
        mt=mu1+mt
        mm2.iloc[TM, 7]=mt
        mm2.to_csv('BDATOS/mostrador.cvs', mode="w", index="", header="True")
        g7=g6-mu1
        LL5.iloc[TM, 4]=g7
        mm2.iloc[TM, 4]=g7
        mm2.to_csv('BDATOS/mostrador.csv',mode="w", index="", header="True")
        LL5.to_csv('BDATOS/bodega1.csv', mode="w", index="", header="True")
        LL5=pd.read_csv('BDATOS/bodega1.csv')
        mm2=pd.read_csv('BDATOS/mostrador.csv')
        


    print("\n\n\n\n***************   Bodega actualizada    *******************)
    print("\n\n\n\n", LL5)
    print("\n\n\n\n***************   Mostrador actualizado   ****************")
    print("\n\n",mm2)
    
    break
def vencimiento():
  while True:
    today=dt.today()
    print(today)
    f5=today.strftime('%Y%m%d')
    f55=int(f5)
    print(f55)
    f25=today-timedelta(10)
    print(f25)
    f25=today.strftime('%Y%m%d')
    print(f25)
    f255=int(f25)
    print(f255)
    print("\n\n\n\n************   ALERTA DE PRODUCTO VENCIDO     ************")
    L5=pd.read_csv('BDATOS/bodega1.csv')
    for i in range(len(L5)):
      if(L5.iloc[i, 7]<=f55):
        print("\n\nproducto con nombre: ", L5.iloc[i, 1], " y referencia: "L5.iloc[i, 2]"    con fecha de compra: ",L5.iloc[i, 6] ) 
        print("\n\n                                                                          Esta vencido - reemplazar")

    print("\n\n\n\n***********     Alerta de producto cercano a vencerse    ******************")
    for i in range(len(L5)):
      L5=pd.read_csv('BDATOS/bodega1.csv')
      k=(L5.iloc[i,7])
      if( k>f225 ):
        if(<f55):
          print("HOLA")
          print("\n\nProducto con nombre: ", L5.iloc[i,1], " y referencia: ",L5.iloc[i,2],"     con fecha de compra: ", L5.iloc[i,6])
          print("\n\n")
    break  

'''
print("\t\t\t\t PÁGINA PRINCIPAL \n\n")                  # se imprime el titulo de la página del menu del manejo operativo del negocio

# función para activar el submenu de entrada de la página compras
def menu():                                              # se crea un menu para el manejo operativo del negocio
    
    print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
    print("\t1 - Cambio de porcentaje de ganancia ")                  # se imprime registro de compras
    print("\t2 - Para llenar el mostrador con productos")              # se imprime registro total acumulado
    print("\t3 - Vencimiento de productos")                     # se imprime ingreso abodega
    print("\t9 - Terminar con uso de menu")              # se imprime finalizacón de menú
          
# Se crea un una iteración con while mientras se cumpla la condición
while True:                                              # se activa el ciclo while para activar el menú
      menu()                                             # se activa la función menú
      opcionMenu = input("\n Inserte el número de la opción: ")   # sirve para ingresar el valor de la opción seleccionada
                  
      if opcionMenu == "1":                              # Para activar la función compra
          print("\n\nhola\n\n")                          # imprime mensaje de saludo
          ganancia()                                     # la función compra se ejecuta
     
           

        
      elif opcionMenu == "2":                            # Para activar la función total
             unidades()                                     # se ejecuta la función total
      

      elif opcionMenu == "3":                            # se activa la función bodega
             vencimiento()
        
     

      elif opcionMenu == "9":                            # se elige la activa la opción finalizar menú
          print("\n\n\t\tSistema finalizado")                    # mensaje que confirma la finalización del menu
          break                                          # se finaliza el ciclo if del menú         
'''