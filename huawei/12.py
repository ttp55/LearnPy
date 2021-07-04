# @Time : 2021/4/29 20:57
# @Author : WZG
# --coding:utf-8--

l = input().split(',')
l = list(map(int, l))
n = int(input())
job_time = 0

for i in range(len(l)):
    job_time = job_time + 1 + n
    try:
        if l[i+1] != l[i]:
            job_time = job_time + n - 1
            continue
        else:
            for x in range(len(l)):
                if l[x] != l[i]:
                    l[x], l[i] = l[i], l[x]
    except:
        break

print(job_time)


# 输入一个列表，再输入一个任务等待时间N，每个任务执行时间为1，相同任务要有间隔N, 不同任务无间隔， 最终输出完成任务所需最少时间多少

# 2,2,2,3 如N为2 应该输出 7