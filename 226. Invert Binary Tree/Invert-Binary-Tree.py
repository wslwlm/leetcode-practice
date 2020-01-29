# 题目地址: https://leetcode.com/problems/invert-binary-tree/
# Runtime: 24 ms Memory Usage: 12.8 MB
# 递归

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MySolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# RunTime: 8ms
class bestSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root


# 栈代替递归, 防止爆栈
class githubSolution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        stack = [root]
        while stack:
            node = stack.pop(0)
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return root