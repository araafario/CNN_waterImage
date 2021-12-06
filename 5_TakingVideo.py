import cv2 as cv
import numpy as np

path_file = "D:\\PycharmProjects\\Workspace\\PdamMachineLearning\\source\\source.mp4"
cv.namedWindow("source", cv.WINDOW_NORMAL)
cap = cv.VideoCapture(path_file)
y = 594
x = 813
h = 938 - 594
w = 1275 - 813
c = 0

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break

    if c >= 30:
        crop_img = frame[y:y + h, x:x + w]
        cv.imshow("window", crop_img)
        c = 0

    c += 1
    cv.imshow("source", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
