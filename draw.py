import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('blank', blank)

# #paint a certain color
# # blank[200:300] =  0,255,0
# # cv.imshow('green', blank)

# #2. draw a rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (0,255,0), -1)
# cv.imshow('rectamgle', blank)

# #3.draw a circle
# cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, (255,0,0), 3)
# cv.imshow('circle', blank)

# #4.draw a line
# cv.line(blank, (0,0), (250,250), (0,0,255), 5)
# cv.imshow('line', blank)

#5.write text in image
cv.putText(blank, 'Anuraag', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('text', blank)


cv.waitKey(0)