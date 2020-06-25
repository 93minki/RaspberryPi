__author__= '93minki@taeha.co.kr'

import numpy as np
import cv2

def transform():
    img = cv2.imread('images/sudoku.jpg')
    h, w = img.shape[:2]
    
    pts1 = np.float32([[50, 50], [200, 50], [20, 200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
    
    M = cv2.getAffineTransform(pts1, pts2)
    
    img2 = cv2.warpAffine(img, M, (w, h))
    
    cv2.imshow('original', img)
    cv2.imshow('Affine-Transform', img2)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
transform()