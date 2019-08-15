# @time:  2019/8/15 10:26
# @author: WZG
# encoding: utf-8


def spin_words(s):
    # Your code goes here

    # return ' '.join(l)
    return ' '.join(n[::-1] if len(n) > 4 else n for n in (s.split()))


print(spin_words("Welcome to Beijing"))

