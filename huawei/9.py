# @Time : 2021/4/27 15:09
# @Author : WZG
# --coding:utf-8--
#!/usr/bin/python
# -*- coding:utf-8 -*-

# ********* 转换方法介绍 *********
# 将需要转换的数字从右向左，每4位分成一个section，如:24530467103，将该数字拆分后，得到:
# 245 3046 7103 （245亿3046万7103）
# 对拆分后的数字先按照section进行数字到汉字的转换，然后添加数值单位，如:仟，佰，拾，处理结束后可以得到转换后的序列。
# 对section处理结束后，再对每个section进行单位的追加。如：兆、亿、万。
# 这里需要注意一些特殊情况，如：section中连续出现0，最后一个数字为0等。

DEBUG = True

upper = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
decimal_unit = ["角", "分", "厘", "毫"]
section_unit = ["万", "亿", "兆"]
count_unit = ["拾", "佰", "仟"]

def dbg_print(s):
  if DEBUG:
    print(s)

def split_num(num):
  num_list = []
  if (len(num) <= 4):
    num_list.append(num)
    return num_list
  while (len(num)):
    if (len(num) <= 4):
      num_list.append(num)
      num_list.reverse()
      return num_list
    sec = num[-4:]
    num_list.append(sec)
    num = num[:-4]

# 处理小数部分，只支持4位，多于4位，四舍五入。
def convert_dec(num):
  result = ""
  count = 0
  dbg_print(num)
  for i in num:
    n = int(i)
    if (0 != n):
      result += upper[n]
      result += decimal_unit[count]
    count += 1
  dbg_print(result)
  return result

# 处理整数部分
def convert_int(num):
  section_list = split_num(num)
  dbg_print(num)
  dbg_print(section_list)
  result = ""
  sec_index = len(section_list) - 2
  for item in section_list:
    index = len(item) - 2
    # 统计连续出现的数字0的个数。
    flag = 0
    # 计算遍历过的item中的字符数。
    count = 0
    # 对每个section进行处理，得到数字对应的汉字。
    for i in item:
      n = int(i)
      if (0 == n):
        flag += 1
      else:
        flag = 0
      # 用来区分section的最后一位为0的情况
      if (count != len(item)-1):
        # 该位置的数字为0，并且它的下一个数字非0。
        if ((flag >= 1) and ('0' != item[count+1])):
          result += upper[n]
        elif (0 != n):
          result += upper[n]
      else:
        # section的最后一个数字非0的情况。
        if (0 != n):
          result += upper[n]
      # 最后一个数字以及数字为0时，都不需要添加单位。
      if ((index >= 0) and (0 != n)):
        result += count_unit[index]
      index += 1
      count += 1
    if (sec_index >= 0 and flag != count):
      result += section_unit[sec_index]
    dbg_print(result)
    sec_index -= 1
  result = result.replace("壹拾", "拾")
  result += "元"
  return result

# 转换函数
def convert(num):
  result = ""
  num = round(float(num), 4)
  integer,decimal = str(num).split('.')
  result_int = convert_int(integer)
  result_dec = convert_dec(decimal)

  if (len(result_dec) == 0):
    result = result_int = result_int + "整"
  else:
    result = result_int + result_dec
  return result
