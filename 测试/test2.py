# @Time : 2019/5/15 15:25
# @Author : WZG
# --coding:utf-8--

import time

print([n ** 2 - 100 for m in range(168) for n in range(m) if (m + n) * (m - n) == 168])


print(time.strptime('2017-5-7', '%Y-%m-%d')[7])
