import numpy as np
import cv2
import time

def calcfps(cap):
    prevTime = 0
    while True:
        ret, frame = cap.read()
        
        curTime = time.time()
        sec = curTime - prevTime
        prevTime = curTime
        
        fps = 1/(sec)
        
        print(fps)
        
        strFPS = ('FPS : %0.1f' %fps)
        
        cv2.putText(frame, strFPS, (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
        cv2.imshow('Calc FPS',frame)
        
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def init():
    try:
        print('Camera Open')
        cap=cv2.VideoCapture(-1)
    except:
        print('Fail To Open Camera')
        return
    
    #fps = 25.0
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(fps)
    width = int(cap.get(3))
    height = int(cap.get(4))
    recordFlag = False
    
    while True:
        ret, frame = cap.read()
        ret2, frame2 = cap.read()
        
        cv2.imshow('Video',frame)
        
        grayA = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
        
        diff = np.abs(cv2.subtract(grayA, grayB))
        
        s = np.std(diff)
        
        if s > 10:
            print(s,'different! Write Start!')
            
            endTime = time.time() + (10 * 1)
            
            cur = 'Video'+time.strftime('%H-%M-%S',time.localtime(time.time()))+'.avi'
            recordFlag = True
            print(cur)
            
            fcc = cv2.VideoWriter_fourcc('D','I','V','X')
            out = cv2.VideoWriter(cur, fcc, fps, (width, height))
            
            while recordFlag == True:
                ret3, frame3 = cap.read()
                out.write(frame3)
                if time.time() > endTime:
                    recordFlag = False
                    print('End')
                    out.release()
                    print(time.strftime('%H-%M-%S',time.localtime(time.time())))
                    break
                
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
init()
