


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
    print("\n\n\t\tPÁGINA PARA CAMBIAR EL PORCENTAJE DE GANANCIA EN FORMA INDIVIDUAL")
    print("\n\n\t\tReferencia en productos en Bodega\n\n")

    m2=pd.read_csv("BDATOS/mostrador.csv")
    m22=m2.iloc[:,0:2]
    print(m22)

    g2=input("\n\n\n\ningrese la referencia del producto: ")
    g3= str(g2)

    m5= m2[m2['Referencia']==g3]
    print("\n\n\n\n   Datos de  Referencia ingresada \n\n",  m5)


    mg=input("\n\n\n\nIngrese el nuevo porcentaje de ganancia del producto: ")
    mg1= (mg)
    print("\n\n\n\n            Porcentaje de ganancia ingresado:",  mg1)


    float()
    z1= 97
    for TM in range(len(m2)):
     # ciclo para comparar con todas las claves con la base de datos
     #TM=m2.iloc[TM,5]
     #print(TM)                    # Permite hallar una clave  en una posición determinada
     if (m2.iloc[TM,1]==g3):
          m2.iloc[TM, 5]=mg
          m2.to_csv('BDATOS/mostrador.csv', mode="w",index="", header="True")
          m2.iloc[TM, 6]= z1
          m2=pd.read_csv("BDATOS/mostrador.csv")
          z1=m2.iloc[TM,3]
          z2=m2.iloc[TM,5]
          zz= (z1*z2/100)+z1
          m2.iloc[TM,6]=zz
          m2.to_csv('BDATOS/mostrador.csv',mode="w", index="", header="True")
          #print(zz)
          
          aa5 =pd.read_csv("BDATOS/mostrador.csv")  
          print(aa5)
    else:
      break     

  
