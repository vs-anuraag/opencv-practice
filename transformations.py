import cv2 as cv
from cv2 import imshow 
import numpy as np

img = cv.imread('rss/photo/park.jpg')

cv.imshow('park', img)

#translations
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, -100, -100)
cv.imshow('translated img', translated)

#rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img,45)
cv.imshow('rotated', rotated)
rotatedx2 = rotate(rotated,90)
cv.imshow('rotated 2x times', rotatedx2)

#resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
imshow('resized', resized)

#fliping 
flip = cv.flip(img, -1)
cv.imshow('flip', flip)

#croping
croped = img[200:400, 300:400]
cv.imshow('cropped', croped)


cv.waitKey(0)