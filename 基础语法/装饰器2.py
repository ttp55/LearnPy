from 基础语法.decorator import log


@log()
def now():
    print('Hello decorator!')


now()
