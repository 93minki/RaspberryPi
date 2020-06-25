import numpy as np
import cv2

def showVideo():
	try:
		print('Open Camera')
		cap = cv2.VideoCapture(-1)
	except:
		print('Fail to Open Camera')
		return
	cap.set(3, 480)
	cap.set(4, 320)

	while True:
		ret, frame = cap.read()

		if not ret:
			print('Error')
			break

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		luv = cv2.cvtColor(frame, cv2.COLOR_BGR2Luv)


		cv2.imshow('default',frame)
		cv2.imshow('Gray',gray)
		cv2.imshow('HSV',hsv)
		cv2.imshow('Luv',luv)

		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break

	cap.release()
	cv2.destroyAllWindows()

showVideo()
