# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 18:28:03 2017

@author: NAHID
"""

import numpy as np
import cv2

#Displaying an Image using opencv

#img = cv2.imread('nahid.jpg',0)
img = cv2.imread('mdb001.pgm', 0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('nahidgray.png',img)
    cv2.destroyAllWindows()



#Using mathplotlib


from matplotlib import pyplot as plt

img = cv2.imread('mdb001.pgm',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()  

print img.shape

imgarr = np.array(img) 

#print imgarr

imgdata = imgarr.astype(int)

print imgdata

#np.savetxt('test.out', imgarr, delimiter=',')

np.savetxt('test.out', imgarr.astype(int), fmt='%i', delimiter=",")

