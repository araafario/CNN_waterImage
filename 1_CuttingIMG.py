import cv2 as cv
import numpy as np

path_file = "D:\\PycharmProjects\\Workspace\\PdamMachineLearning\\example.jpg"
def clickingevent(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print(f"{x},{y}")

img = cv.imread(path_file)
y = 594
x = 813
h = 938 - 594
w = 1275 - 813
crop_img = img[y:y+h, x:x+w]

cv.namedWindow('image',cv.WINDOW_NORMAL)
cv.setMouseCallback('image',clickingevent)
# cv.imshow("hi",crop_img)
cv.imshow("image",img)
cv.waitKey(0)
