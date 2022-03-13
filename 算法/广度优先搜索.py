# @Time : 2021/6/21 9:37
# @Author : WZG
# --coding:utf-8--
from collections import deque


# 添加节点与邻居
graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

# 首先创建队列，因为先进先出，将要处理的节点放进队列，数组存储处理过的节点，循环处理当前队列节点，如果尾字母为M，就返回，它就为最近节点

print(graph)
def search(name):
    search_queue = deque()
    search_queue += graph[name]

    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person[-1] == 'm':
                return print(person + ' is a mango seller!')
            else:
                search_queue += graph[person]
                searched.append(person)

    return "no seller"


search('you')

