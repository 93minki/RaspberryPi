import numpy as np
import cv2

def showVideo():
    try:
        print(' Camera Open! ')
        cap = cv2.VideoCapture(-1)

    except:
        print(' Fail to Open Camera ')
        return

    cap.set(3, 480)
    cap.set(4, 320)

    while True:
        ret, frame = cap.read()

        if not ret:
            print('Error')
            break

        cv2.imshow('Video',frame)

        for i in range(0, 18):
            print('cap.get(',i,')',cap.get(i))

        k = cv2.waitKey(1) &0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

showVideo()
