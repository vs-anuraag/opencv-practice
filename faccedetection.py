import cv2 as cv

img = cv.imread('rss/photo/group 1.jpg')
cv.imshow('lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray person', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=2)

print(f'number if faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (255), 2)

cv.imshow('detectected', img)

cv.imwrite('result1.jpg', img)

cv.waitKey(0)