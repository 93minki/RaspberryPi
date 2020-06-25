import numpy as np
import cv2

def playVideo():

	try:
		print('Play Video!')
		cap = cv2.VideoCapture('mycam.avi')
	except:
		print('Faile To Play Video')
		return

	while True:
		ret, frame = cap.read()
		cv2.imshow('Play Video',frame)

		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			print('Play Stop')
			break

	cap.release()
	cv2.destroyAllWindows()

playVideo()
