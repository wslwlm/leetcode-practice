# 题目地址: https://leetcode.com/problems/binary-tree-right-side-view/
# Runtime: 28 ms Memory Usage: 12.8 MB
# 思路: 层次遍历, 取每一层的最右边的节点

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = []
        res = []
        q.append(root)
        while q:
            q_1 = q[:]
            lastNode = None
            for node in q_1:
                lastNode = q.pop(0)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(lastNode.val)
        return res


# RunTime: 20ms
# 思路: 递归
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root : return []
        res=[]
        def dfs(root, res, level):
            if not root: return
            if level==len(res): ## one element added for one level
                res.append(root.val)
            dfs(root.right, res, level+1)
            dfs(root.left, res, level+1)
            return res
        return dfs(root, res,0)