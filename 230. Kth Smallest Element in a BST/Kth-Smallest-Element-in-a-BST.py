# 题目地址: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# Runtime: 44 ms Memory Usage: 16.8 MB
# 思路: BST树的中序遍历是有序的, 栈实现

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        s = []
        while root or s:
            while root:
                s.append(root)
                root = root.left
            
            node = s.pop()
            k -= 1
            if k == 0:
                return node.val
            root = node.right


# RunTime: 
# 思路: 递归实现中序遍历BST
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0
        self.res = None
        self.flag = False
        def dfs(root):
            if root:
                dfs(root.left)
                self.count+=1
                if self.count == k:
                    self.flag = True
                    self.res =  root.val
                if self.flag: return
                dfs(root.right)
        dfs(root) 
        return self.res


# 摘自github上
# 参考链接: https://github.com/azl397985856/leetcode/blob/master/problems/230.kth-smallest-element-in-a-bst.md
# 还有一种思路是: 
# 联想到二叉搜索树的性质，root 大于左子树，小于右子树，如果左子树的节点数目等于 K-1，那么 root 就是结果，否则如果左子树节点数目小于 K-1，那么结果必然在右子树，否则就在左子树。 因此在搜索的时候同时返回节点数目，跟 K 做对比，就能得出结果了。