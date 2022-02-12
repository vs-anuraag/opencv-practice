import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('rss/photo/park.jpg')
cv.imshow('park',img)

# plt.imshow(img)
# plt.show()

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#bgr to hsv huge saturation value
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv', hsv)

#bgr to l*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('lab', lab)

#bgr to rgb
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('rgb', rgb)

#hsv to bgr
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('hsv to bgr', hsv_bgr)
#can do LAB to bgr
#cant do directly grom gray to hsv or others
#need to convert to bgr first

# plt.imshow(rgb)
# plt.show()


cv.waitKey(0)