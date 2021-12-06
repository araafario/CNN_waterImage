import cv2 as cv
import numpy as np
import time

path_file = "D:\\PycharmProjects\\Workspace\\PdamMachineLearning\\source\\source.mp4"
cv.namedWindow("learning", cv.WINDOW_NORMAL)
cap = cv.VideoCapture(path_file)

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing import image

classifier = Sequential()
classifier.add(Conv2D(32, (3, 3), input_shape=(64, 64, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Conv2D(32, (3, 3), activation='relu'))
classifier.add(MaxPooling2D(pool_size=(2, 2)))
classifier.add(Flatten())
classifier.add(Dense(units=128, activation='relu'))
classifier.add(Dense(units=1, activation='sigmoid'))
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
classifier.load_weights('myClassifier.h5')

y = 594
x = 813
h = 938 - 594
w = 1275 - 813
c = 0
counting_washing = 0
counting_steady = 0
logging = ''
statelogging = 0
prediction = 'wait'

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret == False:
        break

    if c >= 30:
        test_image = frame[y:y + h, x:x + w]
        test_image = cv.resize(test_image, (64, 64))
        test_image = (test_image[..., ::-1])
        test_image = np.expand_dims(test_image, axis=0)
        result = classifier.predict(test_image)

        if result[0][0] == 1:
            prediction = 'State : washing'
            counting_washing += 1
            counting_steady = 0
        else:
            prediction = 'State : steady'
            counting_steady += 1
            counting_washing = 0

        if counting_washing >= 10 and statelogging == 0:
            statelogging = 1
            localtime = time.asctime(time.localtime(time.time()))
            logging = str(localtime)
        elif counting_steady >= 30 and statelogging == 1:
            statelogging = 2
            localtime = time.asctime(time.localtime(time.time()))
            logging = str(localtime)
        elif counting_steady >= 120 and statelogging == 2:
            statelogging = 0
        c = 0
        cv.rectangle(frame, (813, 594), (1275, 938), (0, 255, 0), 2)
    elif c <= 2:
        cv.rectangle(frame, (813, 594), (1275, 938), (0, 0, 255), 2)
    else:
        cv.rectangle(frame, (813, 594), (1275, 938), (0, 255, 0), 2)
    c += 1

    cv.putText(frame, prediction, (50, 1000), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2, cv.LINE_AA)
    if statelogging == 1:
        cv.putText(frame, 'Start Wash = ' + logging, (50, 1050), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)
    elif statelogging == 2:
        cv.putText(frame, 'End Wash = ' + logging, (50, 1050), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv.LINE_AA)

    cv.imshow("learning", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
