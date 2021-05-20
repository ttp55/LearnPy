# @Time : 2021/5/11 15:52
# @Author : WZG
# --coding:utf-8--
import time
start = time.perf_counter()
a = [1, '2']
b = [1, 2, 3]
c = set(a + b)
if len(c) == len(b):
    print(True)
else:
    print(False)

end = time.perf_counter()
print(end-start)