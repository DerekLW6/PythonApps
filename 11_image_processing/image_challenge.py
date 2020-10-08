import cv2
import os

directory = 'C:\\Users\\derek\\Desktop\\MIDS Program\\python_apps_udemy\\11_image_processing\image_practice'

for filename in os.listdir(directory):
    filename1 = '.\\11_image_processing\\image_practice\\' + filename
    img = cv2.imread(filename1)
    resize_image = cv2.resize(img, (100,100) )
    new_filename = "resized_" + filename
    print(new_filename)
    cv2.imwrite(new_filename, resize_image)
    