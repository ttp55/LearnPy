# @time:  2019/7/9 13:28
# @author: WZG
# encoding: utf-8

import re


htp = urllib3.PoolManager()
r = htp.request('GET', 'http://192.168.243.69:18084/airportcdm/')
print(r.status)
