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
            cv2.imshow('param2', param)
    elif event == cv2.EVENT_LBUTTONUP:
      
        drawing = False
        param = cv2.rectangle(param, (ix, iy), (x, y), (0, 255, 0), 1)
        
        dst = param.copy()
        roi = param[x, y]
        dst[x,y] = roi
        
        cv2.imshow('param2', param)
        cv2.imshow('cut', dst)
    

def init():
    
    cap = cv2.VideoCapture(-1)
    
    while True:
        
        ret, frame = cap.read()
        cv2.imshow('param',frame)
        cv2.setMouseCallback('param', onMouse, param = frame)
        
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    cap.release()
    cv2.destroyAllWindows()
    
    
    
init()