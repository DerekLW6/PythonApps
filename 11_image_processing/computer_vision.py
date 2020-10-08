import cv2
import numpy as np
import pandas as pd

img = cv2.imread('.\\11_image_processing\\galaxy.jpg', 0)

# Displaying the image (After resizing to fit the screen) cut the numpy array in half and cast them as ints
resize_image = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
cv2.imshow("Galaxy", resize_image)
# cv2.imwrite("galaxy_reside.jpg", resize_image) Writing to a file
cv2.waitKey(0)
cv2.destroyAllWindows()