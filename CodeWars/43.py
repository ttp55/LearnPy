# @Time : 2019/9/6 8:52
# @Author : WZG
# --coding:utf-8--


def str_func(num_str):
    if len(num_str) == 1:
        return None
    elif len(num_str) == 2:
        if int(num_str[0]) > int(num_str[1]):
            return num_str[1] + num_str[0]
        else:
            return None
    else:
        sub_result = str_func(num_str[1:])
        if sub_result != None:
            return num_str[0] + str(sub_result)
        else:
            smaller_max_idx = None
            sub_str = num_str[1:]
            for i in range(len(sub_str)):
                if int(sub_str[i]) < int(num_str[0]) \
                        and (
                            smaller_max_idx is None
                            or int(sub_str[i]) > int(sub_str[smaller_max_idx])
                        ):
                    smaller_max_idx = i
            if smaller_max_idx is None:
                return None
            else:
                ret_str = sub_str[smaller_max_idx] + ''.join(sorted(sub_str[:smaller_max_idx] + num_str[0] + sub_str[smaller_max_idx + 1:], reverse=True))
                return ret_str


def next_smaller(num):
    ret = str_func(str(num))
    if ret is None or ret[0] == '0':
        return -1
    else:
        return int(ret)


print(next_smaller(1234567908))
