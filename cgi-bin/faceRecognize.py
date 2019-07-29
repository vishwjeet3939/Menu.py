#!/usr/bin/python36
import cv2
import numpy as np
import webbrowser
website = "http://Server_ip/new1.html"
pathOfWeb="/usr/bin/firefox"
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("trainingData.yml")
id = 0
font =cv2.FONT_HERSHEY_COMPLEX_SMALL
while 1:
    ret,img=cam.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==1):
            webbrowser.get(pathOfWeb).open_new_tab(website)
            cam.release()
            cv2.destroyAllWindows()
        elif(id==2):
            id='ShahRukKhan'
        elif(id==3):
            id='Saloni'
        elif(id==4):
            id='Raxxxx Dii'
        elif(id==5):
            id='Mr. Beck'
        elif(id==6):
            id='Mr. Viral'

        else:
            id="User Not Authorised"
     #   cv2.putText(img,str(id),(x,y+h), font, 2,(255,0,0),3);
    #cv2.imshow("Face",img)
    if (cv2.waitKey(1) == 27):
        break
cam.release()
cv2.destroyAlWindows()
