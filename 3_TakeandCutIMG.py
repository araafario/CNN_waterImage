import cv2

path_file = "D:\\PycharmProjects\\Workspace\\PdamMachineLearning\\source\\Source.mp4"
cap = cv2.VideoCapture(path_file)
count = 0
i = 0
j = 0
c = 0

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break

    if c >= 15:
        y = 594
        x = 813
        h = 938 - 594
        w = 1275 - 813

        crop_img = frame[y:y + h, x:x + w]
        if 50*2 <= count < 470*2:
            state = 'washing'
            cv2.imwrite('dataset\\training_set\\washing\\' + state + str(i) + '.jpg', crop_img)
            print(state + str(i) + '.jpg')
            i += 1
        elif count < 50*2 or count >= 470*2:
            state = 'steady'
            cv2.imwrite('dataset\\training_set\\steady\\' + state + str(j) + '.jpg', crop_img)
            print(state + str(j) + '.jpg')
            j += 1
        else:
            print('wait'+str(count))
        c = 0
        count += 1

    c += 1

cap.release()
cv2.destroyAllWindows()