# @Time : 2022/3/11 13:48
# @Author : WZG
# --coding:utf-8--

from ddddocr import DdddOcr

ocr = DdddOcr()
file = open('yanzhengma.jpg', 'rb')
img = file.read()
result = ocr.classification(img)
print(result)