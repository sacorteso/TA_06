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






  


    
