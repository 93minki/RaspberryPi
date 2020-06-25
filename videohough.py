import numpy as np
import cv2

def hough(thr, frame):
    
    imgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(imgray, 50, 150, apertureSize = 3)
    
    lines = cv2.HoughLines(edges, 1, np.pi/180, thr)
    
    for line in lines:
        r, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * r
        y0 = b * r
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * a)
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * a)
        
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
    
def phough(thr, minLineLength, maxLineGap):
    img = cv2.imread('images/sudoku.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(imgray, 50, 150, apertureSize = 3)
    
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, thr, minLineLength, maxLineGap)
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        
    cv2.imshow('res',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def init(thr, minLineLength, maxLineGap):
    
    try:
        cap = cv2.VideoCapture(-1)
    except:
        print('Error')
        return
    
    while True:
        ret, hough = cap.read()
        ret, houghP = cap.read()
        
        grayhough = cv2.cvtColor(hough, cv2.COLOR_BGR2GRAY)
        grayhoughP = cv2.cvtColor(houghP, cv2.COLOR_BGR2GRAY)
        
        houghedges = cv2.Canny(grayhough, 50, 150, apertureSize = 3)
        houghPedges = cv2.Canny(grayhoughP, 50, 150, apertureSize = 3)
        
        lines = cv2.HoughLines(houghedges, 1, np.pi/180, thr)
       
        
        if lines is not None:
            for line in lines:
                r, theta = line[0]
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a * r
                y0 = b * r
                x1 = int(x0 + 1000 * (-b))
                y1 = int(y0 + 1000 * a)
                x2 = int(x0 - 1000 * (-b))
                y2 = int(y0 - 1000 * a)
                
                cv2.line(hough,(x1, y1), (x2, y2), (0, 255, 0), 1)
            cv2.imshow('hough',hough)
        else:
            cv2.imshow('hough',hough)
        
        linesP = cv2.HoughLinesP(houghPedges, 1, np.pi/180, thr, minLineLength, maxLineGap)
        
        if linesP is not None:
            for line in linesP:
                x1, y1, x2, y2 = line[0]
                cv2.line(houghP, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            cv2.imshow('houghP',houghP)
        else:
            cv2.imshow('houghP',houghP)
        
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
init(140, 100, 10)
        
    