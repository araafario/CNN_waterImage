import cv2 as cv
import numpy as np

cv.namedWindow("window", cv.WINDOW_NORMAL)

img = cv.imread('example.jpg')

cv.rectangle(img, (813, 594), (1275, 938), (0, 255, 0), 2)
cv.putText(img, 'Washing', (50, 1000), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv.LINE_AA)
cv.imshow("window", img)

cv.waitKey(0)
cv.destroyAllWindows()
