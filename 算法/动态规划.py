# @Time : 2022/3/24 15:23
# @Author : WZG
# --coding:utf-8--

grid = [[1,3,1],[1,5,1],[4,2,1]]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if i == j == 0: continue
        elif i == 0: grid[i][j] = grid[i][j - 1] + grid[i][j]
        elif j == 0: grid[i][j] = grid[i - 1][j] + grid[i][j]
        else: grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
print(grid[-1][-1])
