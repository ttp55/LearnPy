# @Time : 2021/8/16 14:52
# @Author : WZG
# --coding:utf-8--

import pandas as pd
import requests
import re

url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
ht = re.findall(r'([a-zA-z]+://.*?)"', strhtml.text)
print(pd.Series(ht).to_csv('urlStr.csv'))

