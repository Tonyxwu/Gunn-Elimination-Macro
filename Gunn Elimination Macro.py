import pyautogui
import time

start = int(input('what number are you on?'))
pyautogui.PAUSE = 0.04
time.sleep(4)
increment = 0
totalDelta = 0
for i in range(start,100000):
	saved = time.perf_counter()
	number = str(i)
	if len(number) < 5:#if it is not big enough
		number = '0'*(5-len(number)) + number
	#pyautogui.keyDown('ctrl')
	pyautogui.press('a')
	pyautogui.keyUp('ctrl')
	pyautogui.write(number)
	pyautogui.press('enter')
	pyautogui.keyDown('ctrl')
	pyautogui.press('tab')


	deltaT = time.perf_counter()-saved
	totalDelta += deltaT
	increment += 1
	
	print ("Time per match:", totalDelta / increment, "Total matches in session:", increment, "Current search value:",i)