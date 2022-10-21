import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
# 创建下载目录
base_dir = os.path.join(os.getcwd(), '終將成為你')
os.makedirs(base_dir, exist_ok=True)
save_dir = ''
# 打开漫画首页
browser = webdriver.Firefox()
browser.get('https://www.copymanga.org/comic/zuizhongwochengleni')
sleep(2)
# 找到每一章的 url
elems = browser.find_elements(By.CSS_SELECTOR, '#default全部 a')
for elem in elems:
    episode_url = elem.get_attribute('href')
    # 创建章节目录
    episode_title = elem.get_attribute('title')
    save_dir = os.path.join(base_dir, episode_title)
    os.makedirs(save_dir, exist_ok=True)
    if episode_url.startswith('http'):
        # 打开章节
        browser.get(episode_url)
        # 加载每一页，每页大概需要按6次space键
        comicCount = browser.find_element(By.CLASS_NAME, 'comicCount')
        comicCount = int(comicCount.text)
        html = browser.find_element(By.TAG_NAME, 'html')
        for i in range(comicCount):
            for j in range(6):
                html.send_keys(Keys.SPACE)
            sleep(0.2)
        # 找到每一页的链接
        pages = browser.find_elements(
            By.CSS_SELECTOR, '.comicContent-list img')
        for i in range(len(pages)):
            page_url = pages[i].get_attribute('src')
            if page_url.endswith('webp'):
                # 下载每一页
                res = requests.get(page_url)
                f_obj = open(os.path.join(save_dir,
                                          os.path.basename(page_url)), 'wb')
                for chunk in res.iter_content(100000):
                    f_obj.write(chunk)
                f_obj.close()
browser.quit()
