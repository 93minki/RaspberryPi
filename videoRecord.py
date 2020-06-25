import numpy as np
import cv2

def writeVideo():
	try:
		print('Operating Camera')
		cap = cv2.VideoCapture(-1)
	except:
		print('Fail To Operate Camera')
		return

	fps = 30.0
	width = int(cap.get(3))
	height = int(cap.get(4))
	fcc = cv2.VideoWriter_fourcc('D','I','V','X')

	out = cv2.VideoWriter('mycam.avi',fcc,fps,(width,height))
	print('Recording Start')

	while True:
		ret, frame = cap.read()

		if not ret:
			print('Error to Read Video')
			break
		cv2.imshow('video',frame)
		out.write(frame)

		k=cv2.waitKey(1)&0xFF
		if k==27:
			print('Stop Recording')
			break

	cap.release()
	out.release()
	cv2.destroyAllWindows()

writeVideo()
