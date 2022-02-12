import cv2 as cv

img = cv.imread('rss/photo/cats.jpg')
cv.imshow('cats',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#simple tresholding
threshold, tresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('threshold simple', tresh)

threshold, tresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshold simple inverse', tresh_inv)

#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('adaptive tresh', adaptive_thresh)

cv.waitKey(0)