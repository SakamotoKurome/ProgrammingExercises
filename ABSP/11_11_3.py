from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox()
# 打开游戏页面
browser.get('https://play2048.co/')
# 不断发送：上、右、下、左
elem = browser.find_element(By.TAG_NAME, 'html')
for i in range(100):
    elem.send_keys(Keys.UP)
    elem.send_keys(Keys.RIGHT)
    elem.send_keys(Keys.DOWN)
    elem.send_keys(Keys.LEFT)
    print(i)
