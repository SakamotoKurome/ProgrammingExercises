import os
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# 生成带有客人名字和一些鲜花装饰的288×360图像文件
save_dir = os.path.join(os.getcwd(), 'cards')
os.makedirs(save_dir, exist_ok=True)
f_obj = open('guests.txt')
guests = f_obj.readlines()
f_obj.close()
card_size = (288, 360)
# 鲜花
f_im = Image.open('pngtree.jpg')
# 缩放鲜花
f_im = f_im.resize((card_size[0], card_size[1]))
for guest in guests:
    # 图像文件
    card = Image.new('RGBA', card_size)
    card_width, card_height = card.size
    # 粘贴鲜花
    card.paste(f_im, (0, 0))
    # 写上客人名字
    draw = ImageDraw.Draw(card)
    text_width, text_height = draw.textsize(guest.strip())
    text_font = ImageFont.truetype(
        '/usr/share/fonts/truetype/DejaVuSerif-Italic.ttf', 16)
    text_color = (random.randint(0, 255), random.randint(
        0, 255), random.randint(0, 255))
    # 期望水平居中显示
    draw.text((int((card_width - text_width) / 2),
              int((card_height - text_height) / 3)), guest.strip(), fill=text_color, font=text_font)
    # 在图像的边缘添加一个黑色的矩形
    draw.line([(0, 0), (0, 360), (288, 360), (288, 0), (0, 0)],
              fill="black", width=4)
    # 保存座位卡
    card.save(os.path.join(save_dir, f'{guest}.png'))
