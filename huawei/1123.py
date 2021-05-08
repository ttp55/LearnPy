num = '151021.15'
dt1 = {'0': '零', '1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒',
       '8': '捌', '九': '玖'}
lt1 = ['', '万', '亿']
lt2 = ['', '拾', '佰', '仟']
str_ = '人民币'
intp, floatp = num.split('.')


def fun(num):
    global str_
    counter = len(num) // 4
    if len(num) % 4 == 0:
        for index, i in enumerate(num[:4]):
            if i == '0':
                if str_[-1] != '零':
                    str_ += '零'
            else:
                str_ += dt1.get(i) + lt2[:len(num[:4])][::-1][index]
    else:
        mm = len(num) % 4
        for index, i in enumerate(num[:mm]):
            if i == '0':
                if str_[-1] != '零':
                    str_ += '零'
            else:
                str_ += dt1.get(i) + lt2[:len(num[:mm])][::-1][index]
        str_ += lt1[counter % 4]
        fun(num[mm:])


def floatfun(num):
    global str_
    if num == ['0', '0']:
        str_ += '整'
    else:
        for index, i in enumerate(num):
            if i != '0':
                str_ += dt1.get(i) + ['角', '分'][index]


def main():
    global str_
    fun(list(intp))
    str_ += '元'
    floatfun(list(floatp))
    print(str_)


if __name__ == '__main__':
    main()
