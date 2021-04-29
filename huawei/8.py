# @Time : 2021/4/26 14:04
# @Author : WZG
# --coding:utf-8--
while True:
    try:
        l = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖',  '角', '分', '整']
        l1 = ['元', '拾', '佰', '仟']
        l2 = ['元', '万', '亿']
        n = list(input())
        s = ['人民币']
        m = len(n) - 3
        y = [n[: m][x if x > 0 else 0: x - 4 if x - 4 > -1 else None: -1][::-1] for x in range(m - 1, 0, -4)][::-1]
        for v in range(len(y)):
            y[v] = list(map(int, y[v]))
        print(y)

        for i in y:
            if len(i) == 2:
                s.append(l1[1])
                s.append(l[i[1]])
                if len(y) >= 2:
                    s.append(l2[len(y)-2])
                continue

            elif len(i) > 2 and len(y) >= 2:
                for x in i:
                    s.append(l[x])
                    if i.index(x) == len(i) - 1:
                        continue
                    else:
                        s.append(l1[len(i)-i.index(x)-1])
                b = len(y) - y.index(i)

                s.append(l2[len(y) - b])


        print(s)






    except:
        break
