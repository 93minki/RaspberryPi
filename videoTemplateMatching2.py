import numpy as np
import cv2

drawing = False
ix, iy = -1, -1

def onMouse(event, x, y, flags, param):
    global ix, iy, drawing
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.rectangle(param, (ix, iy), (x, y), (0, 255, 0), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(param, (ix, iy), (x, y), (0, 255, 0), -1)
    
        

def OnVideoMatching():
    try:
        cap = cv2.VideoCapture(-1)
    except:
        print('Error')
        return
    
    ret, frame = cap.read()
    cv2.namedWindow('streaming')
    cv2.setMouseCallback('streaming', onMouse, param = frame)
    
    while True:
        
        ret, frame = cap.read()
        

        cv2.imshow('streaming', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('a'):
            
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
        
        
        
#         if dst is not None:
#             print('res is not None')
#             cv2.imshow('template',dst)
#         else:
#             print('res is None')
#             cv2.imshow('template',frame)
            
    
        k=cv2.waitKey(1)&0xFF
        if k==27:
            print('Stop')
            break
        
        
    cap.release()
    cv2.destroyAllWindows()
    
#OnVideoMatching()

col, width, row, height = -1, -1, -1, -1
frame = None
frame2 = None
inputmode = False
rectangle = False
trackWindow = None
roi_hist =None

def onMouse(event, x, y, flags, param):
    global col, width, row, height, frame, frame2, inputmode
    global rectangle, roi_hist, trackWindow
    
    if inputmode:
        if event == cv2.EVENT_LBUTTONDOWN:
            rectangle = True
            col, row = x, y
        elif event == cv2.EVENT_MOUSEMOVE:
            if rectangle:
                frame = frame2.copy()
                cv2.rectangle(frame, (col, row), (x, y), (0, 255, 0), 2)
                cv2.imshow('frame', frame)
                
        elif event == cv2.EVENT_LBUTTONUP:
            inputmode = False
            rectangle = False
            cv2.rectangle(frame, (col, row), (x, y), (0, 255, 0), 2)
            height, width = abs(row-y), abs(col-x)
            trackWindow = (col, row, width, height)
            roi = frame[row:row+height, col:col+width]
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
            roi_his = cv2.calcHist([roi], [0], None, [180], [0, 180])
            cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
            
        return
    
def camShift():
    global frame, frame2, inputmode, trackWindow, roi_hist
    
    try:
        cap = cv2.VideoCapture(-1)
    except Exception as e:
        print(e)
        return
    
    ret, frame = cap.read()
    
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', onMouse, param=(frame, frame2))
    
    termination = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if trackWindow is not None:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
            ret, trackWindow = cv2.meanShift(dst, trackWindow, termination)
            
            x, y, w, h = trackWindow
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
        cv2.imshow('frame', frame)
        
        k = cv2.waitKey(60) & 0xFF
        if k == 27:
            break
        
        if k == ord('i'):
            print('Select Area for CamShift and Enter a Key')
            inputmode = True
            frame2 = frame.copy()
            
            while inputmode:
                cv2.imshow('frame', frame)
                cv2.waitKey(0)
                
    cap.release()
    cv2.destroyAllWindows()
    
camShift()
                
    
