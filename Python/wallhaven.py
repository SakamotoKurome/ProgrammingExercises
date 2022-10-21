import os
import requests
import random
import string
from operator import itemgetter


# 随机字符串
def get_random_string(length):
    result_str = ''.join(random.choice(
        string.ascii_letters + string.digits) for i in range(length))
    return result_str


# 获取这次api请求中最好的壁纸
def get_best_wallpaper():
    baseurl = 'https://wallhaven.cc/api/v1/search'
    apikey = ''
    categories = '111'
    purity = '111'
    sorting = 'random'
    ratios = '16x9'
    seed = get_random_string(6)
    api = f'{baseurl}?apikey={apikey}&categories={categories}\
        &purity={purity}&sorting={sorting}&ratios={ratios}&page=1&seed={seed}'
    res = requests.get(api)
    res.raise_for_status()
    wallpapers = res.json()['data']
    # 将壁纸按照favorites排序
    wallpapers = sorted(wallpapers, key=itemgetter('favorites'), reverse=True)
    for wallpaper in wallpapers:
        # 下载favorites最多且本地没有的壁纸
        if os.path.basename(wallpaper['path']) not in os.listdir(os.getcwd()):
            res = requests.get(wallpaper['path'])
            res.raise_for_status()
            f_obj = open(os.path.basename(wallpaper['path']), 'wb')
            for chunk in res.iter_content(100000):
                f_obj.write(chunk)
            f_obj.close()
            break


get_best_wallpaper()
