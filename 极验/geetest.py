# 得到gt和challenge
# https://www.geetest.com/demo/gt/register-slide?t=1723790919478
import io

from PIL import Image
import numpy as np
import requests
import ddddocr

# 获取背景图片
res = requests.get('https://static.geetest.com/pictures/gt/09b7341fb/bg/f9e454994.webp')
with open('bg.png', 'wb') as f1:
    f1.write(res.content)


'''处理乱序背景图片'''
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

'''得到滑块图片'''
res1 = requests.get('https://static.geetest.com/pictures/gt/09b7341fb/slice/f9e454994.png')
with open('slice.png', 'wb') as f2:
    f2.write(res1.content)

#
# with open('slice.png', 'rb') as f1:
#     slice_bytes=f1.read()
# img_slice=Image.open(io.BytesIO(slice_bytes))
#
# with open('bg1.png', 'rb') as f2:
#     bg_bytes=f2.read()
# img_bg=Image.open(io.BytesIO(bg_bytes))

with Image.open('slice.png') as s_img:
    # 创建一个字节流对象
    slice_byte_stream = io.BytesIO()
    # 将图片保存到字节流中
    s_img.save(slice_byte_stream, format='PNG')
    # 获取字节流的内容
    slice_png_bytes = slice_byte_stream.getvalue()

with Image.open('bg1.png') as b_img:
    # 创建一个字节流对象
    bg1_byte_stream = io.BytesIO()
    # 将图片保存到字节流中
    b_img.save(bg1_byte_stream, format='PNG')
    # 获取字节流的内容
    bg1_png_bytes = bg1_byte_stream.getvalue()

det=ddddocr.DdddOcr(det=False,ocr=False)
res=det.slide_match(slice_png_bytes, bg1_png_bytes,simple_target=True)
# 得到滑动距离
x=res['target'][0]
print(x)