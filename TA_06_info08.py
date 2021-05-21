from datetime import date as dt #librería para manejar fechas
from datetime import datetime as dtt  #librería para manejar el tiempo
from datetime import timedelta        #librearía para realizar operaciones matemáticas con el tiempo
import pandas as pd # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os           # Librerías para realizar funciones internas del software
import csv          # Librería para manipular archivos con extensión csv
import time         # Librería para manipular el tiempo
#import matplotlib.pyplot as plt
#import openpyxl


def proveedor(): # se crea funcion proveedor
  while True:

    CA0=[]#se crea lista para almacenar la indentificacion del cliente
    PP01=[]#se crea lista para almacenar la referencia del producto
    PP02=[]#se crea lista para almacenar el nombre del producto
    PP03=[]#se crea lista para almacenar el valor unitario del producto
    PP04=[]#se crea lista para almacenar la cantidad de productos que se va a comprar un cliente respecto a una referencia determinada 
    PP05=[]#se crea lista para almacenar el subtotal de la compra por referencia de producto
    PP06=[]#se crea lista para almacenar la fecha
    PP07=[]#se crea lista para almacenar la hora
    PP08=[]
  
    print("\n\n\n\n\t\t\t\t\t              PÁGINA PROVEEDORES") # titulo de la página de clientes
    PPP01=input("\n\nIngrese el nombre de la empresa: ")          # Para ingrese la identificación
    PPP02=input("\n\nIngrese el nombre del vendedor: ")        # Para ingresar el nombre del cliente
    PPP03=input("\n\nIngrese el primer apellido de vendedor: ")           # Para ingresar el primer apellido del cliente
    PPP04=input("\n\nIngrese el segundo apellido del vendedor: ")          # Para ingresar el segundo apellido del cliente
    PPP05=input("\n\nIngrese el numero de celular de la empresa: ")         # para ingresasar el número del celular
    PPP06=input("\n\nIngrese el numero fijo de la empresa: ")       
    PPP07=input("ingrese el correo de la empresa: ")        # para ingresar el número del teléfono fijo
    PPP08=input("Ingrese el primer dia de visita de la semana: ")
    PPP09=input("ingrese el segundo dia de visita: ")
    CA0.append(PPP01) #se crea lista para almacenar la identificacion del cliente
    PP01.append(PPP02) #se crea lista para almacenar la identificacion del cliente
    PP02.append(PPP03) #se crea lista para almacenar la identificacion del cliente
    PP03.append(PPP04) #se crea lista para almacenar la identificacion del cliente
    PP04.append(PPP05) #se crea lista para almacenar la identificacion del cliente
    PP05.append(PPP06) #se crea lista para almacenar la identificacion del cliente
    PP06.append(PPP07)
    PP07.append(PPP08)
    PP08.append(PPP09)
  
    CL=(CA0,PP01,PP02,PP03,PP04,PP05,PP06,PP07,PP08)      # se crea lista con los datos del cliente
    PL01=pd.DataFrame(CL)             # Se crea DataFrame con los datos del cliente
    PL02=pd.DataFrame.transpose(PL01)  # se transpone el DataFrame
    PL02.columns=["Empresa","NVendedor","Papellido","Sapellido","Celular","Fijo","Correo","Pvisita","Svisita"]
    PL02.to_csv('BDATOS/proveedor.csv', mode="a", index="", header="") # se graba la información del cliente en la base de datos clientes
    PL03=pd.read_csv('BDATOS/proveedor.csv')  # se lee la base e datos de cliente
    print(PL03)                              # Se imprime la base de datos cliente
  #else:
    break

print("\t\t\t\t PÁGINA PRINCIPAL DE PROVEEDORES\n\n")    # se imprime el titulo de la página del menu del manejo operativo del negocio


def menu():                                                # se crea un menu para el manejo operativo del negocio
    
    print("\n\n\n\nSelecciona una opción \n")              # se imprime mensaje del menú
    print("\t8.1 - Costos de Bodega completa ")            # se imprime registro de costos de bodega forma completa
    print("\t7.2 - Costos de bodega por fechas")           # se imprime registro de costos de bodega forma fechas específicas
    print("\t7.3 - Ingreso de datos para costos fijos")    # se imprime opción para anexar datos de costsos fijos
    print("\t7.4 - Costos fijos completos")                # se imprime el registro de costos fijos la base completa
    print("\t7.5 - Costos fijos por fecha")                # se imprme el registro  de costos fijos la base por fecha específica
    print("\t7.6 - Ingresos por ventas - completa")        # se imprime el registro de ventas la base completa
    print("\t7.7 - Ingresos por ventas - manejo por fechas") # Se imprime el registro de ventas la base por fecha específica
    print("\t7.8 - CONTABILIDAD")                          # se imprime la opción del control toal de la contabilidad
    print("\t9 - Terminar con uso de menu")              # se imprime finalizacón de menú
          
# Se crea un una iteración con while mientras se cumpla la condición
while True:                                              # se activa el ciclo while para activar el menú
      menu()                                             # se activa la función menú
      opcionMenu = input("\n Inserte el número de la opción: ")   # sirve para ingresar el valor de la opción seleccionada
                  
      if opcionMenu == "8.1":                            # Para activar la función costos de bodega forma completa
          print("\n\nhola\n\n")                          # imprime mensaje de saludo
          proveedor()                                    # la función costos de bodega de forma completa se ejecuta
     
           

        
      elif opcionMenu == "7.2":                          # Para activar la función costos de bodega forma por fechas específicas
             bodegafecha()                               # la función costos de bodega de forma por fechas específicas se ejecuta
      

      elif opcionMenu == "7.3":                          # se activa la función ingresos de datos para costos fijos
             ingcostosf()                                # Se ejecuta la función ingresos de datos para costos fijos
        
      elif opcionMenu == "7.4":                          # se activa la función costos fijos forma completa
            costosf()                                    # Se ejecuta la función costos fijos forma completa

      elif opcionMenu == "7.5":                          # se activa la función costos fijos forma fecha específica
             costosff()                                  # Se ejecuta la función costos fijos forma fecha específica


      elif opcionMenu == "7.6":                          # se activa la función ventas en forma completa
             ingventasT()                                # se ejecuta la función ventas en forma fechas específica

      elif opcionMenu == "7.7":                          # se activa la función ventas en forma fechas específica
              ingventasTF()                              # se ejecuta la función ventas en forma fechas específica

      elif opcionMenu == "7.8":                          # se activa la función contabilidad total del negocio
             contabilidad()                              # se ejecuta la función contabilidad total del negocio

      #elif opcionMenu == "9":                           # se elige la activa la opción finalizar menú
          #print("\n\n\t\tSistema finalizado")           # mensaje que confirma la finalización del menu
         # break                                         # se finaliza el ciclo if del menú









'''
#funcionando
# Valor de productos por paca
co = pd.read_csv("BDATOS/bodega1.csv")
cp=co['Producto']
co2=co['Ppaca']
C=[cp,co2]


co5=pd.DataFrame(C)
co6=pd.DataFrame.transpose(co5)
print(co6)
co6.set_index('Producto',inplace=True)
print(co6)

co6.plot( kind = 'bar')
plt.title("INFORME DE BODEGA\n VALOR DE LOS PRODUCTOS POR PACA")
plt.ylabel('Precio en pesos')
plt.xlabel('Producto')

plt.show()
'''
'''
# funcionando
# Para ventas
fventas = pd.read_csv("BDATOS/ventas.csv")

f1=fventas['Vtotal']
f2=fventas['Fecha']
C1=[f1,f2]


ffventas=pd.DataFrame(C1)
print(ffventas)
ff1ventas=pd.DataFrame.transpose(ffventas)
#ff1ventas=ff1ventas.groupby(['Fecha']).mean()
print(ff1ventas)
ff1ventas.set_index('Fecha',inplace=True)
print(ff1ventas)



ff1ventas.plot( kind = 'bar')
plt.title("INFORME DE VENTAS\nVALOR DE LAS VENTAS POR FECHAS")
plt.ylabel('Precio en pesos')
plt.xlabel('Fecha')

plt.show()
'''

'''
# Funcionando
# unidades en bodega
co = pd.read_csv("BDATOS/bodega1.csv")
cpp=co['Producto']
cco2=co['unidades']
C=[cpp,cco2]


co6=pd.DataFrame(C)
co7=pd.DataFrame.transpose(co6)
print(co7)
co7.set_index('Producto',inplace=True)
print(co7)

co7.plot( kind = 'bar')
plt.title("INFORME DE BODEGA\n Cantidad de unidades por producto")
plt.ylabel('Cantidad de unidades')
plt.xlabel('Producto')

plt.show()
'''
'''
#calendario
print('ingrese el número del mes y el día: ', end='')
mes, dia = map(int, input().split())


semana={1:'Lunes', 2:'Martes', 3:'Miércoles', 4:'Jueves',
        5:'Viernes', 6:'Sábado', 7:'Domingo'}

L58=pd.read_csv('BDATOS/ventas.csv')
L58=pd.DataFrame(L58['Fecha'])
print(L58)

L58['Fecha']= pd.to_datetime(L58['Fecha'], format="%Y%m%d" )
print(L58)

#L58['Fecha']= pd.to_datetime(L58['Fecha'], format="%U" )
print(L58)
LA58=[]
LB58=[]
LC58=[]


#L58.strftime()

LA58 = [L58['Fecha'].dt.year]
LA58=str(LA58)
LB58 = [L58['Fecha'].dt.month]
LB58=str(LB58)
LC58 = [L58['Fecha'].dt.day]
LC58=str(LC58)

print(LA58)
print(LB58)
print(LC58)




#numero_dia=dt.isoweekday(dt(LA58,LB58,LC58))



#numero_dia=dt.isoweekday(dt(2021,mes,dia))

#print('El nombre del día es: %s' % semana[numero_dia])
'''
#IF,capitalbase,CBodega,Cfijos,Ventas,EntrdaExtra,porc,ganancianeta,Disponible

###inf= pd.read_csv("BDATOS/contabilidad1.csv")
###print(inf)
###inf1=inf['IF']
###inf2=inf['capitalbase']
###inf3=inf['CBodega']
###inf4=inf['Cfijos']
###inf5=inf['ganancianeta']

###print(inf1)
###print(inf2)
###print(inf3)
###print(inf4)
###print(inf5)
#FUNCIONA
# CAPITAL BASE
'''
C11=[inf1,inf2]

C12=pd.DataFrame(C11)
C13=pd.DataFrame.transpose(C12)
print(C13)
C13.set_index('IF',inplace=True)
print(C13)

C13.plot( kind = 'bar')
plt.title("INFORME DE CONTABILIDAD\n CAPITAL BASE")
plt.ylabel('DINERO EN PESOS')
plt.xlabel('FECHA')

plt.show()
'''
'''
#FUNCIONA
# COSTOS DE BODEGA
C21=[inf1,inf3]

C22=pd.DataFrame(C21)
C23=pd.DataFrame.transpose(C22)
print(C23)
C23.set_index('IF',inplace=True)
print(C23)

C23.plot( kind = 'bar')
plt.title("INFORME DE CONTABILIDAD\n COSTOS BODEGA")
plt.ylabel('DINERO EN PESOS')
plt.xlabel('FECHA')

plt.show()
'''
'''
#FUNCIONA
# COSTOS FIJOS
C31=[inf1,inf4]

C32=pd.DataFrame(C31)
C33=pd.DataFrame.transpose(C32)
print(C33)
C33.set_index('IF',inplace=True)
print(C33)

C33.plot( kind = 'bar')
plt.title("INFORME DE CONTABILIDAD\n COSTOS FIJOS")
plt.ylabel('DINERO EN PESOS')
plt.xlabel('FECHA')

plt.show()

'''
'''
# GANANCIA NETA
C41=[inf1,inf5]

C411=pd.DataFrame(C41)
C43=pd.DataFrame.transpose(C411)
print(C43)
C43.set_index('IF',inplace=True)
print(C43)

#C43.plot( ax=ax1, kind = 'bar')
#plt.title("INFORME DE CONTABILIDAD\n GANANCIA NETA")
#plt.ylabel('DINERO EN PESOS')
#plt.xlabel('FECHA')

#plt.show()



fig,(ax1)=plt.figure()
C43.plot( ax=ax1, kind = 'bar')
ax=fig.add_subplot(221)
ax.plot(ax1, color="blue")
plt.show()
'''


###C41=[inf1,inf2,inf3,inf4,inf5]

###C411=pd.DataFrame(C41)
###C43=pd.DataFrame.transpose(C411)
###C43.plot(x="IF", y=["capitalbase","CBodega","Cfijos","ganancianeta"],kind='bar')
###plt.show()
