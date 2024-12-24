# @Time : 2024/12/24 15:41
# @Author : WZG
# --coding:utf-8--
from PIL import Image
import pytesseract
import cv2
import numpy as np
import re

def chuli01():
    scale_factor = 2
    img = Image.open('E://img/code1.png')
    img = img.resize((int(img.width * scale_factor), int(img.height * scale_factor)))
    img = img.convert('L')

    threshold = 130
    img = img.point(lambda x: 0 if x < threshold else 255, '1')

    kernel = np.ones((2, 2), np.uint8)
    print(type(np.array(img)))
    img = cv2.morphologyEx(np.array(img), cv2.MORPH_OPEN, kernel)
    img = Image.fromarray(img)

    return img