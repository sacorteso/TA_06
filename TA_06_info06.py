

# ADVERTENCIA
# En la opción 6.5 se recomienda utilizar número de cédiula : 123



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

def venta():
  while True:
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


    for k in range(z):  # se crea una iteración para registrar las los productos que se van a vender.
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
    
       #ventas=(ce,ff7,f55,f56)                     # Se crea lista para ventas totales
       #ventas1=pd.DataFrame(ventas)               # Se crea dataframe para ventas totales
       #ventas2=pd.DataFrame.transpose(ventas1)    # se transpone el dataframe para organizar los datos
       #ventas2.columns=['Cedula','Vtotal','Fecha','Hora'] # se coloca nombres a las columnas
       #ventas2.to_csv('BDATOS/ventas.csv', mode="a", index="", header="") # Se graba los datos para ventas totales en el archivo ventas.csv
       #ventas2= pd.read_csv('BDATOS/ventas.csv')
   
    
  #else:
  #break
  #return c1
  #return c2



def Factura():
  while True:
    temporal22=pd.read_csv('BDATOS/temporal.csv')  # Para leer la base de datos temporal
    factura22=pd.read_csv('BDATOS/factura.csv')   # Para leer la base de datos de factura
    Vtotal=temporal22['Subtotal'].sum()  # para sumar el valor total de la compra de productos
    tem=temporal22.drop(['Fecha','Hora'], axis=1) # Para eliminar columnas de la fecha y hora
    #c1= int(cc)                                # variable para la identificcaión del cliente
    c2= Vtotal                           # variable para el valor total de la compra
    #return c2
    #os.system('clear')                         # para limpiar la pantalla
    print("\n\n\n\n\t\t\t\t\t                  FACTURA DE VENTA") # titulo de la página factura de venta
    print("\n\n\n\n")                          #salto de linea                    
    print("Cédula: ", "\t\t\t\t\tFecha: " ,       f55,   "\t\t\t\t\tHora: ",        f56) # para insertar cédula, fecha , hora
    print("\n\n\n\n")                          # salto de línea
    print(tem)                                 # Se imprime datos de la compra para la factura
    print("\n\n")                              # salto de linea
    print("\n\n\t\t           Valor total de la venta: ", Vtotal)  # se imprime el valor total de la venta\n
  #else:
    break
  
#c1= (c1)
#c2
#ventas=(c1,c2,f55,f56)                     # Se crea lista para ventas totales
#ventas1=pd.DataFrame(ventas)               # Se crea dataframe para ventas totales
#ventas2=pd.DataFrame.transpose(ventas1)    # se transpone el dataframe para organizar los datos
#ventas2.columns=['Cedula','Vtotal','Fecha','Hora'] # se coloca nombres a las columnas
#ventas2.to_csv('BDATOS/ventas.csv', mode="a", index="", header="") # Se graba los datos para ventas totales en el archivo ventas.csv
#ventas2= pd.read_csv('BDATOS/ventas.csv')


def Venta_acum():
  while True:
          # para limpiar la pantalla
    print("\n\n\n\n\t\t\t\t\t                 PÁGINA DE VENTAS ACUMULADAS") # titulo de la página factura de venta
    print("\n\n\n\n")                          #salto de linea                    
    print(           "\t\t\t\t\tFecha: " ,       f55,   "\t\t\t\t\tHora: ",        f56)
    #ventas=(c1,c2,f55,f56)                     # Se crea lista para ventas totales
    #ventas1=pd.DataFrame(ventas)               # Se crea dataframe para ventas totales
    #ventas2=pd.DataFrame.transpose(ventas1)    # se transpone el dataframe para organizar los datos
    #ventas2.columns=['Cedula','Vtotal','Fecha','Hora'] # se coloca nombres a las columnas
    #ventas2.to_csv('BDATOS/ventas.csv', mode="a", index="", header="") # Se graba los datos para ventas totales en el archivo ventas.csv
    ventas2= pd.read_csv('BDATOS/ventas.csv')  # para leer el contenido del archivo de ventas totales
    print("\n\n\n\n",ventas2)                  # se imprime el contenido del archivo de ventas totales
  #else:
    break

# Menú
def menu():                                              # se crea un menu para el manejo operativo del negocio
    print("\n\n\n\n\t\t\t\t\t              PÁGINA PRINCIPAL DE VENTAS Y CLIENTES\n\n") # titulo de la página factura de venta
    print("\n\n\n\n      Selecciona una opción \n")                    # se imprime mendsaje del menú
    print("\t            6.1 - Para generar venta ")                  # se imprime registro de compras
    print("\t            6.2 - Factura")              # se imprime registro total acumulado
    print("\t            6.3 - Venta acumulada")                     # se imprime ingreso abodega
    print("\t            6.4 - Página de clientes")              # se imprime finalizacón de menú
    print("\t            6.5 - Página de Compras de cada cliente")              # se imprime finalizacón de menú         
    print("\t            6.7 - Otras opciones")              # se imprime finalizacón de menú




def clientes():
  while True:

    CA=[]#se crea lista para almacenar la indentificacion del cliente
    PP1=[]#se crea lista para almacenar la referencia del producto
    PP2=[]#se crea lista para almacenar el nombre del producto
    PP3=[]#se crea lista para almacenar el valor unitario del producto
    PP4=[]#se crea lista para almacenar la cantidad de productos que se va a comprar un cliente respecto a una referencia determinada 
    PP5=[]#se crea lista para almacenar el subtotal de la compra por referencia de producto
    PP6=[]#se crea lista para almacenar la fecha
    PP7=[]#se crea lista para almacenar la hora
    print("\n\n\n\n\t\t\t\t\t              PÁGINA CLIENTES") # titulo de la página de clientes
    PPP1=input("\n\nIngrese el numero de cedula: ")          # Para ingrese la identificación
    PPP2=input("\n\nIngrese el nombre del cliente: ")        # Para ingresar el nombre del cliente
    PPP3=input("\n\nIngrese el primer apellido: ")           # Para ingresar el primer apellido del cliente
    PPP4=input("\n\nIngrese el segundo apellido: ")          # Para ingresar el segundo apellido del cliente
    PPP5=input("\n\nIngrese el numero de celular: ")         # para ingresasar el número del celular
    PPP6=input("\n\nIngrese el numero fijo: ")               # para ingresar el número del teléfono fijo
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

def compra_cliente():
   while True:
    print("\n\n\n\n\t\t\t\t\t              PÁGINA COMPRA DE CLIENTES") # titulo de la página de clientes
    CA=[]                   # se crea lista para almacenar la indentificacion del cliente
    PPP1=input("\n\n\n\nIngrese el numero de cedula: ")
    CA.append(PPP1)         # se crea lista para almacenar la identificacion del cliente

    PPPP = int(PPP1)        # Se convierte el valor de la identificación del cliente entero 
    print("\n\n")       # Salto de linea
    factura22=pd.read_csv('BDATOS/factura.csv')  # Para leer la base de datos de factura
    #print(factura22)                            # Para imprimir la base de datos de factura
    
    LK=0                                         # Se crea variable pata manejo de DataFrame
    for AA in range(len(factura22)):             # Se crea ciclo para leer la base datos factura respecto a la identificación de clientes
      if(factura22.iloc[AA, 0]==PPPP):           # Condición para leer la base  de adtos de factura
        factura22=pd.read_csv('BDATOS/factura.csv')  # Se lee la base de datos de factura
        LK=factura22.iloc[AA, :]                     # Se busca la identificación especifica
        LK1=pd.DataFrame(LK)                         # Se crea un DataFrame para leer los datos del cliente de las compras que ha realizado
        LK2=pd.DataFrame.transpose(LK1)              # Se transpone el DataFrame
        print("\n\n\n\n")                            # Salto de linea
        print(LK2)                                   # Se imprime los resultados de las compras del cliente.
    break
# Se crea un una iteración con while mientras se cumpla la condición
while True:                                              # se activa el ciclo while para activar el menú
      menu()                                             # se activa la función menú
      opcionMenu = input("\n Inserte el número de la opción: ")   # sirve para ingresar el valor de la opción seleccionada
                 
      if opcionMenu == "6.1": 
                                     # Para activar la función compra
          print("\n\nhola\n\n")             # imprime mensaje de saludo
          venta()                           # la función venta se ejecuta
     
           

        
      elif opcionMenu == "6.2":              # Para activar la función factura
             Factura()                       # se ejecuta la función factura
      

      elif opcionMenu == "6.3":              # se activa la función venta acunulada
             Venta_acum()                    # se ejecuta la función venta acumulada

      elif opcionMenu == "6.4":              # se activa la función clientes
             clientes()                      # se ejecuta la función clients


      elif opcionMenu == "6.5":              # Se activa la función compras de cada cliente
             compra_cliente()                # se ejecuta la  función compra de clientes

      elif opcionMenu == "6.7":    
            break      


   
   

