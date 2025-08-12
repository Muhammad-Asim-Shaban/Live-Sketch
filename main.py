import numpy as np
import cv2


capture=cv2.VideoCapture(0)
capture.set(3,640)
capture.set(4,750)
def sketch(frame):
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,10,70)
    ret,mask=cv2.threshold(canny,100,255,cv2.THRESH_BINARY_INV)
    return mask


while True:
    success,image=capture.read()
    cv2.imshow("Sketched image",sketch(image))
    cv2.waitKey(1)

