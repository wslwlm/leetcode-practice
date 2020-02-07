# 题目地址: https://leetcode.com/problems/binary-tree-preorder-traversal/
# Runtime: 16 ms Memory Usage: 12.7 MB
# 思路: 访问根节点, 递归左子树, 递归右子树

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MySolution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        res = []
        
        res.append(root.val)
        res += self.preorderTraversal(root.left)
        res += self.preorderTraversal(root.right)
        
        return res


# Runtime: 24 ms Memory Usage: 12.6 MB
# 思路: 栈实现
class MySolution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        s = []
        
        while s or root:
            while root:
                s.append(root)
                res.append(root.val)
                root = root.left
            
            node = s.pop()
            root = node.right  
        return res


# RunTime: 8ms
# 思路: 递归实现, python中使用的是引用传递, 共同列表
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res


# RunTime: 12ms
# 思路: 栈实现
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack, preorder = [], []
        if not root:
            return preorder
        stack.append(root)
        
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder