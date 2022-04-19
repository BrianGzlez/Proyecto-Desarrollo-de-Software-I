from atexit import register
import cv2 
import numpy as  np
import os 
from matplotlib import pyplot as plt
from mtcnn.mtcnn import MTCNN


#Ubicación en la que se guardaran las fotos 
path = "C:/Users/BRIAN/OneDrive - INTEC/Escritorio/Proyecto/Reconocimiento"

user = input("Your name: ")
cap = cv2.VideoCapture(0)
user_reg_img = user 
img = f"{user_reg_img}.jpg"

def face(img, faces):
    data = plt.imread(img)
    for i in range(len(faces)):
        x1, y1, ancho, alto = faces[i]["box"]
        x2, y2 = x1 + ancho, y1 + alto
        plt.subplot(1,len(faces), i + 1)
        plt.axis("off")
        face = cv2.resize(data[y1:y2, x1:x2],(150,200), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(img, face)
        plt.imshow(data[y1:y2, x1:x2])

while True:
    ret, frame =  cap.read()
    cv2.imshow("Registro Facial", frame)
    if cv2.waitKey(1)== 27:
        break 
    
cv2.imwrite(f"C:/Users/BRIAN/OneDrive - INTEC/Escritorio/Proyecto/Reconocimiento/{img}", frame)
print("Foto tomada correctamente")
cap.release()
cv2.destroyAllWindows()

pixels = plt.imread(img)
faces = MTCNN().detect_faces(pixels)
face(img,faces)


#Linea para registrar en la base de datos
#register_face_db(img) es una funcion que tiene como parametro la imagen 


def login_capture():
    cap = cv2.VideoCapture(0)
    user_login = user2.get()
    img = f"{user_login}_login.jpg"
    img_user = f"{user_login}.jpg"

    while True:
        ret, frame = cap.read()
        cv2.imshow("Login Facial", frame)
        if cv2.waitKey(1) == 27:
            break
    
    cv2.imwrite(img, frame)
    cap.release()
    cv2.destroyAllWindows()

    pixels = plt.imread(img)
    faces = MTCNN().detect_faces(pixels)
    face(img, faces)

  

    res_db = db.getUser(user_login, path + img_user)
    if(res_db["affected"]):
        my_files = os.listdir()
        if img_user in my_files:
            face_reg = cv2.imread(img_user, 0)
            face_log = cv2.imread(img, 0)

            comp = compatibility(face_reg, face_log)
            
            if comp >= 0.94:
                print("{}Compatibilidad del {:.1%}{}".format(color_success, float(comp), color_normal))
                printAndShow(screen2, f"Bienvenido, {user_login}", 1)
            else:
                print("{}Compatibilidad del {:.1%}{}".format(color_error, float(comp), color_normal))
                printAndShow(screen2, "¡Error! Incopatibilidad de datos", 0)
            os.remove(img_user)
    
        else:
            printAndShow(screen2, "¡Error! Usuario no encontrado", 0)
    else:
        printAndShow(screen2, "¡Error! Usuario no encontrado", 0)


