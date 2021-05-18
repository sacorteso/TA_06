

### ADVERTENCIA
#  La clave global es jefe
# librerías para manejar base de datos
import pandas as pd # Librería para utilizar y manipular dataframe
import numpy as np  # Librería para realizar operaciones matemáticas y manejo de matrices
import os           # Librerías para realizar funciones internas del software
import csv          # Librería para manipular archivos excel y con extensión .csv 


listacontras = [] 
#funcion para en ingreso a la lista de contaseñas
def creaciondecontrase():  
    while True:   # ciclo while para comprobar las contraseñas
        #contrainic= input("ingrese una nueva contraseña con al menos 8 a 15 caracteres: ")
        contrainic = input("\nIngrese nueva contraseña de 8 a 15 caracteres:")
        longitud1 = len(contrainic)
        print("su contraseña tiene:", longitud1, "caracteres")
        if longitud1 > 7 and longitud1 < 16 :
          print("correcto") 
          break
        else:
           contrainic = input("Presione cualquier tecla para reintentar: ")
    contrainic2 = input("ingrese nuevamente su contraseña: ")
    while (contrainic != contrainic2):
        contrainic2 = input("error ingrese nuevamente su contraseña: ")
    return str(contrainic)
contrainic = ()

          


# Creación del menú con sus respectiva opciones
import os
#import pandas as pd #librería para Dataframe
#import numpy as np  #librería para Dataframe
# lectura de la clave global desde archivo txt
with open('CLAVES/Global.txt', 'r') as Ltexto:
  L = Ltexto.readline()
# inicio de la función menú
def menu():
    1
    print("Selecciona una opción \n")
    print("\t1   -   Cambio de clave Global")
    print("\t2   -   Login y clave para nuevo empleado")
    print("\t2.1 -   Base de dtos de empleados")
    print("\t3   -   Otras opciones")
    print("\t9   -   Terminar con uso de menu")
          
# Se crea un una iteración con wile mientras se cumpla la condición

while True:
      menu()
      opcionMenu = input("\n Inserte el número de la opción: ")
      
      
      Ltexto.close()
      if opcionMenu == "1": # Opción para cambiar la clave global
          print("\nhola\n") # saludo
          input("Se ha pulsado la opción 1...\n pulsa enter para continuar") #confirmación que lselecciono opción 1
          T = input("\nIngrese clave Global: ") #solicitud de ingreso de clave global
          if L == T: # Comparador de claves
            K=input("\nIngrese nueva clave: ") # solicitud para nueva clave
            K1=input("\nIngrese nuevamente la nueva clave: ") # Solicitud para nueva clave
            if K == K1: # compara que la nueva clave si la recuerda el usuario
              L = K1 # variable adicional
              Ltexto=open("CLAVES/Global.txt","w+") # se activa la función para eliminar la clave vieja del archivo txt
              Ltexto.write(L) # se escribe la nueva clave global en el archivo txt
              Ltexto.close() # se cierra el archivo txt que guarda la clave global.
              
              print(" \n Clave Global modificada\n") # anuncio que la clave global fue modificada
          else:
            break               # opción si no se ingresa la clave global correcta.
            print("\nregrese a menú e intentelo de nuevo\n")  


          
      elif opcionMenu == "2": # Opción para ingresar los datos de los empleados, generar login de usuario y claves.
          
         
          input("\nSe ha pulsado la opción 2...\n pulsa enter para continuar ") 
          k= input("\nIngrese clave Global: ") # ingresa clave global para permiti hacer actualizaciones
          
         
          while(L==k):# permite crear un cilclo para ingresar nuevos empleados
            for i in range(1):
               nombre= input("\ningrese el nombre: ")  # para ingresar nombre del empleado
               apellido= input("\nIngrese el apellido: ") # para ingresar el apellido
               clave = creaciondecontrase() # para ingresar una clave manual a gusto del empleado
               usuario= nombre[0:3]+apellido[0:3] #+str(i) # permite creae el login de usuario
               os.system('clear') # limpia la pantalla
               listacontras.append(clave)
               
               # confirma visualmente los datos ingrsados por el administrador
               print("\n", "Su nombre es: ", nombre,"\n")
               print("\n", "Su apellido es: ", apellido, "\n")
               print("\n", "Su clave es: ", clave, "\n")
               print("\n", "Su Login es: ", usuario,"\n")
               
               # para crear bases datos (nombre) para dataframe
               LNombre=open("BDATOS/Nombre.txt", "a+")
               LNombre.write(nombre)
               LNombre.write("\n")
               LNombre.close()
               with open('BDATOS/Nombre.txt', 'r') as Nom:
                    LN = Nom.readlines()
                    #print(LN)
               LNombre.close()
                            
               # para crear bases datos (apellido) para dataframe                
               LApellido=open("BDATOS/Apellido.txt", "a+")
               LApellido.write(apellido)
               LApellido.write('\n')
               LApellido.close()
               with open('BDATOS/Apellido.txt', 'r') as Ape:
                    LA = Ape.readlines()
                   # print(LA)
               LApellido.close()
                            
               # para crear bases datos (clave de usuario) para dataframe
               LClave=open("CLAVES/Clave.txt", "a+")
               LClave.write(clave)
               LClave.write("\n")
               LClave.close()
               with open('CLAVES/Clave.txt', 'r') as Cla:
                    LC = Cla.readlines()
                   # print(LC)
               LClave.close()

               # para crear bases datos (login de usuario) para dataframe
               LUsuario=open("BDATOS/Usuario.txt", "a+")
               LUsuario.write(usuario)
               LUsuario.write("\n")
               LUsuario.close()
               with open('BDATOS/Usuario.txt', 'r') as Usu:
                    LU = Usu.readlines()
                    #print(LU,"\n")
                    print("\n")
               LUsuario.close()
            break
      elif opcionMenu == "2.1":      
               os.system('clear')                      # Sirve para limpiar la pantalla
               print("\t\t\t\t BASE DE DATOS CON LOS EMPLEADOS \n\n")   
               
               with open('BDATOS/Nombre.txt', 'r') as Nom: # se lee base da datos con los nombres
                    LN = Nom.readlines()                   # lista con los nombres
               with open('BDATOS/Apellido.txt', 'r') as Ape:# se lee base de datos con los apellidos
                    LA = Ape.readlines()                    # lista con los apellidos
               with open('CLAVES/Clave.txt', 'r') as Cla:   # se lee base de datos con las claves de los empleados
                    LC = Cla.readlines()                    # lista con las claves

               #Se crea DataFrame para los datos de los empleados           
               df= pd.DataFrame(list(zip(LN,LA,LC)), columns =['Nombre','Apellido','Clave'])
               print(df)
               
               break

      elif opcionMenu == "3":
              print("por el momento no hay opciones")
              input("\nSe ha pulsado la opción 3...\n pulsa enter para finalizar")
              break  
               
              # finalización del ciclo del menú
      elif opcionMenu == "9":
              print("fin del programa")
              input("\nSe ha pulsado la opción 9...\n pulsa enter para finalizar")
              break


