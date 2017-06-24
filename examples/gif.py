# -*- coding: utf-8 -*-

from Myro import *
init("COM3")

list_img = []
COUNT_PHOTO = 15

for img in range(COUNT_PHOTO):
    photo = takePicture()
    list_img.append(photo)
    turnLeft(0.5, 0.1)

savePicture(list_img, 'movie_ELLIOT.gif')