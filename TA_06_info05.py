#Advertencia
# En la opción 5.1 en ingrese la referencia del producto utilizar c500ml
#    en ingrese el nuevo porcentaje de ganancia del producto utilizar 35 

# En la opción 5.2 en ingrese la referencia del producto utilizar CL1000
#     en ingrese la fecha de compra del producto utilizar 20210428
#     ingrese la nueva cantidades de unidades del producto para mostrador
#     utilizar 5 o máximo las unidades que muestra los datos de la bodega

# librerías para manejar base de datos
from datetime import date as dt       # Librería para manejar fechas
from datetime import datetime as dtt  # Librería para manejar el tiempo
from datetime import timedelta        # Librería para realizar operaciones matemáticas con el tiempo
import pandas as pd # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os           # Librerías para realizar funciones internas del software
import csv          # Librería para manipular archivos excel y con extensión .csv 
from tabulate import tabulate   # Librería pararealizar tabulaciones al imprimir los resultados

# listo para funcionamiento
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
    print("\n")  # Salto de línea
    titulo = ("  PAGINA MOSTRADOR ") # Titulo para cambiar el porcentaje de ganancia del producto
    print(titulo.center(70, "="))  # Para imprimir el titulo centrado
    print("\n")  # Salto de línea
    
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
    
    m5= LL5[LL5['Referencia']==g3 ]                             # Se buscan las referencias correspondientes en la base de datos de bodega
    m6= LL5[LL5['Fcompra']==g5   ]                              # Se buscan las referencias correspondientes en la base de datos de bodega              

    
    os.system('clear')                                          # Se limpia la pantalla
    print("\n\n\n\nDatos de la bodega \n\n", m5)                # Se imprime los resultados de las referencias encontradas
    
    

    TM = mm2[mm2["Referencia"]==g3].index                       # Para hallar la posición de la fila del producto en el DataFrame de mostrador
    TMM= input("\n\ningrese el número de fila del producto con la referencia y fecha especifica: ") # Para ingresar la posición de la fila del producto del DataFrame bodega
    TMM1= int(TMM)                                              # Se convierte la variable en un entero
    # Se ingresa la cantidad de productos de una referencia determinada que van para el mostrador de ventas
    mu= input("\n\nIngrese la nueva cantidad de unidades del producto para mostrador: ")  
    mu1= int(mu)                                   # El anterior valor se convierte en entero
    
    
    mt=0                                           # Se crea variable para guardar la cantidad de productos acumulados en mostrador                                                                
   
  
    mt= mm2.iloc[TM, 7]                            # Se escoge el valor del acumulado en el mostrador y se crea una nueva variable
    g6= LL5.iloc[TMM1, 4]                          # Se escoge la cantidad de unidades disponibles en la bodega 
    mm2.iloc[TM, 4]= mu1                           # Se actualiza la cantidad  de unidades en el mostrador
    mt=mu1+mt                                      # Se suma la nueva cantidad de unidades al acumulado
    mm2.iloc[TM, 7]= mt                            # Se actualiza el acumulado en la base de datos de mostrador
    mm2.to_csv('BDATOS/mostrador.csv', mode="w", index="", header="True") # Se graba las nuevas modificaciones en la base de datos mostrador
    g7=g6-mu1                                      # Las unidades que se llevan para el mostrador se descuentas al inventario de la bodega
    LL5.iloc[TMM1, 4]= g7                          # Se actualiza las nuevas cantidades de unidades del producto en la bodega
    LL5.to_csv('BDATOS/bodega1.csv', mode="w", index="", header="True")  # Se graba las nuevas actualizaciones en la base decdatos de bodega
    mm2.iloc[TM, 2]= g7                            # La unidaes del productos actualizadas en la bodega se informa en la base de datos de mostrador
    mm2.to_csv('BDATOS/mostrador.csv',mode="w", index="", header="True") # Se graba las nuevas actualizaciones en la base de datos de mostrador
    LL5=pd.read_csv('BDATOS/bodega1.csv')          # Se lee la base de datos de bodega para confirmar los cambios
    mm2=pd.read_csv('BDATOS/mostrador.csv')        # Se lee la base de datos de mostardor para confirmar los cambios
        


    print("\n\n\n\n***************   Bodega actualizada    *******************") # Mensaje de confirmación de datos actualizados en bodega
    print("\n\n\n\n", LL5)                                                       # Se muestra la base datos de bodega
    print("\n\n\n\n***************   Mostrador actualizado   ****************")  # Mensaje de confirmación de datos de actualizados en mostrador
    print("\n\n",mm2)                                                            # Se muestra la base e datos de mostrador
    ff=5                                      # Se crea variable para finalizar ciclo de la opción
    T= str(input("\n\nescriba ff para finalizar esta opción: ")) # Mensaje de confirmación para finalizar ciclo de la opción manual de usuario 
    if(T==ff):                                # Se verifica si cumple la condición
      break                                   # Finaliza primer ciclo
    break                                     # Finaliza segundo ciclo
 
                                 

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


os.system('clear')     # Para limpiar la pantalla
print("\n\n*********************************************************************************************************")   # Decoración de titulo de pantalla
print("\n\t\t\t\t                          PÁGINA PRINCIPAL DE MOSTRADOR ")                                              # se imprime el titulo de la página del menu del manejo operativo del negocio
print("\n\n*********************************************************************************************************")   # Decoración de titulo de pantalla
today=dt.today()      # Selecciona la fecha actual
print(today)          # imprime la fecha actual
# función para activar el menu de entrada de la página mostrador
def menu():           # se crea un menu para el manejo operativo del negocio
    
    print("          \n\n\n\nSelecciona una opción \n")    # se imprime mensaje del menú para elegir una opción
    print("                  \t5.1 - Cambio de porcentaje de ganancia ")        # se imprime cambio de porcentaje de ganacia
    print("                  \t5.2 - Para llenar el mostrador con productos")   # se imprime para llenar el mostrador con productos
    print("                  \t5.3 - Vencimiento de productos")                 # se imprime vencimiento de productos
    print("                  \t5.4 - Agotamiento de productos")                # se imprime agotamiento de productos
    print("                  \t9   - Terminar con uso de menu")                   # se imprime finalizacón de menú
          
# Se crea un una iteración con while mientras se cumpla la condición
while True:                                              # se activa el ciclo while para activar el menú
      menu()                                             # se activa la función menú
      opcionMenu = input("\n Inserte el número de la opción: ")   # sirve para ingresar el valor de la opción seleccionada
      #os.system('clear')             
      if opcionMenu == "5.1":                            # Para activar la función cambio de porcentaje de ganacia
          print("\n\nhola\n\n")                          # imprime mensaje de saludo
          ganancia()                                     # la función ganancia se ejecuta
     
           

        
      elif opcionMenu == "5.2":                          # Para activar la función para llenar el mostrador con productos
             unidades()                                  # la función unidades se ejecuta
      

      elif opcionMenu == "5.3":                          # Para activar la función  vencimiento de productos
             vencimiento()                               # la función vencimiento se ejecuta

      elif opcionMenu == "5.4":                          # Para activar la función agotamiento de productos
             agotado()                                   # la función agotado se ejecuta
        
        
     

      elif opcionMenu == "9":                            # se elige la activa la opción finalizar menú
          print("\n\n\t\tSistema finalizado")            # mensaje que confirma la finalización del menu
          break                                          # se finaliza el ciclo  del menú
                  
     
    
    
