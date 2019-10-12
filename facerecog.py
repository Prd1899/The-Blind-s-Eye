import cv2
import numpy as np
from imutils.video.pivideostream import PiVideoStream
from imutils.video import FPS
from picamera.array import PiRGBArray
from picamera import PiCamera
from subprocess import call
import time
import argparse
import imutils
import speech_recognition as sr
from brain1 import brain1
from SenseCells.tts import tts
#Load pretrained cascade face detection
face_cascade = cv2.CascadeClassifier('lbpcascade_frontalface.xml')
#Load improved FPS video instead of the default Picamera
reader  = PiVideoStream().start()
time.sleep(0.2)
#Load the recognizer
rec = cv2.face.createLBPHFaceRecognizer()
#Load trained local binary pattern face data
rec.load("recognizer/trainingData.yml")
id=0
c=0
font = cv2.FONT_HERSHEY_SIMPLEX
tts('Welcome user, systems are now ready to run. How can I help you?')
def hey():
	#read each frame in the real-time video
    frame = reader.read()
    image=frame
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	#Use histogram equalizer for adjusting face in different light condition
    equ = cv2.equalizeHist(gray) 
    faces = face_cascade.detectMultiScale(equ, 1.05, 5,minSize=(10,10))
	#If the face is not frontal face then rotate the face by +30/-30 degree
    if len(faces)==0:
                rows,cols = equ.shape
                M = cv2.getRotationMatrix2D((cols/2,rows/2),30,1)
                dst = cv2.warpAffine(equ,M,(cols,rows))
                faces = face_cascade.detectMultiScale(dst, 1.05, 5,minSize=(10,10))
                if len(faces)==0:
                        rows,cols = equ.shape
                        M = cv2.getRotationMatrix2D((cols/2,rows/2),-30,1)
                        dst = cv2.warpAffine(equ,M,(cols,rows))
                        faces = face_cascade.detectMultiScale(dst, 1.05, 5,minSize=(10,10))
                        detectFace(faces,dst,image)
                else:
                    detectFace(faces,dst,image)
    else:
        detectFace(faces,equ,image)

    cv2.imshow('Face', image)
    if(cv2.waitKey(1)==ord('q')):
        cap.release()
        cv2.destroyAllWindows()
       
#Face recognition function
def detectFace(faces,hog,image):
        for (x, y, w, h) in faces:
                cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
                result = cv2.face.MinDistancePredictCollector()
                rec.predict(hog[y:y+h,x:x+w],result, 0)
                id = result.getLabel()

                conf = result.getDist()
                if(conf<150):
                        if(id==1):
                                id="Pratham_"+str(conf)
                                speech1="It is Pratham"
                                call(["espeak",speech1]) 

  
                        if(id==2):
                                id="Shubh_"+str(conf)
                                speech2="It is Shubh"
                                call(["espeak",speech2])	   
                        if(id==0):
                                id="Unknown_"+str(conf)
                                speech3="Unknown"
                                call(["espeak",speech3])
                c=c+1
                cv2.putText(image,str(id),(x,y+h),font,1,(255,255,255),2,cv2.LINE_AA)		
def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=5)
        print("Say something!")
        audio = r.listen(source)
    try:
        speech_text = r.recognize_google(audio).lower().replace("'", "")
        call(["espeak",speech_text])
        print("Jarvis thinks you said '" + speech_text + "'")
        if(speech_text == "recognise"):
                hey()
    except sr.UnknownValueError:
        print("Jarvis could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service;{0}".format(e))
    brain1(speech_text)
    main()

main()
