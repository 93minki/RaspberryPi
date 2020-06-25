import numpy as np
import cv2

drawing = False
ix, iy = -1, -1
def onMouse(event, x, y, flags, param):
    global drawing, ix, iy

    if event == cv2.EVENT_LBUTTONDOWN:
      
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
     
        if drawing:
            param = cv2.rectangle(param, (ix, iy), (x, y), (0, 255, 0), 1)
            
    elif event == cv2.EVENT_LBUTTONUP:
      
        drawing = False
        param = cv2.rectangle(param, (ix, iy), (x, y), (0, 255, 0), 1)
        
        w = x - ix
        h = y - iy
        
        dst = param[iy : iy + h, ix : ix + w]
        
        cv2.imshow('cut', dst)
        cv2.imwrite('testimg.jpg',dst)
    

def init():
    
    cap = cv2.VideoCapture(-1)
    
    while True:
        
        ret, frame = cap.read()
        cv2.imshow('param',frame)
        cv2.setMouseCallback('param', onMouse, param = frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
        elif cv2.waitKey(1) &0xFF == ord('q'):
            ret, frame = cap.read()
            src = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            templit = cv2.imread('testimg.jpg',cv2.IMREAD_GRAYSCALE)
            dst = src.copy()
            
            result = cv2.matchTemplate(src, templit, cv2.TM_SQDIFF_NORMED)
            
            minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
            x, y = minLoc
            h, w = templit.shape
            
            dst = cv2.rectangle(dst,(x,y),(x+w,y+h),(0,0,255),1)
            cv2.imshow("dst",dst)
    
            
            print('template Matching')
            
    
    cap.release()
    cv2.destroyAllWindows()
    
    
    
init()