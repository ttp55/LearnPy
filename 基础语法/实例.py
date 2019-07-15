no = 30
guess = 0
while guess!=no:
    guess = int(input("请输入你猜的数字："))
    if(guess==no):
        print("yes!")
    elif(guess<no):
        print("小了!")
    elif(guess>no):
        print("大了！")
    else:
        print("error!")
