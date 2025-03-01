#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@文件    :__init__.py
@说明    :
@时间    :2025/03/01 13:17:35
@作者    :Akira_TL
@版本    :1.0
"""

from PIL import Image
import glob, os

if __name__ == "__main__":
    # 读取图片
    picture_document_path = input("请输入背景图片文件夹：")
    former_img_path = input("请输入前景图片路径：")
    output_path = input("请输入输出图片文件夹：")
    former = Image.open(former_img_path)
    for file in glob.glob(picture_document_path + "/**/*.png", recursive=True):
        background = Image.open(file)
        former_tmp = former.resize((background.size[0], background.size[1]))
        background.paste(former_tmp, (0, 0), former_tmp)
        file_output_path = file.replace(picture_document_path, output_path)
        if not os.path.exists(os.path.dirname(file_output_path)):
            os.makedirs(os.path.dirname(file_output_path), exist_ok=True)
        print(f"导出文件: {file_output_path}")
        background.save(file.replace(picture_document_path, output_path))
