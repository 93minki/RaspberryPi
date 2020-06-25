import numpy as np
import cv2

def OnVideoMatching():
    try:
        cap = cv2.VideoCapture(-1)
    except:
        print('Error')
        return
    
    
    while True:
        
        ret, frame = cap.read()
        
        
        cv2.waitKey(1) & 0xFF == ord('a'):
            
            cv2.imwrite('images/compareImage.jpg',frame)
            
            captureImage = cv2.imread('images/compareImage.jpg',cv2.IMREAD_GRAYSCALE)
            
            #grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
            tempImage = cv2.imread('images/icon.jpg', cv2.IMREAD_GRAYSCALE)
        
            ret2, dst = cap.read()
        
            res = cv2.matchTemplate(grayFrame, tempImage, cv2.TM_CCORR_NORMED)
        
        
        
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(res)
        
            x, y = minLoc
            h, w = tempImage.shape
        
            dst = cv2.rectangle(dst, (x, y),(x + w, y + h), (0, 0, 255), 1)
        
        cv2.imshow('original', frame)
        cv2.imshow('gray',grayFrame)
        cv2.imshow('template',res)
        
        
        if dst is not None:
            print('res is not None')
            cv2.imshow('template',dst)
        else:
            print('res is None')
            cv2.imshow('template',frame)
            
    
        k=cv2.waitKey(1)&0xFF
        if k==27:
            print('Stop')
            break
        
        
    cap.release()
    cv2.destroyAllWindows()
    
OnVideoMatching()
    