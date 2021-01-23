import numpy as np
import cv2

cap = cv2.VideoCapture("/dev/video0")
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

while(True):    
    # Capture frame-by-frame    
    ret, frame = cap.read()    
    
    # Display the resulting frame    
    # cv2.imshow('preview',frame)    
    
    #gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    #cv2.imshow('frame', gray)

    cv2.imshow('frame', frame)
    
    #Waits for a user input to quit the application    
    if cv2.waitKey(1) & 0xFF == ord('q'):    
        break
    
cap.release()
cv2.destroyAllWindows()