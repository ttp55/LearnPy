# @time:  2019/8/7 16:03
# @author: WZG
# encoding: utf-8

a = {"status":0,
     "msg":"success",
     "data":[
         {
             "symbol":"xxx",
             "a":"1998",
             "on":"00000"
         },
         {
             "symbol":"yyy",
             "a":"1997",
             "on":"00000"
         }
     ]}

b = list(a["data"])
print(b)