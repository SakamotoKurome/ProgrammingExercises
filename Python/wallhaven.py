import os
import requests
import random
import string
from operator import itemgetter
import pprint
import time
import sys
import dbus


# 随机字符串
def get_random_string(length):
    result_str = ''.join(random.choice(
        string.ascii_letters + string.digits) for i in range(length))
    return result_str


class WallhavenAPI:
    def __init__(self,
                 baseurl='https://wallhaven.cc/api/v1/search',
                 apikey='',
                 categories='111',
                 purity='111',
                 sorting='random',
                 ratios='16x9'):
        self.baseurl = baseurl
        self.apikey = apikey
        self.categories = categories
        self.purity = purity
        self.sorting = sorting
        self.ratios = ratios
        self.seed = get_random_string(6)

    def get_url(self):
        if self.apikey != '':
            return f'{self.baseurl}?\
                apikey={self.apikey}&\
                    categories={self.categories}&\
                        purity={self.purity}&\
                            sorting={self.sorting}&\
                                ratios={self.ratios}&\
                                    page=1&\
                                        seed={self.seed}'
        else:
            return f'{self.baseurl}?\
                categories={self.categories}&\
                    purity={self.purity}&\
                        sorting={self.sorting}&\
                            ratios={self.ratios}&\
                                page=1&seed={self.seed}'


# 设置 Gnome 壁纸
def set_gnome_wallpaper(wallpaper_name):
    os.system(
        f"/usr/bin/gsettings set org.gnome.desktop.background \
            picture-uri file://{os.path.realpath(wallpaper_name)}")
    os.system(
        f"/usr/bin/gsettings set org.gnome.desktop.background \
            picture-uri-dark file://{os.path.realpath(wallpaper_name)}")


# 设置 KDE 壁纸
def setwallpaper(filepath, plugin='org.kde.image'):
    jscript = """
    var allDesktops = desktops();
    print (allDesktops);
    for (i=0;i<allDesktops.length;i++) {
        d = allDesktops[i];
        d.wallpaperPlugin = "%s";
        d.currentConfigGroup = Array("Wallpaper", "%s", "General");
        d.writeConfig("Image", "file://%s")
    }
    """
    bus = dbus.SessionBus()
    plasma = dbus.Interface(bus.get_object(
        'org.kde.plasmashell', '/PlasmaShell'), dbus_interface='org.kde.PlasmaShell')
    plasma.evaluateScript(jscript % (plugin, plugin, filepath))


def set_kde_wallpaper(wallpaper_name):
    setwallpaper(os.path.realpath(wallpaper_name))


def download_wallpaper(wallpaper_url):
    print(f'Target: {wallpaper_url}')
    res = requests.get(wallpaper_url, proxies=proxies)
    res.raise_for_status()
    total_size = int(res.headers.get('content-length'))  # bytes
    chunk_size = 102400  # 102400 bytes = 100 KB
    wallpaper_name = os.path.basename(wallpaper_url)
    f_obj = open(wallpaper_name, 'wb')
    for i, chunk in enumerate(res.iter_content(chunk_size=chunk_size)):
        f_obj.write(chunk)
        c = i * chunk_size / total_size * 100
        sys.stdout.write(f"\r{round(c)}%")
        time.sleep(.1)
        sys.stdout.flush()
    sys.stdout.write('\r100%\n')
    sys.stdout.flush()
    f_obj.close()
    set_gnome_wallpaper(wallpaper_name)
    set_kde_wallpaper(wallpaper_name)


# 获取某页 favorites 最多的壁纸
def get_best_wallpaper():
    res = requests.get(WallhavenAPI().get_url(), proxies=proxies)
    res.raise_for_status()
    wallpaper_metadatas = res.json()['data']
    # 将壁纸按照favorites排序
    wallpaper_metadatas = sorted(wallpaper_metadatas,
                                 key=itemgetter('favorites'), reverse=True)
    for wallpaper_metadata in wallpaper_metadatas:
        # 下载favorites最多且本地没有的壁纸
        wallpaper_url = wallpaper_metadata['path']
        if os.path.basename(wallpaper_url) not in os.listdir(os.getcwd()):
            download_wallpaper(wallpaper_url)
            break


proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890',
}
get_best_wallpaper()
