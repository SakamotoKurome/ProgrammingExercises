import requests
import bs4
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s- %(message)s')

# 下载给定网页
dest_url = 'https://www.bing.com/search?q=e'
res = requests.get(dest_url)
res.raise_for_status()
# 找到所有 a 标签
soup = bs4.BeautifulSoup(res.text, features="html.parser")
elems = soup.select('a')
# 下载标签对应的网页,根据状态码找到所有坏链接
for elem in elems:
    url = elem.get('href')
    if str(url).startswith('http'):
        res = requests.get(url)
        if (res.status_code == requests.codes.not_found):
            print(url)
