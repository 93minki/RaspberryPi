import numpy as np
import cv2

def contourTest():
    
    try:
        cap = cv2.VideoCapture(-1)
    except:
        print('Fail To Open Camera')
        return
    
    while True:
        ret1, frame = cap.read()
        
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        ret2, thr = cv2.threshold(grayFrame, 127, 255, 0)
        _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        cv2.drawContours(frame, contours, -1, (0, 255, 0), 1)
        cv2.imshow('thresh', thr)
        cv2.imshow('contour', frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
contourTest()