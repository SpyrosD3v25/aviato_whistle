"""
This file is responsible for bluring faces from the images so the website does not have any issues with GDPR. 
"""

import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
from django.conf import settings
    
class Blur:
    def __init__(self): pass

    def plotImages(self, img):
        plt.imshow(img, cmap="gray")
        plt.axis('off')
        plt.style.use('seaborn')
        plt.show()
      

    def run(self, img_path):
        image = cv.imread(img_path)          
        gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        harr_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

          
        ##self.plotImages(image)
          
        face_detect = cv.CascadeClassifier(settings.MEDIA_ROOT + 'haarcascade_frontalface_default.xml')
        face_cords = harr_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=1 )
        print(face_cords)
        for x, y, w, h in face_cords:
            blur_face = image[y:y+h, x:x+w]
            blur_face = cv.GaussianBlur(blur_face,(23, 23), 30)
            image[y:y+blur_face.shape[0], x:x+blur_face.shape[1]] = blur_face

        #cv.imshow("Blur Faces", image)
        #cv.waitKey(0)

        cv.imwrite(img_path, image)
