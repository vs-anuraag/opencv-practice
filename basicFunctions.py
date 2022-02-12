import cv2 as cv

img = cv.imread('rss/photo/park.jpg')

cv.imshow('1',img)

#convert to gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('i1', gray)

#bluring
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
#the 3,3 can bve cahnged to any odd number to for increasing or decreasing the blur effect
cv.imshow('blur', blur)
 
#edge cascade/detection
canny = cv.Canny(blur, 125, 175)
cv.imshow('edge detection', canny)

#dialating the image
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

#eroding
eroded = cv.erode(dilated, (3,3), iterations=3)
cv.imshow('eroded', eroded)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('resozed', resized) 

#croping
cropped = img[50:200, 200:400]
cv.imshow('cropped', cropped)


cv.waitKey(0)