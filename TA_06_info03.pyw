

#k=input("ingrese su clave: ")
#L="administrador"
#Tnombre=[]
#Tapellido=[]
#Tclave=[]
#total=[]
#while(L==k):
#      for i in range(3):
#      nombre=input("ingrese su nombre: ")
#      Tnombre=nombre
#      apellido=input("ingrese su apellido: ")
#       Tapellido=apellido
#        clave= input("ingrese su clave: ")
#       Tclave= clave
#  

#        print(i)
#      break
#print(total)      
#lista de las nuevas contraseñas      
listacontras = [] 
#funcion para en ingreso a la lista de contaseñas
def creaciondecontrase():
      contrainic = input("ingrese su nueva contraseña: ")
      contrainic2 = input("ingrese nuevamente su contraseña: ")
     while (contrainic != contrainic2) :
         contrainic2 = input("error ingrese nuevamente su contraseña: ")
     return listacontras.append(contrainic))
     
creaciondecontrase()            
print(listacontras)
a = input ("ingese la contraseña:")
print (a)
print(a in lista1)

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
