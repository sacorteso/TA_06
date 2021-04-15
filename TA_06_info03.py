

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
      
    






def ventana_inicio():
    global ventana_principal
    pestas_color="DarkGrey"
    ventana_principal=TK()
    ventana_principal.geometry("300x250") #Dimensiones de la ventana
    ventana_principal.title("Login con tkinder") # Titulo de la ventana
    Label(text="Escoja su opción", bg="LightGreen", width="300", height="2",font=("Calibri",13)).pack()
    Label(text="").pack()
    Button(text="Acceder", height="2", width="30", bg=pestas_color, command=login).pack()
    Label(text="").pack()
    Button(text="Registrarse", height="2", width="30", bg=pestas_color, command=registro).pack()
    Label(text="").pack()
    ventana_principal.mainloop()
      
