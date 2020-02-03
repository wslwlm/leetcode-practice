# 题目地址: https://leetcode.com/problems/validate-binary-search-tree/
# Runtime: 40 ms Memory Usage: 15 MB
# 分治法, 分别递归左子树和右子树, 并且比较左子树的最大值与根和右子树的最大值和根

class MySolution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        l = root.left
        r = root.right
        while l and l.right:
            l = l.right
            
        if l and l.val >= root.val:
                return False
            
        while r and r.left:
            r = r.left
            
        if r and r.val <= root.val:
                return False
            
        return self.isValidBST(root.right) and self.isValidBST(root.left)


# RunTime: 20ms
# 利用BST的特性, 中序遍历为有序数组, 然后遍历并比较
class Solution:
    def isValidBST(self, root: TreeNode, lower=float('-inf'), upper=float('inf')) -> bool:
        return self.isValidBST_traversal(root)
    
    def isValidBST_traversal(self, root:TreeNode):
        stack = []
        current = root
        last_num = float('-inf')
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            if last_num >= current.val: return False
            last_num = current.val
            current = current.right
        return True


# RunTime: 24ms
# 思路: 比较每一个三节点子树的值, 自底向上, 根据BST的定义
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        
        """
        iteration, pass lower and upper from the root
        to left child, updated to lower, root.val
        to right child, updated to root.val upper
        """
        if not root:
            return True
            
        stack = [(root, float('-inf'), float('inf')), ] 
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True  


# 思路: 根据定义法递归
class githubSolution:
    def isValidBST(self, root: TreeNode, area: tuple=(-float('inf'), float('inf'))) -> bool:
        """思路如上面的分析，用Python表达会非常直白
        :param root TreeNode 节点
        :param area tuple 取值区间
        """
        if root is None:
            return True
        
        is_valid_left = root.left is None or\
                   (root.left.val < root.val and area[0] < root.left.val < area[1])
        is_valid_right = root.right is None or\
                   (root.right.val > root.val and area[0] < root.right.val < area[1])
        
        # 左右节点都符合，说明本节点符合要求
        is_valid = is_valid_left and is_valid_right
        
        # 递归下去
        return is_valid\
            and self.isValidBST(root.left, (area[0], root.val))\
            and self.isValidBST(root.right, (root.val, area[1]))


# 递归
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower, upper):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            return True

        return helper(root, float('-inf'), float('inf'))