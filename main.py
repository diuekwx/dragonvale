import pyautogui
import cv2
import pytesseract
from mss import mss
import numpy as np
import time

with mss() as sct:
    ss = sct.grab(sct.monitors[1])
    img = np.array(ss)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2BGR)


template = cv2.imread('assets/market.png', cv2.IMREAD_COLOR)
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
_, max_val, _, max_loc = cv2.minMaxLoc(res)

threshold = 0.8 
if max_val >= threshold:
    x, y = max_loc
    h, w = template.shape[:2]
    center = (x + w//2, y + h//2)
    print("element at:", center)
else:
    print("found")

pyautogui.moveTo(center)
time.sleep(2)
pyautogui.click()