import cv2
import numpy as np
import pandas as pd
import time 

video = cv2.VideoCapture(0)
a = 1

while True:
    a += 1 
    check, frame = video.read()

    cv2.imshow("Capturing", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

print(a)
video.release()
cv2.destroyAllWindows()

