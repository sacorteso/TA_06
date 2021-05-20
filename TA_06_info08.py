from datetime import date as dt #librería para manejar fechas
from datetime import datetime as dtt  #librería para manejar el tiempo
from datetime import timedelta        #librearía para realizar operaciones matemáticas con el tiempo
import pandas as pd # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os           # Librerías para realizar funciones internas del software
import csv          # Librería para manipular archivos con extensión csv
import time         # Librería para manipular el tiempo

def proveedor(): # se crea funcion proveedor
  while True:

    CA=[]#se crea lista para almacenar la indentificacion del cliente
    PP1=[]#se crea lista para almacenar la referencia del producto
    PP2=[]#se crea lista para almacenar el nombre del producto
    PP3=[]#se crea lista para almacenar el valor unitario del producto
    PP4=[]#se crea lista para almacenar la cantidad de productos que se va a comprar un cliente respecto a una referencia determinada 
    PP5=[]#se crea lista para almacenar el subtotal de la compra por referencia de producto
    PP6=[]#se crea lista para almacenar la fecha
    PP7=[]#se crea lista para almacenar la hora
    print("\n\n\n\n\t\t\t\t\t              PÁGINA PROVEEDORES") # titulo de la página de clientes
    PPP1=input("\n\nIngrese el nombre de la empresa: ")          # Para ingrese la identificación
    PPP2=input("\n\nIngrese el nombre del vendedor: ")        # Para ingresar el nombre del cliente
    PPP3=input("\n\nIngrese el primer apellido de vendedor: ")           # Para ingresar el primer apellido del cliente
    PPP4=input("\n\nIngrese el segundo apellido del vendedor: ")          # Para ingresar el segundo apellido del cliente
    PPP5=input("\n\nIngrese el numero de celular de la empresa: ")         # para ingresasar el número del celular
    PPP6=input("\n\nIngrese el numero fijo de la empresa: ")       
    PPP7=input("ingrese el correo de la empresa: ")        # para ingresar el número del teléfono fijo
    PPP8=input("Ingrese el primer dia de visita de la semana: ")
    PPP9=input("ingrese el segundo dia de visita: ")
    CA.append(PPP1) #se crea lista para almacenar la identificacion del cliente
    PP1.append(PPP2) #se crea lista para almacenar la identificacion del cliente
    PP2.append(PPP3) #se crea lista para almacenar la identificacion del cliente
    PP3.append(PPP4) #se crea lista para almacenar la identificacion del cliente
    PP4.append(PPP5) #se crea lista para almacenar la identificacion del cliente
    PP5.append(PPP6) #se crea lista para almacenar la identificacion del cliente
    CL=(CA,PP1,PP2,PP3,PP4,PP5)      # se crea lista con los datos del cliente
    PL1=pd.DataFrame(CL)             # Se crea DataFrame con los datos del cliente
    PL2=pd.DataFrame.transpose(PL1)  # se transpone el DataFrame
    PL2.to_csv('BDATOS/clientes.csv', mode="a", index="", header="") # se graba la información del cliente en la base de datos clientes
    PL3=pd.read_csv('BDATOS/clientes.csv')  # se lee la base e datos de cliente
    print(PL3)                              # Se imprime la base de datos cliente
  #else:
    break