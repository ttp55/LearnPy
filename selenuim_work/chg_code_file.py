# @Time : 2024/12/25 13:44
# @Author : WZG
# --coding:utf-8--

import pytesseract
from PIL import Image
import os
import re


code_files = os.listdir('E://train')
for fil in code_files:
    scale_factor = 2
    img = Image.open('E://train/%s'%fil)
    img = img.resize((int(img.width * scale_factor), int(img.height * scale_factor)))
    img = img.convert('L')

    threshold = 130
    img = img.point(lambda x: 0 if x < threshold else 255, '1')
    img_str = pytesseract.image_to_string(img, config='--psm 10 --oem 3')
    img_str = re.sub(r'[^a-zA-Z0-9]', '', img_str)
    try:
        os.rename('E://train/%s' %fil, 'E://train/%s.png' %img_str)
    except:pass

