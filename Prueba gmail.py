import cv2
import mimetypes
import smtplib
from os import environ


cap = cv2.VideoCapture(0)

leido, frame = cap.read()

if leido == True:
	cv2.imwrite("C:/Users/LENOVO/Desktop/Proyecto/Fotos/foto.png", frame)
	print("Foto tomada correctamente")
	
else:
	print("Error al acceder a la cámara")

