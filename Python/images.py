from PIL import Image
import os
import shutil
# 选择合适分辨率的图片
work_dir = os.getcwd()
passed_dir = os.path.join(work_dir, 'passed')
failed_dir = os.path.join(work_dir, 'failed')
os.makedirs(passed_dir, exist_ok=True)
os.makedirs(failed_dir, exist_ok=True)

prefer_width, prefer_height = [393, 873]


for filename in os.listdir(work_dir):
    if (filename.lower().endswith(('.png', '.jpg', 'jpeg'))):
        file = os.path.join(work_dir, filename)
        img = Image.open(file)
        width, height = img.size
        if width >= prefer_width and height >= prefer_height:
            shutil.move(file, passed_dir)
        else:
            shutil.move(file, failed_dir)
