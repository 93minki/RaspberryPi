import numpy as np
import cv2

def CannyTest():
    
    try:
        cap = cv2.VideoCapture(-1)
    except:
        print('fail to open Cam')
        return
    
    
    while True:
        ret, frame = cap.read()
    
        grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
        edges = cv2.Canny(grayFrame, 150, 200, apertureSize = 3)
    
        cv2.imshow('Origin', frame)
        cv2.imshow('Canny Edge',edges)
    
        if cv2.waitKey(1) & 0xFF == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    

CannyTest()
    
    
        