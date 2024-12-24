# @Time : 2024/12/23 13:03
# @Author : WZG
# --coding:utf-8--

import cv2 as cv
src_file = 'E://img/code1.png'

# 去噪图
blurred_file = "E://img/code2.png"
# 灰度图
gray_file = "E://img/code3.png"
# 二值化图
binary_file = "E://img/code4.png"


def chuli():
    img_src = cv.imread(src_file)
    blurred = cv.pyrMeanShiftFiltering(img_src,10, 100)
    cv.imwrite(blurred_file, blurred)

    # 灰度图
    gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    # 保存文件
    cv.imwrite(gray_file, gray)
    # 二值化处理
    t, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # t为获取的阈值
    # 保存文件
    cv.imwrite(binary_file, binary)
