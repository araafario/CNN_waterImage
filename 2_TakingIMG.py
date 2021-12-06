import cv2

path_file = "D:\\PycharmProjects\\Workspace\\PdamMachineLearning\\source\\source.mp4"
cap = cv2.VideoCapture(path_file)
i = 0
c = 0

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break

    if c >= 30:
        cv2.imwrite('Output\\Image' + str(i) + '.jpg', frame)
        c = 0

    i += 1
    c += 1


cap.release()
cv2.destroyAllWindows()