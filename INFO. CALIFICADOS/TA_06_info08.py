#Advertencia:
# Si hay una gráfica abierta para poder volver al menú de opciones debe primero cerrar
# la gráfica en el cuadro superior derecho en la X y luego en la ventana de la consola 
# utilizar el scroll del mouse,  ir la final de la pantalla y encontrará el menú disponible.


from datetime import date as dt       #librería para manejar fechas
from datetime import datetime as dtt  #librería para manejar el tiempo
from datetime import timedelta        #librearía para realizar operaciones matemáticas con el tiempo
import pandas as pd                   # Librería para utilizar y manipular dataframe
import numpy as np                    # Librería para realizar operaciones matemáticas y manejo de matrices
import os                             # Librerías para realizar funciones internas del software
import csv                            # Librería para manipular archivos con extensión csv
import time                           # Librería para manipular el tiempo
import matplotlib.pyplot as plt       # Librería para generar gráficas
import openpyxl                       # Librería para leer y escribir archivos excel


def proveedor(): # se crea funcion proveedor
  while True:    # activa la función proveedor

    CA0=[]  # se crea lista para almacenar el nombre de la empresa
    PP01=[] # se crea lista para almacenar el nombre del vendedor
    PP02=[] # se crea lista para almacenar el primer apellido del vendedor
    PP03=[] # se crea lista para almacenar el segundo apellido del vendedor
    PP04=[] # se crea lista para almacenar el número del celular de la empresa 
    PP05=[] # se crea lista para almacenar el teléfono de la empresa
    PP06=[] # se crea lista para almacenar el correo de la empresa
    PP07=[] # se crea lista para almacenar el primer día de visita del vendedor
    PP08=[] # Se crea lista para almacenar el segundo día de visita del vendedor

  
    print("\t\t\t\t\t              PÁGINA PROVEEDORES")      # titulo de la página de proveedores
    PPP01=input("\n\nIngrese el nombre de la empresa: ")             # Para ingresar el nombre de la empresa
    PPP02=input("\n\nIngrese el nombre del vendedor: ")              # Para ingresar el nombre del vendedor
    PPP03=input("\n\nIngrese el primer apellido de vendedor: ")      # Para ingresar el primer apellido del vendedor
    PPP04=input("\n\nIngrese el segundo apellido del vendedor: ")    # Para ingresar el segundo apellido del vendedor
    PPP05=input("\n\nIngrese el numero de celular de la empresa: ")  # para ingresar el número del celular de la empresa
    PPP06=input("\n\nIngrese el numero fijo de la empresa: ")        # Para ingresar el teléfono fijo de la empresa
    PPP07=input("\n\ningrese el correo de la empresa: ")                 # para ingresar el correo de la empresa
    PPP08=input("\n\nIngrese el primer dia de visita de la semana: ")    # Para ingresar el primer día de visita del vendedor
    PPP09=input("\n\ningrese el segundo dia de visita: ")                # Para ingresar el segundo día de visita del vendedor
   
    CA0.append(PPP01)    # Para anexar el nombre de la empresa a la lista correspondiente
    PP01.append(PPP02)   # Para anexar el nombre del vendedor a la lista correspondiente
    PP02.append(PPP03)   # Para anexar el primer apellido del vendedor a la lista correspondiente
    PP03.append(PPP04)   # Para anexar el segundo apellido del vendedor a la lista correspondiente
    PP04.append(PPP05)   # para anexar el número del celular de la empresa a la lista correspondiente
    PP05.append(PPP06)   # Para anexar el teléfono fijo de la empresa a la lista correspondiente
    PP06.append(PPP07)   # para anexar el correo de la empresa a la lista correspondiente
    PP07.append(PPP08)   # Para anexar el primer día de visita del vendedor a la lista correspondiente
    PP08.append(PPP09)   # Para anexar el segundo día de visita del vendedor a la lista correspondiente
   
  
    CL=(CA0,PP01,PP02,PP03,PP04,PP05,PP06,PP07,PP08)      # se crea lista con los datos del proveedor
    PL01=pd.DataFrame(CL)                                 # Se crea DataFrame con los datos del proveedor
    PL02=pd.DataFrame.transpose(PL01)                     # se transpone el DataFrame
    # Se agrega nombres a las columnas
    PL02.columns=["Empresa","NVendedor","Papellido","Sapellido","Celular","Fijo","Correo","Pvisita","Svisita"]
    PL02.to_csv('BDATOS/proveedor.csv', mode="a", index="", header="") # se graba la información en la base de datos de proveedor
    os.system('clear')                                                 # Para limpiar la pantalla
    PL03=pd.read_csv('BDATOS/proveedor.csv')                           # se lee la base de datos de proveedor
    print(PL03)                                                        # Se imprime la base de datos del proveedor
  
    break                                                              # Finalización del ciclo  de esta función


def Bproveedores():     # Función para crear un resumen de la base de datos de proveedores
  while True:           # se activa ciclo para activar la funcion anterior
    #os.system('clear')  # Para limpiar pantalla
    PL03=pd.read_csv('BDATOS/proveedor.csv')  # para leer la base de datos de proveedores
    print("\n\n\n\n*****************************************************************************") # Decoración de pantalla
    print("\n\n**********************  PAGINA PRINCIPAL DE PROVEEDORES  ************************") # Titulo de la página principal de proveedores
    print("\n\n*****************************************************************************")     # Decoración de pantalla
    print("\n\n",PL03)  # para imprimir la base de datos de proveedores 
    break               # para finalizar el ciclo de esta función 


#os.system('clear') #limpiar pantalla


#funcionando
# Valor de productos por paca

def PRpaca():      # Se crea función para realizar informe de los precios de las pacas por productos
  while True:      # Se activa la función anterior
    co = pd.read_csv("BDATOS/bodega1.csv")  # Se lee la base de datos de bodega
    cp=co['Producto']                       # Se extrae los nombres de los productos
    co2=co['Ppaca']                         # Se extrae el precio de las pacas por producto
    C=[cp,co2]                              # Se crea una lista con los datos anteriores
    co5=pd.DataFrame(C)                     # Se crea un DataFrame con los datos anteriormente seleccionados
    co6=pd.DataFrame.transpose(co5)         # Se transpone el DataFrame anterior
    #print(co6)                             # Se imprime los datos del DataFrame anterior
    co6.set_index('Producto',inplace=True)  # Los nombres de los productos se convierten en index para el DataFrame
   # print(co6)                             # Se imprime el DataFrame modificado
    print("\n\n**************************************************************************************") # Decoración de pantalla
    print("\n\n                            Informe estadístico de precio por paca") # Se imprime mensaje para informe estadístico
    print("\n\n**************************************************************************************") # Decoración de pantalla
    GP=co2.describe()                       # Se crea el informe estadístico
    print("\n\n")                           # salto de línea
    print(GP)                               # Se imprime los resultados en el informe estadístico
    co6.plot( kind = 'bar')                 # Se crea gráfica en barras para el Dataframe modificado
    plt.title("INFORME DE BODEGA\n VALOR DE LOS PRODUCTOS POR PACA") # Se agrega titulo a la gráfica
    plt.ylabel('Precio en pesos')                                    # se agrega titulo al eje Y
    plt.xlabel('Producto')                                           # Se agrega titulo al eje X
    plt.show()                                                       # Se muestra la gráfica generada
    break                                                            # Se finaliza el ciclo para esta función
    

# funcionando
# Para ventas

def Ifventas():   # Se crea función para realizar informe de las ventas diarias
  while True:     # Se activa la función anterior
    fventas = pd.read_csv("BDATOS/ventas.csv") # Se lee la base de datos de ventas
    f1=fventas['Vtotal']                       # Se extrae los valores de las ventas
    f2=fventas['Fecha']                        # Se extrae las fechas
    C1=[f1,f2]                                 # Se crea una lista con los datos anteriores
    ffventas=pd.DataFrame(C1)                  # Se crea un DataFrame con los datos anteriormente seleccionados
    ff1ventas=pd.DataFrame.transpose(ffventas) # Se transpone el DataFrame anterior
    #print(ff1ventas)                          # Se imprime los datos del DataFrame anterior
    ff1ventas.set_index('Fecha',inplace=True)  # Las fechas se convierten en index para el DataFrame
    #print(ff1ventas)                          # Se imprime el DataFrame modificado
    print("\n\n**************************************************************************************") # Decoración de pantalla
    print("\n\n                             Informe estadístico de ventas diarias") # Se imprime mensaje para informe estadístico
    print("\n\n**************************************************************************************") # Decoración de pantalla
    GF=f1.describe()                           # Se crea el informe estadístico
    print("\n\n")                           # salto de línea
    print(GF)                                  # Se imprime los resultados en el informe estadístico
    ff1ventas.plot( kind = 'bar')              # Se crea gráfica en barras para el Dataframe modificado
    plt.title("INFORME DE VENTAS\nVALOR DE LAS VENTAS DIARIAS")    # Se agrega titulo a la gráfica
    plt.ylabel('Precio en pesos')                                  # se agrega titulo al eje Y
    plt.xlabel('Fecha')                                            # Se agrega titulo al eje X
    plt.show()                                                     # Se muestra la gráfica generada
    
    break                                                          # Se finaliza el ciclo para esta función



# Funcionando
# unidades en bodega

def Ubodega():    # Se crea función para realizar informe de La cantidad de unidades de los  productos en la bodega
  while True:     # Se activa la función anterior
    co = pd.read_csv("BDATOS/bodega1.csv")  # Se lee la base de datos de bodega
    cpp=co['Producto']                      # Se extrae los nombres de los productos
    cco2=co['unidades']                     # Se extrae la cantidad de unidades de productos en la bodega
    C=[cpp,cco2]                            # Se crea una lista con los datos anteriores
    co6=pd.DataFrame(C)                     # Se crea un DataFrame con los datos anteriormente seleccionados
    co7=pd.DataFrame.transpose(co6)         # Se transpone el DataFrame anterior
    co7.set_index('Producto',inplace=True)  # Los nombres de los productos se convierten en index para el DataFrame
    #print(co7)                             # Se imprime el DataFrame modificado
    print("\n\n**************************************************************************************") # Decoración de pantalla
    print("\n\n                           Informe estadístico de unidades disponibles en bodega") # Se imprime mensaje para informe estadístico
    print("\n\n**************************************************************************************") # Decoración de pantalla
    GU=cco2.describe()                      # Se crea el informe estadístico
    print("\n\n")                           # salto de línea
    print(GU)                               # Se imprime los resultados en el informe estadístico
    
    
    co7.plot( kind = 'bar')                 # Se crea gráfica en barras para el Dataframe modificado
    plt.title("INFORME DE BODEGA\n CANTIDAD DE UNIDADES POR PRODUCTO") # Se agrega titulo a la gráfica
    plt.ylabel('Cantidad de unidades')                                 # se agrega titulo al eje Y
    plt.xlabel('Producto')                                             # Se agrega titulo al eje X
    plt.show()                                                         # Se muestra la gráfica generada

    break                                                              # Se finaliza el ciclo para esta función



def infcontabilidad():   # Se crea función para realizar informe Total de los principales datos en contabilidad
  while True:            # Se activa la función anterior

    inf= pd.read_csv("BDATOS/contabilidad1.csv") # Se lee la base de datos de contabilidad
    #print(inf)                                   # Se imprime la información de la base de datos contabilidad

    inf1=inf['IF']                               # Se extrae las fechas de las operaciones
    inf2=inf['capitalbase']                      # Se extrae los datos del capital base
    inf3=inf['CBodega']                          # Se extrae los costos de la bodega
    inf4=inf['Cfijos']                           # Se extrae los costos fijos de funcionamiento
    inf5=inf['ganancianeta']                     # Se extrae los extrae la ganancia neta
    print("\n\n**************************************************************************************") # Decoración de pantalla
    print("\n                            INFORME DE CONTABILIDAD") # Se imprime mensaje para informe estadístico 
    print("\n **************************************************************************************") # Decoración de pantalla
    print("\n\n--------------------------------------------------------------------------------------") # Decoración de pantalla
    print("\n                        Informe estadístico de capital base") # Se imprime mensaje para informe estadístico 
    print("\n--------------------------------------------------------------------------------------") # Decoración de pantalla
    G2=inf2.describe()                                    # Se crea el informe estadístico para capital base
    print("\n\n")                           # salto de línea
    print(G2)                                             # Se imprime los resultados en el informe estadístico
    
    print("\n\n\n--------------------------------------------------------------------------------------") # Decoración de pantalla
    print("\n                         Informe estadístico de costos de bodega") # Se imprime mensaje para informe estadístico 
    print("\n--------------------------------------------------------------------------------------")
    G3=inf3.describe()                                        # Se crea el informe estadístico para costos de bodega
    print("\n\n")                           # salto de línea
    print(G3)                                                 # Se imprime los resultados en el informe estadístico

    print("\n\n\n--------------------------------------------------------------------------------------")
    print("\n                         Informe estadístico de costos de fijos") # Se imprime mensaje para informe estadístico 
    print("\n--------------------------------------------------------------------------------------")
    G4=inf4.describe()                                       # Se crea el informe estadístico costos fijos de funcionamiento
    print("\n\n")                           # salto de línea
    print(G4)                                                # Se imprime los resultados en el informe estadístico
    print("\n\n\n--------------------------------------------------------------------------------------")
    print("\n                         Informe estadístico de ganancia neta") # Se imprime mensaje para informe estadístico 
    print("\n-------------------------------------------------------------------------------------")
    G5=inf5.describe()                                     # Se crea el informe estadístico para ganancia neta
    print("\n\n")                           # salto de línea
    print(G5)                                              # Se imprime los resultados en el informe estadístico

    C41=[inf1,inf2,inf3,inf4,inf5]                         # Se crea una lista con los datos anteriores

    C411=pd.DataFrame(C41)                                 # Se crea un DataFrame con los datos anteriormente seleccionados
    
    C43=pd.DataFrame.transpose(C411)                       # Se transpone el DataFrame anterior
    C43.plot(x="IF", y=["capitalbase","CBodega","Cfijos","ganancianeta"],kind='bar') # Se crea gráfica en barras para el Dataframe modificado
    plt.title("INFORME DE CONTABILIDAD\n ")                # Se agrega titulo a la gráfica
    plt.ylabel('DINERO EN MILLONES')                       # se agrega titulo al eje Y
    plt.xlabel('\nFECHA')                                  # Se agrega titulo al eje X
    plt.legend(loc="lower left", bbox_to_anchor=(0.8,0.9)) # Se agrega legenda para explicación de la gráfica 
    plt.show()                                             # Se muestra la gráfica generada
    
    
    break                                                  # Se finaliza el ciclo para esta función

    

os.system('clear') 
print("\n\n\t\t\t\t          PÁGINA PRINCIPAL DE PROVEEDORES") # se imprime el titulo de la página principal de proveedores


def menu():                                               # se crea un menu para el manejo operativo del negocio
    
    print("\n\nSelecciona una opción \n")             # se imprime mensaje del menú
    print("\t8.1 - Ingreso de proveedores ")              # se imprime ingreso de proveedores
    print("\t8.2 - Base de datos de proveedores")         # se imprime resumen de la base de datos de proveedores
    print("\t8.3 - Informe del valor de productos por paca") # se imprime informe  del valor de productos por paca
    print("\t8.4 - Informe del valor de las ventas diarias") # se imprime el informe de las ventas diarias
    print("\t8.5 - Informe total de unidades en bodega")     # se imprme el informe total de las unidades en bodega
    print("\t8.6 - Informe total de contabilidad")           # se imprime el informe total de contabilidad
    print("\t9   - Terminar con uso de menu")                  # se imprime finalizacón de menú
          
# Se crea un una iteración con while mientras se cumpla la condición
while True:                                              # se activa el ciclo while para activar el menú
      menu()                                             # se activa la función menú
      opcionMenu = input("\n Inserte el número de la opción: ")   # sirve para ingresar el valor de la opción seleccionada
      os.system('clear')                                          # Para limpiar la pantalla 
      if opcionMenu == "8.1":                            # Para activar la función ingreso de proveedores
          print("\n\nhola\n\n")                          # imprime mensaje de saludo
          proveedor()                                    # la función ingreso de proveedores se ejecuta
     
           

        
      elif opcionMenu == "8.2":                          # Para activar la función resumen de la base de datos de proveedores
             Bproveedores()                              # la función resumen de la base de datos de proveedoresse ejecuta
      

      elif opcionMenu == "8.3":                          # se activa la función informe  del valor de productos por paca
             PRpaca()                                    # Se ejecuta la función informe  del valor de productos por paca
        
      elif opcionMenu == "8.4":                          # se activa la función  informe de las ventas diarias
            Ifventas()                                   # Se ejecuta la función  informe de las ventas diarias

      elif opcionMenu == "8.5":                          # se activa la función informe total de las unidades en bodega
             Ubodega()                                   # Se ejecuta la función informe total de las unidades en bodega

      elif opcionMenu == "8.6":                          # se activa la función informe total de contabilidad
             infcontabilidad()                           # se ejecuta la función informe total de contabilidad
      

      elif opcionMenu == "9":                           # se elige la activa la opción finalizar menú
          print("\n\n\t\tSistema finalizado")           # mensaje que confirma la finalización del menu
          break                                         # se finaliza el ciclo if del menú









