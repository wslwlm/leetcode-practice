# 题目地址: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Runtime: 36 ms Memory Usage: 14 MB
# (非递归)广度优先搜索得到深度

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MySolution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = []
        root.val = 1
        queue.append(root)
        depth = 1
        while queue:
            node = queue.pop(0)
            depth = node.val
            if node.left:
                node.left.val = depth + 1
                queue.append(node.left)
            if node.right:
                node.right.val = depth + 1
                queue.append(node.right)
        return depth  


# 递归实现
class MySolution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        leftDepth = self.maxDepth(root.left)
        rightDepth = self.maxDepth(root.right)
        if leftDepth > rightDepth:
            return leftDepth + 1
        else:
            return rightDepth  + 1

# 递归实现
# RunTime: 16ms
class bestSolution:
    def maxDepth(self, root: TreeNode) -> int:
            return max(self.maxDepth(root.left),self.maxDepth(root.right))+1 if root else 0