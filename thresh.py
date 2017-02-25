# Втора домашна работа по Обработка на слика
#
# Марко Манчов - 151211
import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse
import glob


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,	help = "Path to the directory that contains the images to be indexed")
args = vars(ap.parse_args())

i = 1

for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	img = cv2.imread(imagePath,0)
	ret, thresh = cv2.threshold( img, 115, 255, cv2.THRESH_BINARY )
	cv2.imwrite("database-thresh/img"+str(i)+".jpg",thresh)
	i+=1	
