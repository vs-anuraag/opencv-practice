from re import I
import cv2 as cv

# image reading
img = cv.imread('rss/photo/cat_large.jpg')
cv.imshow('1',img)

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    capture.set(3,width)
    capture.set(4,height)



resizedImage = rescaleFrame(img)
cv.imshow('resized image', resizedImage)

#reading video
capture =cv.VideoCapture('rss/vid/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)

    cv.imshow('video', frame)
    cv.imshow('video_shape_changed', frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
        
capture.release()
cv.destroyAllWindows()