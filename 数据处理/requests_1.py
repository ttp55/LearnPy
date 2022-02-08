# @Time : 2021/8/16 14:52
# @Author : WZG
# --coding:utf-8--

import pandas as pd
import requests
import numpy as np
import re
from matplotlib import pyplot as plt
import seaborn
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
ht = re.findall(r'([a-zA-z]+://.*?)"', strhtml.text)
ht = pd.Series(ht)

# print(pd.Series(ht).to_csv('urlStr.csv'))

#seaborn.displot(ht, kde=False, rug=True)

