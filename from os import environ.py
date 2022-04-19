from os import environ
from email.message import EmailMessage
from email.message import MIMEImage
import smtplib


Password = 'MacasteAjo'
secret_key = environ["Contraseña_Gmail"]
gmail = environ["Gmail"]


conexion = smtplib.SMTP( "smtp.gmail.com", port= 587)
conexion.ehlo()
    #Encriptación TLS
conexion.starttls()
    #Inciar sesión en el servidor STMP 
conexion.login(gmail,secret_key)
   #Mensaje
msg = EmailMessage()
msg.set_content(f"Your password is {Password}")
msg['Subject'] = "Security System Password"
#Adjuntamos imagen 
file = open("C:/Users/LENOVO/Desktop/Proyecto/Fotos/foto.png", "rb")
attach_image = MIMEImage(file.read())
attach_image.add_header('Content-Disposition', 'attachment; filename = "foto.png"')
msg.attach(attach_image)
    #Enviar correo 
conexion.sendmail(gmail,"proyectossoftware2@gmail.com",msg.as_string())
    #Desctonectamos conexión del server
conexion.quit()
print("Su contraseña se ha enviado correctamente!")