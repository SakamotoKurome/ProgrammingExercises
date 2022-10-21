import time
import pyautogui
# 每隔 10 秒钟稍微动一下鼠标
while True:
    pyautogui.moveRel(1, 1)
    time.sleep(10)
