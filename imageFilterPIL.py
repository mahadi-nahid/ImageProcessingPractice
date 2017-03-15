# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 00:03:41 2017

@author: NAHID
"""

from PIL import Image, ImageFilter
#Read image
im = Image.open( 'nahid.JPG' )
#Display image
im.show()

size = 128, 128 

#Applying a filter to the image
im_sharp = im.filter( ImageFilter.EDGE_ENHANCE_MORE )


            
#Saving the filtered image to a new file
im_sharp.save( 'nahid_edges_enhance_more.jpg', 'JPEG' )

#image resizing 
im.thumbnail(size, Image.ANTIALIAS)
im.save('nahid_small.jpg', "JPEG")


#Splitting the image into its respective bands, i.e. Red, Green,
#and Blue for RGB
r,g,b = im_sharp.split()

print (r, g, b)
#Viewing EXIF data embedded in image
exif_data = im._getexif()
exif_data


