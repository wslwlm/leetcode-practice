# 题目地址: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# Runtime: 64 ms Memory Usage: 23.1 MB
# 思路: 递归, 返回值并不是单一, 如果树中存在共同祖先则返回共同祖先, 不存在则返回查找到的p或q
# 其他思路: DFS分别寻找到两个节点p和q的路径，然后对比路径，查看他们的第一个分岔口，则为LCA
# 链接参考: https://www.hrwhisper.me/algorithm-lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 返回root
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if not left:
            return right    # 返回共同祖先
        if not right:
            return left
        else:
            return root     # 找到的p和q都是在root的两边
        

# RunTime: 60ms
# 思路: DFS分别寻找到两个节点p和q的路径，然后对比路径，查看他们的第一个分岔口，则为LCA
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parent = {root : None}
        while p not in parent or q not in parent:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
                parent[node.left] = node
            if node.right:
                stack.append(node.right)
                parent[node.right] = node
        
        ancestor = set()
        # 算出p的路径
        while p:
            ancestor.add(p)
            p = parent[p]
        # 比对分叉口的位置
        while q not in ancestor:
            q = parent[q]
        return q