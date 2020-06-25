import numpy as np
import cv2

def DoCaptureImage():
    try:
        cap = cv2.VideoCapture(-1)
    except:
        print('Error')
        return
    
    while True:
        
        ret, frame = cap.read()
        
        cv2.imshow("Capture Image",frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('a'):
            print('capture')
            cv2.imwrite('images/img.jpg',frame)
        elif key == 27:
            break
        
    
    cap.release()
    cv2.destroyAllWindows()
    

DoCaptureImage()
    