# @Time : 2022/3/1 9:57
# @Author : WZG
# --coding:utf-8--


class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return self.maxDepth(root.left) + self.maxDepth(root.right)