from datetime import date as dt
from datetime import datetime as dtt
from datetime import timedelta
import pandas as pd # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os           # Librerías para realizar funciones internas del software
import csv 



z= input("ingrese la cantidad de productos que se van a vender: ")
z=int(z)
zz1=0
Ptotal=0
compras=pd.DataFrame()
subtotal=[]
for k in range(z):
  print(k)
  L6 =pd.read_csv("BDATOS/mostrador.csv") 
  print(L6.iloc[:,0:2])
  Ref=input("\n\nIngrese la referencia del producto: ")
  Ref=str(Ref)
  can=input("\n\nIngrese la cantidad de producto:  ")
  can= int(can)
  for kk in range(len(L6)):
    if(L6.iloc[kk,1]==Ref):
      zz1=int(L6.iloc[kk,6])
      print("\n\nPrecio individual de", L6.iloc[kk,0],  zz1)
      Ptotal= zz1*can
      print("\n\nPrecio total por producto", L6.iloc[kk,0], Ptotal)
      subtotal=(Ptotal)
      #c1=Ref
      #c2=L6.iloc[kk,0]
      #c3=zz1
      #c4=can
      #c5=Ptotal
      compras[kk,0]=Ref
      compras[kk,1]=L6.iloc[kk,0]
      compras[kk,2]=zz1
      compras[kk,3]=can
      compras[kk,4]=Ptotal
      
      #compras=pd.DataFrame(list(zip(c1,c2,c3,c4,c5)), columns=['Referencia','Nproducto','Preciopro','Cantidad','Subtotal'])
      compras.to_csv('BDATOS/ventas.csv',mode="w", index="", header="True")


  #Pindividual=L6.iloc