import os
from PIL import Image, ImageFont, ImageDraw


def img_gen(text, bg_path, save_path):
    im = Image.open(bg_path)
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype('consola.ttf', 20)
    dr.text((220, 10), text, font=font, fill="#000000")
    im.save(save_path)

os.makedirs('imgs', exist_ok=True)
with open('urls.txt', 'r') as urls:
    count = 0
    for line in urls:
        l = line.strip()
        if l:
            save_path = 'imgs/%.3d.png' % count
            if l[0] == '🔒':
                l = l[1:]
                img_gen(l, 'secure_template.png', save_path)
            else:
                img_gen(l, 'notsecure_template.png', save_path)
            count += 1
                