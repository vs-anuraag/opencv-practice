import cv2 as cv

# image reading
img = cv.imread('rss/photo/cat.jpg')

cv.imshow('1',img)
cv.waitKey(0)

# reading video
capture =cv.VideoCapture('rss/vid/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
        
capture.release()
cv.destroyAllWindows()
