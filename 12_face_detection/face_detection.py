import cv2
import numpy as np
import pandas as pd
import os

# img = cv2.imread('.\\11_image_processing\\galaxy.jpg')
# Creating a Casade Object
face_cascade = cv2.CascadeClassifier('.\\12_face_detection\\Files\\harcascade_frontalface_default.xml')

# Loading the image (add 0 is for color)
img = cv2.imread('.\\12_face_detection\\Files\\news.jpg')

# Converting to Grey
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detecting multiscale
# Decreasing the image by 5% each search
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5) 

# Looping through the images/drawing rectangle
for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0), 3)

# Print returns a Numpy Array
print(type(faces))
print(faces)

# Resizing, in case it gets too big
# resized = cv2.resize(img, (img.shape[1]//2, img.shape[0]//2))

cv2.imshow("Face Highlighted", img)
cv2.waitKey(0)
cv2.destroyAllWindows()