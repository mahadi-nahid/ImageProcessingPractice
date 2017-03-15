# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:39:43 2017

@author: NAHID
"""

import numpy as np
import PIL

#Using mathplotlib


from matplotlib import pyplot as plt

img = np.asarray(PIL.Image.open('mdb001.pgm'))

#img = cv2.imread('mdb001.pgm',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()  

print (img.shape)




imgarr = np.array(img) 

print (imgarr)

np.savetxt('test1.out', imgarr.astype(int), fmt='%i', delimiter=",")

