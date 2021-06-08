#测试鼠标循环运动

import pyautogui
import random
import time


C
while True:
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)

    pyautogui.moveRel(x, y)
    time.sleep(2)


