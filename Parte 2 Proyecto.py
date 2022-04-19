#Parte 2 Proyecto
from ast import Pass
from atexit import register
from calendar import c
import email
#from email.message import Message
from os import environ
import smtplib
from random import choice 

#Variables globales
global Password
global Password_database
global User_database 
global Gmail_datebase
global Gmail 
global User 
Password_database = []
User_database = []
Gmail_database = []

def Registrarse():
    
    User = input("Introduzca su nombre de Usuario: ")
    Gmail = input("Introduzca su correo de gmail:  ")
    
    if Gmail.count("@") == 1:
        Gmail_database.append(Gmail)
    else: 
        print("Su correo no esta bien estructurado.")
        Registrarse()

    User_database.append(User)
    decision = int(input("Desea una general una constraseña aleatoria o configurarla por usted: \n Lista de opciones  \n 1) Presione 1 para elegir contraseña aleatoria \n 2) Presione 2 para introducir la contraseña \n" ))
    
    

    def Elegir_Contraseña():
        Password = ""
        NPassword = input("Seleccione la contraseña :")
        Password = NPassword
        Password_database.append(Password)
        print(f"Tu contraseña es {Password}")
        print(f"Tu usuario es {User_database}, tu contraseña es {Password_database}, tu correo es {Gmail_database} ")


    def Random_Password():
        Password = ""
        longitud = 8 
        valores = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPLKJHGFDSAMNBVCXZ!/&%$#"
        Contraseña_Random = ""
        Contraseña_Random = Contraseña_Random.join([choice(valores)for i in range(longitud)])
        print(f"Tu contraseña generada es {Contraseña_Random}")
        

        print("Quiere utilizar otra contraseña: \n 1) Presione 1 en caso de querer utilizar otra contraseña \n 2) Presione 2 en caso de que le guste la contraseña asignada")
        Password = Contraseña_Random
        Elecion1 = int(input())
        

        if Elecion1 == 1: 
            Random_Password()
        elif Elecion1 == 2:
            print("Contraseña establecida")
            print(f"Su contraseña es {Password}")
            Password_database.append(Password)
        else:
            print("La opción utilizada no es permitida...")
            print("Restableciendo contraseña.....")
            Registrarse()
        print(f"Tu usuario es {User_database}, tu contraseña es {Password_database}, tu correo es {Gmail_database} ")
        Menu_Principal()
    
    
    

    if decision == 1: 
        Random_Password()
    elif decision == 2: 
        Elegir_Contraseña()



def Restablecer_Contraseña():
       Search_User = input("Digite el usuario de la cuenta que desea recuperar: ")

       for i in User_database:
          if Search_User == User:
            NewPassword =input("Introduzca su nueva contraseña")
            Verificicacion = input("Introduzca la contraseña de nuevo")
            if Verificicacion == NewPassword:
                print("Su contraseña ha sido restablecida")
                Password = NewPassword
            elif Verificicacion != NewPassword:
                print("La contraseña no coinciden.")

       NewPassword = Password     


def Enviar_Contraseña():
    #Variables de entorno
   secret_key = environ["Contraseña"]
   gmail = environ["Gmail"]


   conexion = smtplib.SMTP( "smtp.gmail.com", port= 587)
   conexion.ehlo()
    #Encriptación TLS
   conexion.starttls()
    #Inciar sesión en el servidor STMP 
   conexion.login(gmail,secret_key)
   #Mensaje
   Message = f"Your password is: {Password}"
    #Enviar correo 
   conexion.sendmail(email,"proyectossoftware2@gmail.com",)
    #Desctonectamos conexión del server
   conexion.quit()
   print("Su contraseña se ha enviado correctamente!")


def login():
    Login_Usuario = input("Introduzca su usuario: ")
    if not Login_Usuario in User_database:
        print("Usuario no encontrado")
    else:
        Login_Contraseña = input("Introduzca su contraseña: ")
        if not Login_Contraseña in Password_database:
          print("Contraseña incorrecta.")
        

    



    




def Menu_Principal():
    Menu =int(input('Menu Principal \n 1- Login \n 2- Registro \n 3- Restablecer contraseña \n'))

    if Menu == 1:
        login()
    elif Menu == 2:
        Registrarse()
    elif Menu == 3:
        Restablecer_Contraseña()

Menu_Principal()