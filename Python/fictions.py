import requests
import os
import bs4


# class Fiction:
#     def __init__(self, page_url, name, author, description):
#         self.page_url = page_url
#         self.name = name
#         self.author = author
#         self.description = description
#         self.download_url = f'http://txt.downbook.cc/TXT/{self.name}.txt'


def get_page(page_url):  # 获取某一页
    res = requests.get(page_url)
    res.raise_for_status()
    res.encoding = res.apparent_encoding
    return res.text


def get_fictions(page):  # 获取某一页中的所有小说信息
    soup = bs4.BeautifulSoup(page, features='html.parser')
    fictions = soup.select('div.lb ul li a')
    for fiction in fictions:
        fiction_name = fiction.h1.text
        fiction_author = fiction.h2.text
        if '强推' in fiction_name or '金推' in fiction_name or \
                'L泗X汐Y' in fiction_author or '书自清' in fiction_author or \
                '君sola' in fiction_author or '清远' in fiction_author or \
                '小吾君' in fiction_author or '黄连苦寒' in fiction_author or \
                '绝歌' in fiction_author or '沐枫轻年' in fiction_author or \
                '请君莫笑' in fiction_author or '八千岁' in fiction_author or \
                '雁过吾痕' in fiction_author or '时微月上' in fiction_author or \
                '问西来意' in fiction_author:
            print(fiction_name)
            download_fiction(fiction.get('href'))


def download_fiction(download_url):  # 下载该小说
    soup = bs4.BeautifulSoup(
        get_page(base_url+download_url), features='html.parser')
    abs_download_url = soup.select('div.ydxz ul a')[2].get('href')
    print(abs_download_url)
    fiction_name = os.path.basename(abs_download_url)
    if fiction_name not in os.listdir(os.getcwd()):
        res = requests.get(abs_download_url)
        res.raise_for_status()
        res.encoding = 'GBK'
        with open(fiction_name, 'w') as f:
            f.write(res.text)


# 创建并切换工作目录
work_dir = os.path.join(os.getcwd(), 'Fictions')
os.makedirs(work_dir, exist_ok=True)
os.chdir(work_dir)

# # 获取第一页与该页的小说
# base_url = 'https://sj.downbook.cc'
# first_page_url = base_url + '/TXT/list32_1.html'
# first_page = get_page(first_page_url)
# get_fictions(first_page)
# # 从第一页获取总页数
# soup = bs4.BeautifulSoup(first_page, features='html.parser')
# last_page_number = int(soup.select('div.list code a')[1].text)
# # 根据总页数获取每一页
# for i in range(1, last_page_number+1):  # 53
#     print(i)
#     page_url = f'{base_url}/TXT/list32_{i}.html'
#     page = get_page(page_url)  # 这里也可以不用获取页数，直接不断加，直到报错 404 就行
#     try:
#         get_fictions(page)
#     except:
#         print('Failded')

base_url = 'https://sj.downbook.cc'
page_number = 1
while True:
    print(page_number)
    page_url = f'{base_url}/TXT/list32_{page_number}.html'
    try:
        page = get_page(page_url)
    except requests.exceptions.HTTPError as e:
        print(e)  # 当没有下一页的时候（404），说明所有页都处理了
        break
    try:
        get_fictions(page)
    except:
        print('下载地址无效')
    page_number += 1
