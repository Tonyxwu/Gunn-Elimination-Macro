

import cv2 as cv
from mss import mss
import numpy as np
import pyautogui
import time
def colorbox(lower,upper,topleft,bottomright,threshold):#BGR
	bound = {'top':topleft[1],'left':topleft[0],'width':bottomright[0]-topleft[0],'height':bottomright[1]-topleft[1]}
	with mss() as sct:
		img = np.array(sct.grab(bound))#grab bounding box
		img = img[:,:,:3]#slice alpha channel
		pass
	#for(lower, upper) in boundaries:
	    # creates numpy array from boundaries
	lower = np.array(lower, dtype = "uint8")
	upper = np.array(upper, dtype = "uint8")

	    # finds colors in boundaries a applies a mask
	mask = cv.inRange(img, lower, upper)
	red_pixel = cv.countNonZero(mask)
	tot_pixel = img.size
	percentage = round(red_pixel / tot_pixel, 5)
	#print (percentage)
	#cv.imshow('screen', np.array(img))
	#cv.waitKey(0)
	if percentage > threshold:
		return True#colors are true
	else:
		return False#colors are not true
	#return percentage
start = int(input('what number r u on?'))
pyautogui.PAUSE = 0.04
time.sleep(4)
increment = 0
totalDelta = 0
for i in range(start,100000):
	saved = time.perf_counter()
	number = str(100000-i)
	if len(number) < 5:#if it is not big enough
		number = '0'*(5-len(number)) + number

	pyautogui.press('a')
	pyautogui.keyUp('ctrl')
	pyautogui.write(number)
	pyautogui.press('enter')

	while True:
		if colorbox([0,0,0],[0,0,0],[1283,788],[1471,1089],0.001):#keep looking
			break



	deltaT = time.perf_counter()-saved
	totalDelta += deltaT
	increment += 1
	
	print ("Time per match:", totalDelta / increment, "Total matches in session:", increment, "Current search value:",i)