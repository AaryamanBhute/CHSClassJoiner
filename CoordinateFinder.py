import pyautogui
import time
while(True):
	x, y = pyautogui.position()
	print("x: " + str(x))
	print("y: " + str(y))
	time.sleep(1)