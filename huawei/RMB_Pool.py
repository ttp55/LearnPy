# coding:utf-8
def convert_num(x):
    zh_cn = ["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
    return(zh_cn[int(x)])

def convert_yuan(x):
    zh_cn = ["元","拾","佰","仟","万","拾","佰","仟","亿","拾","佰","仟","兆","拾","佰","仟","京"]
    return(zh_cn[int(x)])

def judge(a):
    list = []
    for i in a:
        if float(i)>99999999999999999:
            print(i+"数量级超过京，无法运算")
        elif i[:1:] == "0" and i[1:2:] != ".":
            print("憨批！",i,"前面有0")
        elif float(i) == round(float(i),2):
            list.append(i)
        else:
            print(i+"不是Double字符串")
    return(list)

def dot(b):
    list_dot = []
    for i in b:
        if int(i[len(i)-2::1]) == 0:
            list_dot.append("整")
        elif int(i[len(i)-1::1]) == 0:
            list_dot.append(convert_num(i[len(i)-2:len(i)-1:1])+"角")
        elif int(i[len(i)-2:len(i)-1:1]) == 0:
            list_dot.append("零"+convert_num(i[len(i)-1:len(i):1])+"分")
        else:
            list_dot.append(convert_num(i[len(i)-2:len(i)-1:1])+"角"+convert_num(i[len(i)-1::1])+"分")
    return(list_dot)

def yuan(c):
    list_yuan = []
    for i in c:
        num = i[:len(i)-3:1]
        res = ""
        list_yuan.append(clear_zero(num))
    return(list_yuan)

def clear_zero(d):
    res = ""
    count_z=0
    a = list(d)
    len_d = len(a)
    for i in range(len_d):
        res = res+convert_num(a[i])+convert_yuan(len_d-i-1)
        if a[i] == "0":    #判断当前位为0
            if i != 0:
                if a[i-1] != "0":   #判断前一位不为0
                    if (len_d-i-1) % 4 == 0 and i != len_d:     #判断当前位是万亿兆京位且不是元位
                        res = res[:len(res)-2:]+res[-1::]   #干掉一个”零“,保留万亿兆京
                    else:   #判断当前位不是万亿兆京位
                        res = res[:len(res)-1:]  #只去掉单位保留一个”零“
                        count_z += 1    #增加一个”零“，计数器+1
                else:   #前一位也为0
                    if (len_d-i-1) % 4 == 0 and i != len_d:     #判断当前位是万亿兆京位且不是元位
                        if count_z < 3:
                            res = res[:len(res)-count_z-2:]+res[-1::]   #去掉计数器个数的“零”并保留万亿兆京
                            count_z = 0     #计数器清零
                        else:
                            res = res[:len(res)-count_z-2:]   #去掉计数器个数的“零”及万亿兆京
                            count_z = 0     #计数器清零
                    else:   #判断当前位不是万亿兆京位
                        res = res[:len(res)-1:]  #只去掉单位保留一个”零“
                        count_z += 1    #增加一个”零“，计数器+1
        else:   #当前位不是0
            if i != 0 and count_z != 0:     #当前不是第一位，前面还有0
                res = res[:len(res)-count_z-1:]+res[-2::] #去掉计数器个数的“零”并保留万亿兆京
                count_z = 0     #计数器清零
    return(res)

def combine(e,f):
    if e == "零元":
        if f[:1:] == "零":
            return(f[1::])
        elif f != "整":
            return(f)
    return(e+f)


if __name__  ==  '__main__':
    x = []
    while True:
        try:
            l = input()
            x.append(l)
            y = judge(x)
            list_res = []
            yuan = yuan(y)
            dot = dot(y)
            for i in range(len(y)):
                print("人民币"+combine(yuan[i],dot[i]))
        except:
            break