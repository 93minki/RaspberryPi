import numpy as np
import cv2

def convex():
    img = cv2.imread('images/convexHull.JPG')
    img1 = img.copy()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cnt = contours[1]
    cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)
    check = cv2.isContourConvex(cnt)
    
    if not check:
        hull = cv2.convexHull(cnt)
        cv2.drawContours(img1, [hull], 0, (0, 255, 0), 3)
        cv2.imshow('convexHull', img1)
        
    cv2.imshow('contour', img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def convex2():
    img = cv2.imread('images/convexHull2.JPG')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cnt = contours[5]
    
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
    
    rect = cv2.minAreaRect(cnt)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    
    cv2.drawContours(img, [box], 0, (0, 255, 0), 3)
    
    cv2.imshow('rectangle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    
convex()
convex2()