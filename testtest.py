import numpy as np
import cv2
import time

from picamera import PiCamera
from time import sleep



def init():

    camera = PiCamera()
    
    while True:
        cam1 = camera.start_preview()
        cam2 = camera.start_preview()
        
        if cam1 != cam2:
            print('gg')
    
init()

