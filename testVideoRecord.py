import numpy as np
import cv2

def writeVideo():
    try:
        cap = cv2.VideoCapture(-1)
    except:
        return
    
    fps = 20.0
    width = int(cap.get(3))
    height = int(cap.get(4))
    fcc = cv2.VideoWriter_fourcc('D','I','V','X')
    
    out = cv2.VideoWriter('testcam.avi', fcc, fps, (width, height))
    print('Record Start')
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            print('Error')
            break
        
        cv2.imshow('video',frame)
        out.write(frame)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            print('Stop')
            break
        
    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
writeVideo()