import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

photo_width = 4800
photo_height = 3200
photo = Image.open('/Users/xxr/Desktop/sydney.jpg').resize((photo_width,photo_height),Image.ANTIALIAS)
image_path = '/Users/xxr/Desktop/Photos/'

image_format = '.jpg'
image_size = 50
image_row = int(photo_height/image_size)
print('row',image_row)
image_column = int(photo_width/image_size)
print('column',image_column)
image_save_path = '/Users/xxr/Desktop/final_photo100*100.png'

image_names = [name for name in os.listdir(image_path) if os.path.splitext(name)[1] == image_format]
photos = []
for name in image_names:
    item = Image.open(image_path+name).resize((image_size,image_size),Image.ANTIALIAS)
    photos.append(item)

def image_compose():
    to_image = Image.new('RGB',(image_column*image_size,image_row*image_size))
    print(to_image.size)
    for y in range(1,image_row+1):
        print(y)
        for x in range(1,image_column+1):
            best_distance = 100000000000
            best_img = 0
            for image in photos:
                distance = 0
                for i in range(image_size):
                    for j in range(image_size):
                        image_pixel = image.getpixel((i,j))
                        photo_pixel = photo.getpixel(((x-1)*image_size+i,(y-1)*image_size+j))
                        for m in range(0,3):
                            distance = distance+ abs(image_pixel[m]-photo_pixel[m])
                if best_distance > distance:
                    best_distance = distance
                    best_img = image
            to_image.paste(best_img,((x-1)*image_size,(y-1)*image_size))
    to_image.save(image_save_path)




image_compose()


