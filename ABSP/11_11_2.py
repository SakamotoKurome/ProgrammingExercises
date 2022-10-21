import requests
import bs4
import os
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')


# 自己先在网页上操作一遍，然后将操作写成类似TODO的注释，最后将所有TODO实现就可以了


# 代理
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}


# 确定下载目录
dir = os.getcwd() + '/images'
os.makedirs(dir, exist_ok=True)


# 根据关键字查找图片，返回图片列表
search_url = 'https://imgur.com/search?q='
keywords = 'art'
search = search_url + keywords
logging.debug('Searching: ' + search)
res = requests.get(search, proxies=proxies)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, features="html.parser")
thumbnails = soup.select('.image-list-link img')


# 图片缩略图以 b.jpg 结尾，改为 .jpeg 即为原图
for thumbnail in thumbnails[:5]:
    original = thumbnail.get('src')
    original = 'https:' + original
    original = original.replace('b.jpg', '.jpeg')
    logging.debug('Downloading original: ' + original)

    # 下载原图
    res = requests.get(original, proxies=proxies)
    res.raise_for_status()
    f_obj = open(os.path.join(dir, os.path.basename(original)), 'wb')
    for chunk in res.iter_content(100000):
        f_obj.write(chunk)
    f_obj.close()
