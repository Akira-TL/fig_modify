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
import numpy as np

if __name__ == "__main__":
    # 读取图片
    background = Image.open("figs/test1.png")
    former = Image.open("figs/former.png")
    former = former.resize((background.size[0], background.size[1]))
    background.paste(former, (0, 0), former)
    background.save("figs/test_out.png")
