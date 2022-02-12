from pyexpat import features
from tkinter import Label
import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(r'rss/face/val/madonna/4.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('person', gray)

#detect the face
face_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,z,h) in face_rect:
    face_roi = gray[y:y+h,x:x+z]

    label, confidence = face_recognizer.predict(face_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX, 1.0, 255, 2)
    cv.rectangle(img, (x,y),(x+z,y+h), 255, 2)


cv.imshow('face recognized', img)

cv.waitKey(0)