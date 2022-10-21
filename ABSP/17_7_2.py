import os
from PIL import Image
# 扫描整个硬盘,找到这些遗忘的“照片文件夹”
for foldname, subfolders, filenames in os.walk('/'):
    numPhotoFiles = 0
    numNonPhotoFiles = 0
    for filename in filenames:
        # 照片文件必须具有文件扩展名.png 或.jpg
        if filename.lower().endswith('.png') or filename.lower().endswith('.jpg'):
            im = Image.open(os.path.join(foldname, filename))
            width, height = im.size
            # 照片文件的宽度和高度都必须大于 500 像素。
            if width > 500 and height > 500:
                numPhotoFiles += 1
            else:
                numNonPhotoFiles += 1
        else:
            numNonPhotoFiles += 1
    # “照片文件夹”。假定就是超过半数文件是照片的任何文件夹。
    if numPhotoFiles > numNonPhotoFiles:
        print(foldname)
