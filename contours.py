import cv2 as cv
import numpy as np

img = cv.imread('rss/photo/cats.jpg')

cv.imshow('cat',img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# canny = cv.Canny(blur,125,175)
# cv.imshow('canny edges', canny)

ret, tresh = cv.threshold(gray,125,255, cv.THRESH_BINARY)
cv.imshow('trsh', tresh)

contours, hierarchies = cv.findContours(tresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours) } contour(s) found!:')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('contours', blank)

cv.waitKey(0)
