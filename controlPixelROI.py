import numpy as np
import cv2

img = cv2.imread('images/screen.jpg')
cv2.imshow('original', img)

subimg = img[300:400, 350:750]
cv2.imshow('cutting',subimg)

img[300:400, 0:400] = subimg

print(img.shape)
print(subimg.shape)

cv2.imshow('modified', img)

cv2.waitKey(0)
cv2.destroyAllWindows()


#B = img.item(200, 150, 0)
#G = img.item(200, 150, 1)
#R = img.item(200, 150, 2)

#BGR = [B, G, R]

#px = img[200,150]
#print(px)
#print(BGR)

#print(img.shape)
#print(img.size)
#print(img.dtype)
