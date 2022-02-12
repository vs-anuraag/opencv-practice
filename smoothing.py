import cv2 as cv
from cv2 import GaussianBlur
from matplotlib.image import imsave

img = cv.imread('rss/photo/cats.jpg')

cv.imshow('cats',img)

# averaging
average = cv.blur(img, (3,3))
cv.imshow('avg', average)

#gussian blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gauss', gauss)

#mediam blur
median = cv.medianBlur(img, 3)
cv.imshow('median',median)

#bilateral blur
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)