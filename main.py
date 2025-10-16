import pyautogui
import cv2
import pytesseract
from mss import mss
import numpy as np
import time
import random



def find_and_click(path):
    with mss() as sct:
        sct.shot()
        img = cv2.imread('monitor-1.png', cv2.IMREAD_COLOR)

    template = cv2.imread(path, cv2.IMREAD_COLOR)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)

    threshold = 0.8
    h, w = template.shape[:2]
    x, y = max_loc
    top_left = (x, y)
    bottom_right = (x + w, y + h)

    img_display = img.copy()
    cv2.rectangle(img_display, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(img_display, f"{max_val:.2f}", (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Detection", img_display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    if max_val >= threshold:
        center = (x + w//2, y + h//2)
        print(f"{path} element at:", center, f"(score={max_val:.2f})")
        pyautogui.moveTo(center)
        time.sleep(random.uniform(2.25, 5.23))
        pyautogui.click()
    else:
        print(f"{path}: not found (score={max_val:.2f})")

find_and_click('assets/market.png')
find_and_click('assets/dragons.png')