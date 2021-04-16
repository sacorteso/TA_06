

 

# Creación del menú con sus respectiva opciones

L= "administrador"

def menu():
   
    print("Selecciona una opción")
    print("\t1 - Cambio de clave Global")
    print("\t2 - Ingreso de nuevo empleado")
    print("\t3 - Otras opciones")
    print("\t9 - Terminar con uso de menu")
          
# Se crea un una iteración con wile mientras se cumpla la condición
while True:
      menu()
      opcionMenu = input(" Inserte el número de la opción: ")
          
      if opcionMenu == "1":
          print("hola")
          input("Se ha pulsado la opción 1...\n pulsa enter para continuar")
          
      elif opcionMenu == "2":
          print("")
          input("Se ha pulsado la opción 2...\n pulsa enter para continuar") 
          k= input("Ingrese clave Global: ")
          Tnombre=[]
          Tapellido=[]
          Tclave=[]
          usuario=[]
          
          while(L==k):
            for i in range(1):
               nombre= input("ingrese el nombre: ")
               Tnombre.append(nombre)
               apellido= input("Ingrese el apellido: ")
               Tapellido.append(apellido)
               clave= input("Ingrese la clave")
               Tclave.append(clave)
               usuario= nombre[0:3]+apellido[0:3]+str(i)
               print(usuario)
               print(Tnombre)
               print(Tapellido)
               print(Tclave)
            break
      elif opcionMenu == "3":
              print("")
              input("Se ha pulsado la opción 2...\n pulsa enter para continuar")   
          
      elif opcionMenu == "9":  
            break
      else:
            print("")
            input("No has elegido ningún valor correcto...\n pulsa enter para continuar")
       
          
'''    
# SANTIAGO
listacontras = [] 
#funcion para en ingreso a la lista de contaseñas
def creaciondecontrase():
    contrainic = input("ingrese su nueva contraseña: ")
    contrainic2 = input("ingrese nuevamente su contraseña: ")
    while (contrainic != contrainic2):
        contrainic2 = input("error ingrese nuevamente su contraseña: ")
    return listacontras.append(contrainic)
     
creaciondecontrase()            
print(listacontras)
#confirmacion de prueba para en ingreso a las cuentas
a = input ("ingese la contraseña:")
print (a)
print(a in listacontras)
####


from tkinter import*

def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal= Tk()
    ventana_principal.geometry("300x250") #Dimensiones de la ventana
    ventana_principal.title("Login con tkinder") # Titulo de la ventana
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2",font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack()
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack()
    Label(text="").pack()
    ventana_principal.mainloop()  
    
    '''

