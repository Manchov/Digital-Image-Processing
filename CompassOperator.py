#Прва домашна работа по Обработка на слика
#Детекција на рабови со Компас операторот. Функија како влез прима слика, врши детекција на робови и ја прикажува сликата со детектирани рабови
#Марко Манчов - 151211

import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

#Читање на влезни аргументи/слика
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

img = cv2.imread(args["image"])
img = np.float32(img)

#Матрица - Запад
sw = np.array(([1,0,-1],[1,0,-1],[1,0,-1]), dtype="float32")
imgsw = cv2.filter2D(img,-1,sw) 
imgsw = abs(imgsw)
imgsw = imgsw / np.amax(imgsw[:])

#Матрица - Југ
ss = np.array(([1,1,1],[0,0,0],[-1,-1,-1]), dtype="float32")
imgss = cv2.filter2D(img,-1,ss) 
imgss = abs(imgss)
imgss = imgss / np.amax(imgss[:])

#Матрица - Север
sn = np.array(([-1,-1,-1],[0,0,0],[1,1,1]), dtype="float32")
imgsn = cv2.filter2D(img,-1,sn) 
imgsn = abs(imgsn)
imgsn = imgsn / np.amax(imgsn[:])

#Матрица - Исток
se = np.array(([-1,0,1],[-1,0,1],[-1,0,1]), dtype="float32")
imgse = cv2.filter2D(img,-1,se) 
imgse = abs(imgse)
imgse = imgse / np.amax(imgse[:])

#Матрица - СевероЗапад
swn = np.array(([1,1,0],[1,0,-1],[0,-1,-1]), dtype="float32")
imgswn = cv2.filter2D(img,-1,swn) 
imgswn = abs(imgswn)
imgswn = imgswn / np.amax(imgswn[:])

#Матрица - ЈугоЗапад
sws = np.array(([0,-1,-1],[1,0,-1],[1,1,0]), dtype="float32")
imgsws = cv2.filter2D(img,-1,sws) 
imgsws = abs(imgsws)
imgsws = imgsws / np.amax(imgsws[:])

#Матрица - СеверноИсток
sen = np.array(([0,1,1],[-1,0,1],[-1,-1,0]), dtype="float32")
imgsen = cv2.filter2D(img,-1,sen) 
imgsen = abs(imgsen)
imgsen = imgsen / np.amax(imgsen[:])

#Матрица - ЈугоИсток
ses = np.array(([-1,-1,0],[-1,0,1],[0,1,1]), dtype="float32")
imgses = cv2.filter2D(img,-1,ses) 
imgses = abs(imgses)
imgses = imgses / np.amax(imgses[:])

#Спојување на сликите и прикажување на резултатот
edgeSum1 = cv2.add(np.power(imgsw,2), np.power(imgss,2))
edgeSum2 = cv2.add(np.power(imgse,2),np.power(imgsn,2))
edgeSum3 = cv2.add(np.power(imgses,2),np.power(imgsen,2))
edgeSum4 = cv2.add(np.power(imgses,2),np.power(imgsen,2))
edgeSum12 = cv2.add(edgeSum1,edgeSum2)
edgeSum34 = cv2.add(edgeSum3,edgeSum4)
edgeSum = cv2.add(edgeSum12,edgeSum34)

ret,thresh = cv2.threshold(edgeSum,0.05,1,cv2.THRESH_BINARY)

cv2.imshow("image",thresh)
cv2.waitKey(0)
