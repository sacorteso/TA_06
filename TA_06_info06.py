from datetime import date as dt
from datetime import datetime as dtt
from datetime import timedelta
import pandas as pd # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os           # Librerías para realizar funciones internas del software
import csv 
import time
today=dt.today()
#print(today)
f5=today.strftime('%Y%m%d')
f55=int(f5)
print(f55)
f56=time.strftime('%H:%M:%S')
print(f56)


ce=[] # Se crea lista para almacenar la identificación del cliente
c1=[] # Se crea lista para almacenar la referencia del producto
c2=[] # Se crea lista para almacenar el nombre del producto
c3=[] # Se crea lista para almacenar el valor unitario del producto
c4=[] # Se crea lista para almacenar la cantidad de productos que se va a comprar un cliente respecto a una referencia determinada
c5=[] # Se crea lista para almacenar el subtotatal de la compra por referencia de producto
c6=[] # Se crea lista para almacenar la fecha
c7=[] # Se crea lista para almacenar la hora
cc= input("\n\nIngrese la identificación del cliente: ")
cc=int(cc)

z1= input("\n\ningrese la cantidad de productos que se van a vender: ")
z=int(z1)
zz1=0
zz2=0
subtotal=0
#compras=pd.DataFrame()
subtotal=[]
for k in range(z):
  print(k)
  L6 =pd.read_csv("BDATOS/mostrador.csv") 
  print(L6.iloc[:,0:2])
  Ref1= input("\n\nIngrese la referencia del producto: ")
  Ref= str(Ref1)
  can= input("\n\nIngrese la cantidad de producto:  ")
  can= int(can)
  for kk in range(len(L6)):
    if(L6.iloc[kk,1]==Ref):
      zz1= L6.iloc[kk,0]
      zz2= L6.iloc[kk,6]
      subtotal= zz2*can

      ce.append(cc)
      c1.append(Ref)
      c2.append(zz1)
      c3.append(zz2)
      c4.append(can)
      c5.append(subtotal)
      c6.append(f55)
      c7.append(f56)
      
      factura=(ce,c1,c2,c3,c4,c5,c6,c7)
      factura1=pd.DataFrame(factura)
      factura2=pd.DataFrame.transpose(factura1)
      factura2.columns=['Cedula','Referencia','Nproducto','Punitario','Cantidad','Subtotal','Fecha','Hora']
      
      temporal=pd.DataFrame.transpose(factura1)
      temporal.columns=['Cedula','Referencia','Nproducto','Punitario','Cantidad','Subtotal','Fecha','Hora']
      
      temporal.to_csv('BDATOS/temporal.csv', mode="a", index="", header="")
      


      factura2.to_csv('BDATOS/factura.csv', mode="a", index="", header="")
  
  temporal22=pd.read_csv('BDATOS/factura.csv')
  #print(temporal22)
  factura22=pd.read_csv('BDATOS/factura.csv')
  #print(factura22)
  Vtotal=temporal22['Subtotal'].sum()
  tem=temporal22.drop(['Fecha','Hora'], axis=1)
  c1=cc
  os.system('clear') 
  print("\n\n\n\n\t\t\t\t\t                  FACTURA DE VENTA")
  print("\n\n\n\n")
  print("Cédula: ",c1, "\t\t\t\t\tFecha: " ,       f55,   "\t\t\t\t\tHora: ",        f56)
  print("\n\n\n\n")
  print(tem)
  print("\n\n")
  print("\n\n\t\t           Valor total de la venta: ", Vtotal)



