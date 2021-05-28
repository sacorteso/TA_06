# Advertencia:
# clave de usuario: gabrielawad
# clave global: jefe

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




os.system('clear')                    # Para limpiar pantalla
titulo = "  PÁGINA PRINCIPAL DE ADMINISTRADOR  " # Para crear titulo principal de la aplicación
print("\n\n")                                    # Salto de línea
print(titulo.center(70,"="))                     # Para imprimir el titulo centrado
today=dt.today()               # comando que muestra lafecha actual
f5=today.strftime('%Y%m%d')    # para cambiar el formato de fecha y unirlo
f55=int(f5)                    # para convertir la fecha en un entero para operaciones matemáticas
print(f55)                     # para imprimir la hora
#f56=time.strftime('%H:%M:%S') # para modificar el formato de la hora
#print=(f56)                   # para imprimir la hora modificada
print(today)                   # Para imprimir la fecha actual
print("\n\n")                  # Salto de línea

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


#informe 3

listacontras = []         # Se crea lista para manipular la creación de contraseñas

def creaciondecontrase(): # se crea función para la creación de contraseñas
    while True:           # ciclo while para comprobar las contraseñas
        # Para ingresar la nueva contraseña
        contrainic = input("\nIngrese nueva contraseña de 8 a 15 caracteres:") 
        longitud1 = len(contrainic)               # Para medir la longitud de la contraseña
        print("su contraseña tiene:", longitud1, "caracteres") # Se imprime la cantidad de caracteres de la contraseña
        if longitud1 > 7 and longitud1 < 16 :     # Se crea sistema para verificar  si cumple las condiciones para la clave    
          print("correcto")                       # Se imprime mensaje para confirmación de clave
          break                                   # Se finaliza el ciclo
        else:                                     # Otra opción si no se cumple la opción principal
           contrainic = input("Presione cualquier tecla para reintentar: ") # mensaje para regresar al ciclo de generación de clave
    contrainic2 = input("ingrese nuevamente su contraseña: ")               # Para ingresar nuevamente la clave
    while (contrainic != contrainic2):                                      # Se crea un ciclo while para verificar la clave
        contrainic2 = input("error ingrese nuevamente su contraseña: ")     # Mensaje de erroe cuando la clave no concuerda
    return str(contrainic)                                                  # Retorna la cale correcta
contrainic = ()                                                             # Regreso al ciclo de generación de claves

with open('CLAVES/Global.txt', 'r') as Ltexto:     # Se lee la base de datos de la clave global
  L = Ltexto.readline()                            # Se crea una variable con la clave global



def Global():                                      # Se crea función para crear la clave global                        
  while True:                                      # Se crea el ciclo para activar la función para  crear la clave global
    with open('CLAVES/Global.txt', 'r') as Ltexto: # Se lee la base de datos de clave global
         L = Ltexto.readline()                     # Se crea una variable con la clave global

    Ltexto.close()                                 # Se cierra la base de datos de clave global
      
    print("\n\nhola\n\n")                          # Menaje de saludo
   
    T = input("\nIngrese clave Global: ")          #solicitud de ingreso de clave global
    if L == T:                                     # Comparador de claves
      K=input("\nIngrese nueva clave: ")           # solicitud para nueva clave
      K1=input("\nIngrese nuevamente la nueva clave: ") # Solicitud de verificación para nueva clave
      if K == K1:                                  # compara que la nueva clave si la recuerda el usuario
        L = K1                                     # variable adicional
        Ltexto=open("CLAVES/Global.txt","w+")      # se activa la función para eliminar la clave vieja del archivo txt
        Ltexto.write(L)                            # se escribe la nueva clave global en el archivo txt
        Ltexto.close()                             # se cierra el archivo txt que guarda la clave global.
        break                                      # Se finaliza este ciclo
        print(" \n Clave Global modificada\n")     # anuncio que la clave global fue modificada
      else:                                        # Otra opción si no se cumple la opción principal
        break                                      # opción si no se ingresa la clave global correcta.
        print("\nregrese a menú e intentelo de nuevo\n")  # Se imprime mensaje para regresar al ciclo de creación de clave global


def login():                                       # Se crea función para ingreso de nuevos empleados
  while True:                                      # Se crea el ciclo para activar la función ingreso de nuevos empleados
      
      k= input("\nIngrese clave Global: ")         # ingresa clave global para permitir hacer actualizaciones
      nombre31=[]                                  # Se crea lista para nombre del empleado
      apellido31=[]                                # Se crea lista para el apellido del empleado
      usuario31=[]                                 # Se crea lista para usuario del empleado
      clave31=[]                                   # Se crfea lista para clave de usuario

         
      while(L==k):                                 # permite crear un cilclo para ingresar nuevos empleados
        for i in range(1):                         # Se crea un ciclo para ingrsar los datos del nuevo empleado
        
          nombre= input("\ningrese el nombre: ")     # para ingresar nombre del empleado
          apellido= input("\nIngrese el apellido: ") # para ingresar el apellido
          clave = creaciondecontrase()               # para ingresar una clave manual a gusto del empleado
          usuario= nombre[0:3]+apellido[0:3]         # permite creae el login de usuario
         
          #os.system('clear') # limpia la pantalla
          
          clave1=str(clave)                          # La clave se convirte en string 
          
          # confirma visualmente los datos ingrsados por el administrador
          print("\n",  "Su nombre es: ",   nombre, "\n")    # Se comprueba el nombre del nuevo empleado
          print("\n", "Su apellido es: ",  apellido, "\n")  # Se comprueba el apellido del nuevo empleado
          print("\n", "Su clave es: ",     clave, "\n")     # Se comprueba la clave del nuevo empleado
          print("\n", "Su Login es: ",     usuario,"\n")    # Se comprueba el usuario del nuevo empleado
          nombre31.append(nombre)                           # Se anexa el nombre del nuevo empleado a lista
          apellido31.append(apellido)                       # Se anexa el apellido del nuevo empleado a lista
          usuario31.append(usuario)                         # se anexa el usuario del nuevo empleado a lista
          clave31.append(clave1)                            # Se anexa la clave del nuevo empleado a lista


          emp=[nombre31, apellido31, usuario31,clave31]     # Se crea lista principal con las anteriores listas

          emp1=pd.DataFrame(emp)                            # Se crea DataFrame con los datos del nuevo empleado
          emp2=pd.DataFrame.transpose(emp1)                 # se transpone el DataFrame
          
          emp2.columns=["Nombre","Apellido","Usuario","Clave"] # Se agrega nombres a las columnas
          emp2.to_csv("BDATOS/empleado.csv", mode="a", index="", header="") # se graba la información en la base de datos de empleado
          #os.system('clear')                                                # Para limpiar la pantalla
          clave=pd.DataFrame(clave31)                                        # Se crea DataFrame para guardar la clave del nuevo empleado
          clave.to_csv("CLAVES/Clave.csv", mode="a", index="", header="")    # se graba la información en la base de datos de claves                                    
          return menu                                                        # Para regresar al menú principal
          
          
      
  
          

              
def empleados():                             # Se crea función para leer la base de datos de empleado
  while True:                                # Se crea el ciclo para activar la función para leer la base de datos de empleado
     os.system('clear')                      # Sirve para limpiar la pantalla
     print("\t\t\t\t BASE DE DATOS CON LOS EMPLEADOS \n\n")   # Se imprime el titulo de la página de empleado
     emp2= pd.read_csv('BDATOS/empleado.csv')      # se lee la base de datos de empleado
     print(emp2)                                    # Se imprime la base de datos de empleado
     break                                          # Se finaliza el ciclo

def EE():                                          # Se cea base de datos para eliminar fila 
  while True:                                      # Se crea el ciclo para eliminar fila
      
      k= input("\nIngrese clave Global: ")         # ingresa clave global para permitir hacer actualizaciones
      while(L==k):                                 # permite crear un cilclo para eliminar filas
        emp2= pd.read_csv('BDATOS/empleado.csv')   # se lee la base de datos de empleado
        print(emp2)                                # Imprime la base de datos de empleado
        CL= input("\n\nIngrese la clave del empleado: ") # Se solicita la clave del empleado a eliminar
        
        emp2=emp2.drop(emp2[emp2['Clave']==CL].index)    # Se crea un nuevo DataFrame para realizar las modificaciones en la base da datos de empleado
        emp2.to_csv("BDATOS/empleado.csv", mode="w", index="", header="True") # Se graba las modificcaiones en la base de datos de empleado
        print("\n\n empleado con clave:", CL, "Ha sido eliminado de la base de datos\n\n") # Se imprime mensaje de las modificaciones realizadas
        emp2= pd.read_csv('BDATOS/empleado.csv')         # se lee la base de datos de empleado        
        print("\n\n",emp2,"\n\n")                        # Se imprime la base de datos de empleado actualizada
        break                                            # Finaliza el ciclo de while
      break                                              #Finaliza el ciclo del while principal                                         
        


def fp():
  while True:
     print("fin del programa")
     input("\nSe ha pulsado la opción 9...\n pulsa enter para finalizar")
     break

# informe 4
def ingresoproductosbodega():  # Se crea función para ingresar los productos a la bodega
  while True:                  # ciclo while para ingresar los productos con sus respectivos datos

     ig=1                      # constante para validar variable
     #listas definidas para el dataframe de bodega
     distribuidor=[]           # para crear lista vacía para distribuidor
     producto=[]               # para crear lista vacía para producto
     referencia=[]             # para crear lista vacía para refernecia
     precio=[]                 # para crear lista vacía para precio   
     unidad=[]                 # para crear lista vacía para unidad
     valorxunidad=[]           # para crear lista vacía para valorxunidad
     fecompra=[]               # para crear lista vacía para fecha de compra

     for i in range(ig):       # ciclo for para ingressar los datos a las respectivas listas

      #ingreso de especificaciones de los productos
       distribuidor1=input("\ningrese el nombre del distribuidor: ") # se ingresa el nombre del distribuidor
       producto2= input("\ningrese el nombre del producto: ")        # se ingresa el nombre del producto
       refproducto2= input("\ningrese la referencia del producto: ") # se ingresa la referencia del producto
       precio2= input("\ningrese el precio de la paca: ")            # se ingresa el precio por paca del respectivo producto
       unidad2= input("\ningrese la cantidad de unidades de la paca: ")  # se ingresa la cantidad de unidades de la paca
       fecompra1= input("\ningrese la fecha de compra (formato: año mes dia sin espacios): ") # Se ingresa la fecha de la compra
       vxunidad = int (precio2)/int (unidad2)  # se hace la operación para halar el valor individual del producto.
     

      
#las variables que ingrese el usuario se agregaran a las listas

       distribuidor.append(distribuidor1) # sirve para anexar nuevos valores a la lista de distribuidor
       producto.append(producto2)         # sirve para anexar nuevos valores a la lista de producto
       referencia.append(refproducto2)    # sirve para anexar nuevos valores a la lista de referencia
       precio.append(precio2)             # sirve para anexar nuevos valores a la lista de precio
       unidad.append(unidad2)             # sirve para anexar nuevos valores a la lista de unidad
       fecompra.append(fecompra1)         # sirve para anexar nuevos valores a la lista de fecha de compra
       valorxunidad.append(vxunidad)      # sirve para anexar nuevos valores a la lista de valor x unidad


#las listas se convierten en datafreme
       bodega1=(distribuidor, producto, referencia, precio, unidad, valorxunidad,fecompra ) # se crea una nueva lista para que sea interpretada por el dataframe df1
       os.system('clear')                      # Sirve para limpiar la pantalla
       print("\t\t\t\t PÁGINA DE BODEGA \n\n") # para mostrae el titulo de la página bodega
       df1= pd.DataFrame(bodega1)              # se crea el dataframe Bodega para manipular operaciones con datos más facilmente.
       print("\t\t PRODUCTOS EN BODEGA \n\n")  # se crea el subtitulo de productos de bodega
       df2=pd.DataFrame.transpose(df1)         # se crea un nuevo dataframe para transponer los datos de df1, para una mejor visualización
       df2.columns=['distribuidor', 'producto','referencia', 'precio', 'unidad', 'valorxunidad', 'fecompra'] # Se anexan los titulos de las columnas del dataframe df2
       print(df2)                              # Se imprime los resultados del dataframe df2
       df2.to_csv('BDATOS/bodega1.csv', mode="a", index="", header="") # sirve para grabar los datos en la base de datos correspondiente
       print("\n\n\t\tTOTAL ACUMULADO EN COMPRAS\n\n")   # se imprime titulo de  submenú acumulados de compras
       L5=pd.read_csv('BDATOS/bodega1.csv')                     # lee la base datos de compras
       print(L5) 
     else:                                     # Se crea la segunda opción alternativa
       break                                   # fInaliza este ciclo con el for


# función para crear la pnatalla de compras e ingreso de productos
def compra():                                 # se define la función para compras
   while True:                                # se crea un ciclo white para el ingreso de los productos
   
     N=int(input("ingrese la cantidad total de productos comprados: ")) # sirve para ingresar el número de la opciones en el menú
     empresa=[]                               # se crea una lista vacía para ingresar el nombre de la empresa
     producto=[]                              # se crea una lista vacía para ingresar el nombre del producto
     precio=[]                                # se crea una lista vacía para ingresar el precio de la paca por producto
     unidad =[]                               # se crea una lista vacía para ingresar las unidades de la paca
     fcompra =[]                              # se crea una lista vacía para ingresar la fecha de la compra
     Fv =[]                                   # se crea una lista vacía para ingresar la feha de vencimiento


     for i in range(N):                       # se crea un ciclo for para ingrsar los datos de los productos que entran a la bodega
       empresa1 = input("\ningrese el nombre de la empresa: ") # se ingresa el nombre de la empresa
       producto1= input("\ningrese el nombre del producto: ")  # se ingresa el nombre del producto
       precio1= input("\ningrese el precio de la paca: ")      # se ingresa el precio del rpoducto por paca
       unidad1= input("\ningrese la cantidad de unidades de la paca: ")    # se ingresa la cantidad de unidades de la paca del respectivo producto
       fcompra1= input("\ningrese la fecha de compra: ")       # se ingresa la fecha de la compra
       Fv1= input("\ningrese la fecha de vencimiento: ")       # se ingresa la fecha del vencimiento del producto
       print("\n\n")                                           # se crean saltos de linea para mejor presentacón
       empresa.append(empresa1)  # sirve para anexar nuevos valores a la lista de distribuidor
       producto.append(producto1)# sirve para anexar nuevos valores a la lista de distribuidor
       unidad.append(unidad1)    # sirve para anexar nuevos valores a la lista de distribuidor
       precio.append(precio1)    # sirve para anexar nuevos valores a la lista de distribuidor
       unidad.append(unidad1)    # sirve para anexar nuevos valores a la lista de distribuidor
       fcompra.append(fcompra1)  # sirve para anexar nuevos valores a la lista de distribuidor
       Fv.append(Fv1)            # sirve para anexar nuevos valores a la lista de distribuidor 
       compras=(empresa, producto, precio, unidad, fcompra, Fv) # se crea una nueva lista para que sea interpretada por el dataframe df1
       os.system('clear')        # para limpiar la pantalla
       print("\t\t\t\t PÁGINA DE COMPRAS \n\n")    # imprime el titulo de la sección compras
       print("\t\t\t\t Productos comprados \n\n")  # imprime el titulo del submenú productos comprados
       df= pd.DataFrame(compras )                  # se crea dataframe para manipular más facilemnte los datos de compras
       df1=pd.DataFrame.transpose(df)              # se crea un nuevo dataframe para transponer los datos de df, para una mejor visualización
       df1.columns=['empresa', 'producto', 'precio',' unidad',' fcompra', 'Fv']
       print(df1)                                  # Se imprime los resultados del dataframe df1
       df1.to_csv('BDATOS/compras.csv', mode="a", index="", header="")   # sirve para grabar los datos en la base de datos correspondiente
     else:                                         # Se crea la segunda opción alternativa
        break                                      # fInaliza este ciclo con el for


# Función para manejar el total de productos adquiridos    
def total():                    # se crea una función para manejar los productos adquiridos
      while True:               # se crea un ciclos while para mostrar la actualización del total de los productos comprados
       print("\n\n\t\tTOTAL ACUMULADO EN COMPRAS\n\n")   # se imprime titulo de  submenú acumulados de compras
       L1=pd.read_csv('BDATOS/compras.csv')                     # lee la base datos de compras
       print(L1)                                         # imprime el dataframe de la base de datos de compras
       #with open("compras.csv", newline="") as file:
       #  reader=csv.reader(file,delimiter=",")
       #  for row in reader:
       #    print(row)
       print("\n\n")                                     # se crea saltos de linea
       break    
                                                # se finaliza este ciclo while

#informe 5
# Para cambiar el porcentaje de forma individual
def ganancia(): # Función para modificar el porcentaje de ganancia en las ventas de los productos.
  while True:   # Activa el ciclo para modificar el porcentaje de ganancia en las ventas de los productos.
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
    print("\n\n\n\n            Porcentaje de ganancia ingresado:",  mg1)        # Confirma que el porcentaje de ganancia ingresado es seleccionado


    float()           # se tranforma los datos a tipo float
    z1= 97            # Se crea una variable para operaciones matemáticas
    for TM in range(len(m2)):   # Se crea una iteración para revisar todas las referencias
     # ciclo para comparar con todas las claves con la base de datos
     #TM=m2.iloc[TM,5]
     #print(TM)                  # Permite hallar una clave  en una posición determinada
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
                                                     # otra opción en el ciclo
    break                                             # cierra el ciclo


#listo para funcionamiento
# Para cambiar las unidades de forma individual
def unidades():  # función para elegir la cantidad de productos para la venta según la referencia
  while True:    # Activar el ciclo para elegir la cantidad de productos para la venta según la referencia
    os.system('clear') # para limpiar la pantalla
    print("\n\nPAGINA MOSTRADOR") # Titulo para la página principal de mostrador
    print("\n\n\t\t PAGINA PARA CAMBIAR LAS UNIDADES EN FORMA INDIVIDUAL") # subtitulos para cambiar las unidades en forma individual
    print("\n\n\t\t Referencia en productos en Bodega\n\n")   # Subtitulos para referencia

    mm2=pd.read_csv("BDATOS/mostrador.csv")   # Se lee base de datos mostrador
    LL5=pd.read_csv('BDATOS/bodega1.csv')     # Se lee la base de datos de bodega
    print(LL5)                                # Se imprime la bese de datos de bodega

    print("\n\n\n\n Mostrador actual")        # Se imprime mensaje
    print("\n\n",mm2)                         # Se imprime los productos que están listos para la venta


    g2=input("\n\n\n\nIngrese la referencia del producto: ") # Se imprime mensaje para referencia de producto
    g3=str(g2)                                               # se crea una variable tipo string


    g4=input("\n\ningrese la fecha de compra del producto: ")   # Se ingresa la fecha de compra del producto
    g5=int(g4)                                                  # Se convirta la variable anterior en una variable tipo entero
    m5= LL5[LL5['Referencia']==g3]                              # Se buscan las referencias correspondientes en el DataFrame
    m6= LL5[LL5['Fcompra']==g5]                                 # Se buscan la fecha de compra en el DataFrame
    os.system('clear')                                          # Se limpia la pantalla
    print("\n\n\n\nDatos de la bodega \n\n", m5)                # Se imprime los resultados de las referencias encontradas

    # Se ingresa la cantidad de productos de una referencia determinada que van para el mostrador de ventas
    mu=input("\n\n\n\nIngrese la nueva cantidad de unidades del producto para mostrador: ")  
    mu1= int(mu)                                # El anterior valor se convierte en entero


    mt=0                                        # Se crea variable para guardar la cantidad de productos acumulados en mostrador                                                                
    for TM in range (len(mm2)):                 # Se crea un ciclos para recorrer el DataFrame mostrador
      if (LL5.iloc[TM,2]==g3 and LL5.iloc[TM,6]==g5):  # En la base de datos de bodega se busca la respectiva referencia  y fecha de compra del producto
        LL5=pd.read_csv('BDATOS/bodega1.csv')          # Al cumplir la condición anterior se lee nuevamente la base de datos de bodega
        mm2=pd.read_csv("BDATOS/mostrador.csv")        # Se lee la base de datos de mostrador

        mt= mm2.iloc[TM, 7]                            # Se escoge el valor del acumulado en el mostrador y se crea una nueva variable
        g6= LL5.iloc[TM, 4]                            # Se escoge la cantidad de unidades disponibles en la bodega 
        mm2.iloc[TM, 4]=mu1                            # Se actualiza la cantidad  de unidades en el mostrador
        mt=mu1+mt                                      # Se suma la nueva cantidad de unidades al acumulado
        mm2.iloc[TM, 7]=mt                             # Se actualiza el acumulado en la base de datos de mostrador
        mm2.to_csv('BDATOS/mostrador.cvs', mode="w", index="", header="True") # Se graba las nuevas modificaciones en la base de datos mostrador
        g7=g6-mu1                                      # Las unidades que se llevan para el mostrador se descuentas al inventario de la bodega
        LL5.iloc[TM, 4]=g7                             # Se actualiza las nuevas cantidades de unidades del producto en la bodega
        mm2.iloc[TM, 2]=g7                             # La unidaes del productos actualizadas en la bodega se informa en la base de datos de mostrador
        mm2.to_csv('BDATOS/mostrador.csv',mode="w", index="", header="True") # Se graba las nuevas actualizaciones en la base de datos de mostrador
        LL5.to_csv('BDATOS/bodega1.csv', mode="w", index="", header="True")  # Se graba las nuevas actualizaciones en la base decdatos de bodega
        LL5=pd.read_csv('BDATOS/bodega1.csv')          # Se lee la base de datos de bodega para confirmar los cambios
        mm2=pd.read_csv('BDATOS/mostrador.csv')        # Se lee la base de datos de mostardor para confirmar los cambios
        


    print("\n\n\n\n***************   Bodega actualizada    *******************") # Mensaje de confirmación de datos actualizados en bodega
    print("\n\n\n\n", LL5)
    print("\n\n\n\n***************   Mostrador actualizado   ****************")  # Mensaje de confirmación de datos de actualizados en mostrador
    print("\n\n",mm2)
    break

def agotado():  # Se crea función para controlar el agotamiento de productos en la bodega
  while True:   # Se activa función para controlar el agotamiento de productos en la bodega
    os.system('clear')  # para limpiar pantalla 
    print("\n\n*******************************************************************************************************") # Decoración de titulo de pantalla
    print("\n\n******************************        ALERTA DE PRODUCTO AGOTADO         ******************************") # Titulo de alerta de producto agotado
    print("\n\n*******************************************************************************************************") # Decoración de titulo de pantalla
    L5=pd.read_csv('BDATOS/bodega1.csv')   # Se lee la base de datos de bodega
    for i in range(len(L5)):               # Se crea un ciclo para recorrer la base de datos bodega
       if(L5.iloc[i,4]==0):                # Se activa el ciclo con la condición que la cantidad de los productos están agotados

         #print("\n\nProducto con nombre: ", L5.iloc[i,1], " y referencia: ",L5.iloc[i,2],"       con fecha de compra: ",L5.iloc[i,6] )
         #print("\n\n")
         #print("\n\n                                                                             Está agotado")
         print("\nProducto con nombre: ", L5.iloc[i,1])  # Se muestra el nombre del producto que está agotado
         print("\n         referencia: ", L5.iloc[i,2])  # Se muestra la referencia del producto que está agotado
         print("\ncon fecha de compra: ", L5.iloc[i,6])  # Se muestra la fecha de compra del producto que está agotado
         print("\n\n                                   Está agotado")  # Mensaje que confirma que está agotado
         print("\n\n------------------------------------------------------------------------------------------------")  # Decoración de pantalla para la sección
         
         
    break    # Finalización de este ciclo



  while True: # Se activa función para controlar el agotamiento de productos en la bodega
    print("\n\n*******************************************************************************************************") # Decoración de titulo de pantalla
    print("\n\n*******************************************************************************************************") # Decoración de titulo de pantalla
    print("\n\n************************      ALERTA DE PRODUCTO CERCANO A AGOTARSE    ********************************") # Titulo de alerta de producto cercano a agotarse
    print("\n\n*******************************************************************************************************") # Decoración de titulo de pantalla
    L5=pd.read_csv('BDATOS/bodega1.csv')   # Se lee la base de datos de bodega 
    for i in range(len(L5)):               # Se crea un ciclo para recorrer la base de datos bodega
        if(L5.iloc[i,4]==2):               # Se activa el ciclo con la condición que la cantidad de los productos están agotados
          #print("\n\nProducto con nombre: ", L5.iloc[i,1], " y referencia: ",L5.iloc[i,2],"       con fecha de compra: ",L5.iloc[i,6] )
          #print("\n\n                                                                                      Está cercano a agotarse  ")
          print("\nProducto con nombre: ", L5.iloc[i,1]) # Se muestra el nombre del producto que está cercano a agotarse
          print("\n         referencia: ", L5.iloc[i,2]) # Se muestra la referencia del producto que está cercano a agotarse
          print("\ncon fecha de compra: ", L5.iloc[i,6]) # Se muestra la fecha de compra del producto que está cercano a agotarse
          print("\n\n                                    Está cercano a agotarse") # Mensaje que confirma que está cercano a agotarse
          print("\n\n-------------------------------------------------------------------------------------------------") # Decoración de pantalla para la sección
                                                                                     
    break   # Finalización de este ciclo

def vencimiento():   # Función para avisar cuando hay un producto cercano para vencerse  o  vencido
  while True:        # Activa el ciclo para avisar cuando hay un producto cercano para vencerse  o  vencido
    os.system('clear')  # para limpiar pantalla    
    today=dt.today() # Muestra la fecha actual
    #print(today)
    f5=today.strftime('%Y%m%d') # Cambia el foramato de la fecha
    f55=int(f5)                 # Convierte el nuevo formato de fecha en entero
    #print(f55)
    f25=today-timedelta(15)     # A la fecha actual se restan 15 días
    f255=f25.strftime('%Y%m%d') # A la nueva fecha se le cambia formato
    f257=int(f255)              # A la anterior fecha se convierte en entero
    
    
    print("\n\n*****************************************************************************************************") # Decoración de titulo de pantalla
    print("*************************       ALERTA DE PRODUCTO VENCIDO     ******************************************") # Titulo de alerta de producto vencido
    print("*********************************************************************************************************") # Decoración de titulo de pantalla
    L5=pd.read_csv('BDATOS/bodega1.csv')   # Se lee la base de datos bodega
    
    for i in range(len(L5)):               # Se crea un ciclo para recorrer la base de datos bodega
      if(L5.iloc[i,7]<=f55):               # Se activa el ciclo con la condición de la fecha de vencimiento del producto es igual o mayor a la fecha actual
        #print("\n\nProducto con nombre: ", L5.iloc[i,1], " y referencia: ",L5.iloc[i,2],"       con fecha de compra: ",L5.iloc[i,6] )
        print("\n\n")                      # Salto de línea
        print("\nProducto con nombre: ", L5.iloc[i,1])     # Se muestra el nombre del producto que está vencido
        print("\n         referencia: ", L5.iloc[i,2])     # Se muestra la referencia del producto que está vencido
        print("\ncon fecha de compra: ", L5.iloc[i,6])     # Se muestra la fecha de compra del producto que está vencido
        print("\n\n                                   Está vencido - reemplazar")  # Mensaje que confirma que está vencido
        print("\n\n--------------------------------------------------------------------------------------------------")   # Decoración de pantalla para la sección                                                                   
    print("\n\n******************************************************************************************************")   # Decoración de pantalla para la sección
    print("\n\n**************************       ALERTA DE PRODUCTO CERCANO A VENCERSE   *****************************")   # Titulo de alerta de producto cercano a vencerse
    print("\n\n******************************************************************************************************")   # Decoración de titulo de pantalla
    L5=pd.read_csv('BDATOS/bodega1.csv')    # Se lee la base de datos bodega
    
    
    L57=pd.DataFrame(L5['Fv'])              # Se crea un nuevo DataFRame solamnete con las fechas de vencimientos de los productos
    #print(L57)

    L57['Fv']= pd.to_datetime(L57['Fv'], format="%Y%m%d") # Utilidad de pandas para manipular formatos de fechas y se crea una nuevo DataFrame
    #print(L57)
    
    for kkk in range(1):       # Se crea un ciclo para recorrer el anterior DataFrame
      L9=L57.iloc[kkk:,0]      # Se selecciona una fecha especifica
      T4=L9-timedelta(15)      # A la antrior fecha se resta 15 días
      LL9=pd.DataFrame(T4)     # Con el anterior resultado se crea un nuevo DataFrame
      LL9.columns=['Fv1']      # SE le coloca el titulo a la columna de los datos
     


    for k9 in range(len(L57)):  # Se crea un ciclo para recorrer DataFrame con formato de fecha modificado
      if(LL9.iloc[k9,0]<=today and today<L57.iloc[k9,0]):  # Se activa el ciclo con la condición que la fecha de vencimineto con 15 días de annticipación es menor que el día  actual
                                                           # y el día actual es menor a la fecha de vencimiento del producto.
       # TT=L5.iloc[k9,2]                                  
        
        #print("\n\nProducto con nombre: ", L5.iloc[k9,1], " y referencia: ",L5.iloc[k9,2],"       con fecha de compra: ",L5.iloc[k9,6] )
        print("\n\n")                                      # Salto de linea
        print("\nProducto con nombre: ", L5.iloc[k9,1])    # Se muestra el nombre del producto que está vencido
        print("\n         referencia: ", L5.iloc[k9,2])    # Se muestra la referencia del producto que está vencido
        print("\ncon fecha de compra: ", L5.iloc[k9,6])    # Se muestra la fecha de compra del producto que está vencido
        print("\n\n                                   Está cercano a vencerse - tener cuidado")  # Mensaje que confirma que está cercano a vencerse - tener cuidado
        print("\n\n--------------------------------------------------------------------------------------------------")  # Decoración de titulo de pantalla
        
        #print("\n\n                                                                             Está cercano a vencerse - tener cuidado")
        print("\n\n")  # Salto de línea 
    break              # Finalización del ciclo de esta sección


#informe 6


today=dt.today()            # comando que muestra la fecha actual
f5=today.strftime('%Y%m%d') # para cambiar el formato de fecha y unirlo
f55=int(f5)                 # para convertir la fecha en un entero para operciones matemáticas
print(f55)                  # para imprimir la hora
f56=time.strftime('%H:%M:%S') # pra modificar el foramto de la hora
print(f56)                    # para imprimir la hora
ce=0
ff7=0
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
    
    z1= input("\n\ningrese la cantidad de referencias para la venta que se va a realizar: ") # para crear un ciclo en donde se estima la cantidad de productos que hay que registrar
    z=int(z1)                  # Se convierte el valor del ciclo en un entero
    zz1=0                      # para generar variable para el nombre
    zz2=0                      # para generar variable para el precio individual del producto
    subtotal=[]                # para geneerar variables del valor subtotal ed la venta


    for k in range(z):  # se crea una iteración para registrar las los productos que se van a vender.
      L6 =pd.read_csv("BDATOS/mostrador.csv") # SE lee la base de datos mostrador
      print("\n\n",L6.iloc[:,0:2])    # se imprime el nombre y a referencia del producto
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
          
          cedula=pd.DataFrame(ce)
          
          cedula.to_csv("BDATOS/cedula.csv",mode="w", index="", header="True",columns=['cedula'])

         
          factura=(ce,c1,c2,c3,c4,c5,c6,c7) # se crea lista con los valores de las respectivas variables
          factura1=pd.DataFrame(factura)    # Se crea DataFrame para la factura
          factura2=pd.DataFrame.transpose(factura1) # Se transpone el Dataframe factura
      
         # Se coloca los nombres a las columnas
          factura2.columns=['Cedula','Referencia','Nproducto','Punitario','Cantidad','Subtotal','Fecha','Hora']
      
          temporal=pd.DataFrame.transpose(factura1)  # Se crea el DataFrame temporal que va permitir crear la factura
      
         # Se coloca los nombres a las columnas
          temporal.columns=['Cedula','Referencia','Nproducto','Punitario','Cantidad','Subtotal','Fecha','Hora']
      
         # Se graban los datos para la factura en la base de datos temporal
          temporal.to_csv('BDATOS/temporal.csv', mode="a", index="", header="True")
      
         # Se graban los datos para la factura en la base de datos factura para consultas en el futuro
          factura2.to_csv('BDATOS/factura.csv', mode="a", index="", header="True")
     
         # Para actualizar las unidades en el mostrador
          mm2=pd.read_csv("BDATOS/mostrador.csv")
      
         # Nueva cantidad de unidades del producto para mostrador
          mu1= can                     # Se elige la cantidad de unidades para descontar en mostrador
          mt=0                         # variable para operaciones matemáticas
          for TM in range(len(mm2)):   # se crea un ciclo para recorrer toda la base de mostrador
            if (mm2.iloc[TM, 1]==Ref1):# Se crea un filtro para eliger la referencia correcta
                   
               mm2=pd.read_csv("BDATOS/mostrador.csv") # Se lee la base de datos de mostardor
               #print("\n\n",mm2)                              # Se imprime la base de datos de mostardor antes de descontar las unidades del producto
               mt= mm2.iloc[TM, 7]                     # Se selecciona el acumulado disponible del producto ubicado en el mostrador
          
               mt=mt-mu1                               # se descuenta las respectivas unidades del producto
               mm2.iloc[TM, 7]=mt                      # se actualiza el acumulado con el nueva cantidad de productos
               mm2.to_csv('BDATOS/mostrador.csv', mode="w", index="", header="True") # se graba los nuevos datos en la base de datos de mostrador
                                   
               mm2=pd.read_csv("BDATOS/mostrador.csv") # se lee la base de datos de mostardor con los nuevos datos
               #print("\n\n\n\n")                       # salto de línea
               print("\n\n",mm2)                              # Se imprime la nueva base de datos mostrador
  
    z1=0                                               # Constante para operaciones
    for TK in range(z):                                # Ciclo para recorrer la base de datosde temporal con las últimas ventas
      temp=pd.read_csv("BDATOS/temporal.csv")          # Se lee la base de datos de temporal
      long=len(temp)                                   # Se halla la cantidad de filas en la base de datos temporal
      #print(long)                                     # Se imprime la cantidad de filas
      z1=long-TK-1                                     # Se crea una variable para hallar la posición de la fila 
      temp1=temp.iloc[z1,:]                            # Se extraen los datos de la fila en la posición determinada anteriormente
      temp2=pd.DataFrame(temp1)                        # Se crea un nuevo DataFrame con los datos anteriores
      temp22=pd.DataFrame.transpose(temp2)             # Se transpone el DataFrame
      print("\n\n)")                                   # Salto de linea
      print(temp22)                                    # Se imprime el Dataframe modificado
      # Se agrega titulos a las columnas
      temp22.columns=['Cedula','Referencia','Nproducto','Punitario','Cantidad','Subtotal','Fecha','Hora']
      temp22.to_csv('BDATOS/temporal2.csv', mode="a", index="", header="")   # SE gaba las modifificaciones en la base de datos Temporal2

    
    break                                              # finalización del ciclo de esta función


 
    
                   




   
    



def Factura():
  while True:
    temporal22=pd.read_csv('BDATOS/temporal2.csv')  # Para leer la base de datos temporal
    #factura22=pd.read_csv('BDATOS/factura.csv')   # Para leer la base de datos de factura
    Vtotal=temporal22['Subtotal'].sum()  # para sumar el valor total de la compra de productos
    tem=temporal22.drop(['Fecha','Hora'], axis=1) # Para eliminar columnas de la fecha y hora
                                  # variable para la identificcaión del cliente
                              # variable para el valor total de la compra
    ce=pd.read_csv("BDATOS/cedula.csv")
    ce1=ce['cedula']
    ventas=[ce1,Vtotal,f55,f56]                # Se crea lista para ventas totales
    #ventas1=pd.DataFrame(ventas)               # Se crea dataframe para ventas totales
    #ventas2=pd.DataFrame.transpose(ventas1)    # se transpone el dataframe para organizar los datos
    #print(ventas2)
    #ventas2.columns=['Cedula','Vtotal','Fecha','Hora'] # se coloca nombres a las columnas
    #ventas2.to_csv('BDATOS/ventas.csv', mode="a", index="", header="") # Se graba los datos para ventas totales en el archivo ventas.csv
    #ventas2= pd.read_csv('BDATOS/ventas.csv')
    #cont=pd.read_csv('BDATOS/contador.csv')
    #cont1=cont.iloc[0:0]
    #cont2=cont1+1
    #cont2.to_csv('BDATOS/contador.csv', mode="w", index="", header="") 
    #os.system('clear')                         # para limpiar la pantalla
    
    cont=pd.read_csv("BDATOS/contador.csv")    # Se lee la base  de datos contador
    cont1=pd.to_numeric(cont['contador'])                     # Se halla el valor del contador de la factura
    cont1= cont1+1                             # se incrementa el contador
    c5=[cont1]                                 # Se crea una lista
    cont2=pd.DataFrame(c5)                     # Se crea un nuevo DataFrame
    cont22=pd.DataFrame.transpose(cont2)       # Se transpone el DataFrame
    cont22.columns=['contador']                # Se coloca titulo a las columnas del DataFrame
    cont22.to_csv("BDATOS/contador.csv",mode="w", index="", header="True") # Se graba las modificaciones en la base de datos de contador
    
    os.system('clear')                        # para limpiar pantalla  
    print("\n\n\n\n\t\t\t\t\t                  FACTURA DE VENTA") # titulo de la página factura de venta
    print("\n\n\n\n")                          #salto de linea                    
    print("Cédula: ",ce1, "\t\tFecha: " ,       f55,   "\t\tHora: ",        f56, "\t\tFactura nro.: ", cont1) # para insertar cédula, fecha , hora
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


            
# informe 7
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


#informe 8
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
        

os.system('clear')     # Para limpiar la pantalla
print("\n\n*********************************************************************************************************")   # Decoración de titulo de pantalla
print("\n\t\t\t\t                          PÁGINA PRINCIPAL DE MOSTRADOR ")                                              # se imprime el titulo de la página del menu del manejo operativo del negocio
print("\n\n*********************************************************************************************************")   # Decoración de titulo de pantalla
today=dt.today()      # Selecciona la fecha actual
print(today)          # imprime la fecha actual


def menu(): 
  #os.system('clear') #limpiar pantalla
  print("\n\n")
  tituloG = "PÁGINA PRINCIPAL DE ADMINISTRADOR"
  print(tituloG.center(100," "))
  #print("\n\n")
                                           # se crea un menu para el manejo operativo del negocio
    
  print("\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
  print("                                  \t3 - Empleados ")                  # se imprime registro de compras
  print("                                  \t4 - Compras y Bodega")              # se imprime registro total acumulado
  print("                                  \t5 - Mostrador")  
  print("                                  \t6 - Ventas y Clientes") 
  print("                                  \t7 - Contabilidad") 
  print("                                  \t8 - Reportes") 
  print("                                  \t9 - Terminar con uso de menu")              # se imprime finalizacón de menú
          
# Se crea un una iteración con while mientras se cumpla la condición
while True: 
  menu()                                             # se activa la función menú
  opcionMenu = input("\n Inserte el número de la opción del menú: ")   # sirve para ingresar el valor de la opción seleccionada
  if opcionMenu == "3": 
    #os.system('clear') #limpiar pantalla
    print("\n\n") 
        
    subtitulo = " SUBMENÚ DE EMPLEADOS"
    print("\n\n")
    print(subtitulo.center(100," "))
    print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
    print("                                  \t3.1 - Cambio de clave Global ")                  # se imprime registro de compras
    print("                                  \t3.2 - Login y clave para nuevo empleado")              # se imprime registro total acumulado
    print("                                  \t3.3 - Base de datos de empleados")  
    print("                                  \t3.4 - Eliminar datos de empleado ") 
    print("                                  \t3.5 - terminar con uso de submenú") 
  
    opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
    if opcionmenu== "3.1":
      print("\n\nhola\n\n")                          # imprime mensaje de saludo
      #bodegacom()   
      #mensaje="HOLA"
      #os.system('clear') #limpiar pantalla
      print("\n\n")
      print("3.1".center(100," "))                                  # la función compra se ejecuta
      Global()   

       
    elif opcionmenu == "3.2":                            # se ejecuta la función total
         login() 

    elif opcionmenu == "3.3":                            # se activa la función bodega
             print("3.3")
             empleados()
            
    elif opcionmenu == "3.4":                            # se activa la función bodega
              EE()
              
              

    elif opcionmenu == "3.5":                            # se activa la función bodega
             print("3.5")
             fp()
           
           

#os.system('clear')                                       # sirve para limpiar la pantalla
#print("\t\t\t\t PÁGINA PRINCIPAL \n\n")                  # se imprime el titulo de la página del menu del manejo operativo del negocio

  if opcionMenu == "4": 

     os.system('clear') #limpiar pantalla
     print("\n\n") 
        
     subtitulo = " SUBMENÚ DE COMPRAS Y BODEGA"
     print("\n\n")
     print(subtitulo.center(100," "))
     print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
     print("                                  \t4.1 - Registro de compras")                  # se imprime registro de compras
     print("                                  \t4.2 - Registro total acumulado")              # se imprime registro total acumulado
     print("                                  \t4.3 - Ingreso de bodega")  
     print("                                  \t4.4 - Terminar con uso de suubmenú") 
          
     opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
     if opcionmenu== "4.1": 
       print("\n\nhola\n\n")                          # imprime mensaje de saludo
       #bodegacom()   
       #mensaje="HOLA"
       os.system('clear') #limpiar pantalla
       print("\n\n")
       print("Hola".center(100," "))                                  # la función compra se ejecuta
       ingresoproductosbodega() 
       
        
     elif opcionmenu == "4.2":                                # se ejecuta la función total
           compra()

     elif opcionmenu == "4.3":
         print("4.3")
         total()
         
        
     elif opcionmenu == "4.4": 
        print("4.4")
        break   

     
         
             
  if opcionMenu == "5": 
    os.system('clear') #limpiar pantalla
    print("\n\n") 
        
    subtitulo = " SUBMENÚ DE MOSTRADOR"
    print("\n\n")
    print(subtitulo.center(100," "))
    print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
    print("                                  \t5.1 - Cambio de porcentaje de ganancia ")                  # se imprime registro de compras
    print("                                  \t5.2 - Para llenar el mostrador con productos")              # se imprime registro total acumulado
    print("                                  \t5.3 - Vencimiento de productos")  
    print("                                  \t5.4 - Agotamiento de productos") 
    print("                                  \t5.5 - Terminar con uso de menu") 
    opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
    if opcionmenu== "5.1":
      print("\n\nhola\n\n")                          # imprime mensaje de saludo
      #bodegacom()   
      #mensaje="HOLA"
      os.system('clear') #limpiar pantalla
      print("\n\n")
      print("Hola".center(100," "))                                  # la función compra se ejecuta
      ganancia()   

        
    elif opcionmenu == "5.2":                            # se ejecuta la función total
          unidades()  

    elif opcionmenu == "5.3": 
      print("5.3")
      agotado()
        
    elif opcionmenu == "5.4":   
       print("5.4")
       vencimiento()
             

    elif opcionmenu == "5.5":
      print("5.5")
      break
              

    
             
  if opcionMenu == "6": 
    os.system('clear') #limpiar pantalla
    print("\n\n") 
        
    subtitulo = " SUBMENÚ DE VENTAS Y CLIENTES"
    print("\n\n")
    print(subtitulo.center(100," "))
    print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
    print("                                  \t6.1 - Para generar venta")                  # se imprime registro de compras
    print("                                  \t6.2 - Factura")              # se imprime registro total acumulado
    print("                                  \t6.3 - Venta acumulada")  
    print("                                  \t6.4 - Página de clientes") 
    print("                                  \t6.5 - Página de Compras de cada cliente") 
    print("                                  \t6.6 - ") 
    print("                                  \t6.7 - Otras opciones")
    print("                                  \t9   - ")              # se imprime finalizacón de menú
          
    opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
    if opcionmenu== "6.1": 
      print("\n\nhola\n\n")                          # imprime mensaje de saludo
      #bodegacom()   
      #mensaje="HOLA"
      os.system('clear') #limpiar pantalla
      #print("\n\n")
      #print("Hola".center(100," "))                                  # la función compra se ejecuta
      venta()           

        
    elif opcionmenu == "6.2":             # se ejecuta la función total
           Factura()  

    elif opcionmenu == "6.3":
      print("6.3")
      Venta_acum()
      
        
    elif opcionmenu == "6.4": 
      print("6.4")
      clientes()
             

    elif opcionmenu == "6.5":
      print("6.5")
      compra_cliente()
              


    elif opcionmenu == "6.6":  
      print("6.6")
             

    elif opcionmenu == "6.7": 
      print("6.7")  
      break
              

                                         
  if opcionMenu == "7": 
   os.system('clear') #limpiar pantalla
   print("\n\n") 
        
   subtitulo = " SUBMENÚ DE CONTABILIDAD"
   print("\n\n")
   print(subtitulo.center(100," "))
   print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
   print("                                  \t7.1 - Costos de Bodega completa ")                  # se imprime registro de compras
   print("                                  \t7.2 - Costos de bodega por fechas")              # se imprime registro total acumulado
   print("                                  \t7.3 - Ingreso de datos para costos fijos")  
   print("                                  \t7.4 - Costos fijos completos") 
   print("                                  \t7.5 - Costos fijos por fecha") 
   print("                                  \t7.6 - Ingresos por ventas - completa") 
   print("                                  \t7.7 - Ingresos por ventas - manejo por fechas")
   print("                                  \t7.8 - CONTABILIDAD")
   print("                                  \t9   - Terminar con uso de menu")              # se imprime finalizacón de menú
          
   opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
   if opcionmenu== "7.1": 
     print("\n\nhola\n\n")                          # imprime mensaje de saludo
     os.system('clear') #limpiar pantalla
     print("\n\n")
     print("Hola".center(100," "))                                  # la función compra se ejecuta
     bodegafecha()           

        
   elif opcionmenu == "7.2":                # se ejecuta la función total
        ingcostosf()      

   elif opcionmenu == "7.3": 
      print("7.3")
      costosf()

        
   elif opcionmenu == "7.4": 
      print("7.4")
      costosff()
             

   elif opcionmenu == "7.5": 
     print("7.5")
     ingventasT()
              


   elif opcionmenu == "7.6":
      print("7.6")
      ingventasTF()
             

   elif opcionmenu == "7.7": 
     print("7.7") 
     contabilidad() 
              

   elif opcionmenu == "7.9":
      print("7.9") 
      break
      
             
  if opcionMenu == "8": 
    os.system('clear') #limpiar pantalla
    print("\n\n") 
        
    subtitulo = " SUBMENÚ DE REPORTES"
    print("\n\n")
    print(subtitulo.center(100," "))
    print("\n\n\n\nSelecciona una opción \n")                    # se imprime mendsaje del menú
    print("                                  \t8.1 - Ingreso de proveedores")                  # se imprime registro de compras
    print("                                  \t8.2 - Base de datos de proveedores")              # se imprime registro total acumulado
    print("                                  \t8.3 - Informe del valor de productos por paca")  
    print("                                  \t8.4 - Informe del valor de las ventas diarias") 
    print("                                  \t8.5 - Informe total de unidades en bodega") 
    print("                                  \t8.6 - Informe total de contabilidad") 
    print("                                  \t9   - Finalizar submenú")              # se imprime finalizacón de menú
    opcionmenu = input("\n\n Inserte el número de la opción del submenú: ")
    if opcionmenu== "8.1": 
      print("\n\nhola\n\n")                          # imprime mensaje de saludo
      #bodegacom()   
      #mensaje="HOLA"
      os.system('clear') #limpiar pantalla
      print("\n\n")
      print("Hola".center(100," ")) 
      proveedor()                                  # la función compra se ejecuta
             

        
    elif opcionmenu == "8.2":                           # se ejecuta la función total
           Bproveedores()    

    elif opcionmenu == "8.3": 
           PRpaca()
        
        
    elif opcionmenu == "8.4":
          Ifventas()
        
             

    elif opcionmenu == "8.5":  
         Ubodega()  
              


    elif opcionmenu == "8.6": 
         infcontabilidad()  
         
             
         
          
  elif opcionMenu == "9": 
   
   print("\n\n")
   subtitulof = "Sistema finalizado"
   print(subtitulof.center(100," ")) 
   print("\n\n\t\tSistema finalizado")
   break 
    
