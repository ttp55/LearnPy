# @Time : 2020/10/29 10:56
# @Author : WZG
# --coding:utf-8--

import re

str = "123456 'sdf' 3 /*- + i d DS F sd0of 15345678911 _  'edfds' "

print(re.findall(r'\d', str)) # 所有数字
print(re.findall(r'\D', str)) # 任意非数字
print(re.findall(r'\d{11}', str)) # 11位数字

print(re.findall(r'\w', str)) # 任意单个数字 字母 下划线
print(re.findall(r'\W', str)) # 与w相反

print(re.findall(r'\s', str)) # 任意空白符
print(re.findall(r'\S', str)) #任意非空白符

print(re.findall(r'\r', str)) #回车符
print(re.findall(r'\n', str)) #换行符
print(re.findall(r'\t', str)) #制表符
print('\d?', re.findall(r'\d?', str)) #0次到1次
print(re.findall(r'\d+', str)) #1到多次
print(re.findall(r'\d*', str)) #0到多次
print(re.findall(r'\d{1}', str)) #出现1次
print(re.findall(r'\d{1,}', str)) #至少出现1次
print(re.findall(r'\d{2,3}', str)) #出现2到3次

print(re.findall(r'[aeiou]', str)) #中括号内任意单个元素
print(re.findall(r'[a-z]', str)) #按ASCII表a到Z
print(re.findall(r'[^df]', str)) #取反
print(re.findall(r'1|d', str)) #1或d

print(re.findall(r'1[3-9]\d{9}', str)) #首位1，二位是3到9，其余9位任意数字

print(re.findall(r'1*', str)) #贪婪匹配
print(re.findall(r'1+', str))
print(re.findall(r'1*?', str)) #非贪婪
print(re.findall(r'\'.+\'', str)) #贪婪
print(re.findall(r'\'.+?\'', str)) #非贪婪

print(re.findall(r'xy{1,3}z', 'xyyz')) #匹配到第三个Y时回溯
print(re.findall(r'xy{1,3}?z', 'xyyz'))# 匹配到第二个Y时回溯
# print(re.findall(r'xy{1,3}+yz', 'xyyz')) 目前python不支持独占模式

# 提取出文章中所有的单词 其中 the little cat 需要看成一个单词
print(re.findall(r'''\w+|“[^”]*”''', 'we found “the little cat” is in the hat, we like “the little cat”'))

print(re.findall(r'\d{18}|\d{15}', '123456789123456 123456789123456789'))

print(re.findall(r'\d{15}(?:\d{3})?', '123456789123456 123456789123456789'))


# 分组 替换
print(re.findall(r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2})', '2020-05-10 20:23:05'))
print(re.findall(r'((\d{4})-(\d{2})-(\d{2})) ((\d{2}):(\d{2}):(\d{2}))', '2020-05-10 20:23:05'))
r1 = r'((\d{4})-(\d{2})-(\d{2})) ((\d{2}):(\d{2}):(\d{2}))'
r2 = r"日期\1 时间\5 \2年\3月\4日 \6时\7分\8秒"
print(re.sub(r1, r2, '2020-05-10 20:23:05'))

str1 = 'the little cat cat is in the hat hat, we like it.'

print(re.sub(r'(\w+)(\s\1)+', r'\1', str1))

str2 = 'cat cat' \
       'CAT Cat' \
       'Cat cat' \
       'Cat Cat' \
       'CAT CAT'

print(re.findall(r'(?i)cat', str2)) # 不区分大小写

print(re.findall(r'(?i)(cat) \1', str2))


print(re.findall(r'(cat) \1', str2, re.IGNORECASE))

print(re.findall(r'(?s).+', str2))

print(re.findall(r'[\w\W]', str2))

print(re.findall(r'^the|.$', str1))#^匹配整个字符串的开头，$ 匹配整个字符串的结尾

print(re.findall(r'(?m)^the|.$', str1))

str3 = '<heaD>' \
       '    <title>dddd</title>' \
       '</head>'
print(re.findall(r'(?si)<head>.*<\/head>', str3))

str4 = 'tom asked me if I would go fishing with him tomorrow.'

print(re.sub(r'\btom\b', 'jerry', str4)) #断言




