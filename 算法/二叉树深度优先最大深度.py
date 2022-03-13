# @Time : 2022/3/1 9:54
# @Author : WZG
# --coding:utf-8--
class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
