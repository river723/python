# 得到gt和challenge
# https://www.geetest.com/demo/gt/register-slide?t=1723790919478

from PIL import Image
import numpy as np
import requests

res = requests.get('https://static.geetest.com/pictures/gt/d401d55fc/bg/0c7243c39.webp')
with open('bg.png', 'wb') as f1:
    f1.write(res.content)




def process_image(t_path, e_path):
    # 定义一个数组，用于存储图像片段的顺序
    order = [
        39, 38, 48, 49, 41, 40, 46, 47, 35, 34, 50, 51, 33, 32, 28, 29, 27, 26, 36, 37, 31, 30, 44, 45, 43, 42,
        12, 13, 23, 22, 14, 15, 21, 20, 8, 9, 25, 24, 6, 7, 3, 2, 0, 1, 11, 10, 4, 5, 19, 18, 16, 17
    ]

    # 打开图像
    t = Image.open(t_path)



    width, height = t.size
    # e = e.resize((height, 260))

    # 创建一个新的图像来存储结果
    new_img = Image.new('RGB', (260, 160))

    for i in range(52):
        x = (order[i] % 26) * 12 + 1
        y = height // 2 if order[i] > 25 else 0
        piece = t.crop((x, y, x + 10, y + height // 2))
        new_x=(i % 26) * 10;
        new_y=height // 2 if i > 25 else 0;
        new_img.paste(piece, (new_x, new_y))

    # 保存结果图像
    new_img.save('bg1.png')

# 示例调用
process_image('bg.png', 'bg1.png')



#
# def process_image(source_image_path, output_image_name):
#     # Open the source image
#     source_image = Image.open(source_image_path)
#
#     # Create a new canvas with the same size as the source image
#     canvas = Image.new("RGB", source_image.size)
#
#     # Call the decryptAndDraw function to process the image
#     decrypt_and_draw(canvas, source_image)
#
#     # Convert the canvas to RGB mode for JPEG format
#     rgb_canvas = canvas.convert("RGB")
#
#     # Save the processed image
#     rgb_canvas.save(output_image_name)
#
# process_image("bg.png", "bg1.png")
