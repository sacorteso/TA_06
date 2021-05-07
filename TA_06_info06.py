from datetime import date as dt #librería para maejar fechas
from datetime import datetime as dtt  #librería para manejar el tiempo
from datetime import timedelta        #librearía para realizar operaciones matemáticas con el tiempo
import pandas as pd # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os           # Librerías para realizar funciones internas del software
import csv          # Librería para manipular archivos con extensión csv
import time         # Librería para manipular el tiempo



today=dt.today()            # comando que muestra la fecha actual
f5=today.strftime('%Y%m%d') # para cambiar el formato de fecha y unirlo
f55=int(f5)                 # para convertir la fecha en un entero para operciones matemáticas
print(f55)                  # para imprimir la hora
f56=time.strftime('%H:%M:%S') # pra modificar el foramto de la hora
print(f56)                    # para imprimir la hora


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

z1= input("\n\ningrese la cantidad de productos que se van a vender: ") # para crear un ciclo en donde se estima la cantidad de productos que hay que registrar
z=int(z1)                  # Se convierte el valor del ciclo en un entero
zz1=0                      # para generar variable para el nombre
zz2=0                      # para generar variable para el precio individual del producto
subtotal=[]                # para geneerar variables del valor subtotal ed la venta


for k in range(z):         # se crea una iteración para registrar las los productos que se van a vender
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
          
temporal22=pd.read_csv('BDATOS/temporal.csv')  # Para leer la base de datos temporal
  
factura22=pd.read_csv('BDATOS/factura.csv')   # Para leer la base de datos de factura
  
Vtotal=temporal22['Subtotal'].sum()  # para sumar el valor total de la compra de productos
tem=temporal22.drop(['Fecha','Hora'], axis=1) # Para eliminar columnas de la fecha y hora
c1=cc                                # variable para la identificcaión del cliente
c2= Vtotal                           # variable para el valor total de la compra
os.system('clear')                         # para limpiar la pantalla
print("\n\n\n\n\t\t\t\t\t                  FACTURA DE VENTA") # titulo de la página factura de venta
print("\n\n\n\n")                          #salto de linea                    
print("Cédula: ",c1, "\t\t\t\t\tFecha: " ,       f55,   "\t\t\t\t\tHora: ",        f56) # para insertar cédula, fecha , hora
print("\n\n\n\n")                          # salto de línea
print(tem)                                 # Se imprime datos de la compra para la factura
print("\n\n")                              # salto de linea
print("\n\n\t\t           Valor total de la venta: ", Vtotal)  # se imprime el valor total de la venta


ventas=(c1,c2,f55,f56)                     # Se crea lista para ventas totales
ventas1=pd.DataFrame(ventas)               # Se crea dataframe para ventas totales
ventas2=pd.DataFrame.transpose(ventas1)    # se transpone el dataframe para organizar los datos
ventas2.columns=['Cedula','Vtotal','Fecha','Hora'] # se coloca nombres a las columnas
ventas2.to_csv('BDATOS/ventas.csv', mode="a", index="", header="") # Se graba los datos para ventas totales en el archivo ventas.csv
ventas2= pd.read_csv('BDATOS/ventas.csv')  # para leer el contenido del archivo de ventas totales
print("\n\n\n\n",ventas2)                  # se imprime el contenido del archivo de ventas totales


#temporal.to_csv('BDATOS/temporal.csv', mode="w", index="", header="")
