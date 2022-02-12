import cv2 as cv
from cv2 import Laplacian
import numpy as np

img = cv.imread('rss/photo/park.jpg')
cv.imshow('cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#laplaced

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('laplaced', lap)


#sabel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined = cv.bitwise_or(sobelx, sobely)
cv.imshow('sobelx', sobelx)
cv.imshow('sobely', sobely)
cv.imshow('combined', combined)

#canny
canny = cv.Canny(gray, 150, 175)
cv.imshow('canny', canny)


cv.waitKey(0)