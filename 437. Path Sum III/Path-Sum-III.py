# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        return self.pathSum(root.right, sum) + self.pathSum(root.left, sum) + self.helper(root, sum)
    
    def helper(self, root, sum):
        if root is None:
            return 0
        l = 1 if root.val == sum else 0
        return self.helper(root.left, sum-root.val) + self.helper(root.right, sum-root.val) + l


# RunTime: 36ms
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        sum_cnt = {0: 1}
        res = 0
        
        def helper(root, s):
            if not root:
                return
            nonlocal sum, res
            s += root.val
            res += sum_cnt.get(s - sum, 0)
            sum_cnt[s] = sum_cnt.get(s, 0) + 1
            helper(root.left, s)
            helper(root.right, s)
            sum_cnt[s] -= 1
            
        helper(root, 0)
        return res


# RunTime: 32ms
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        self.count = 0
        
        def helper(root, target, memo, currPathSum):
            if not root:
                return            
            
            currPathSum += root.val
            self.count += memo.get(currPathSum - target, 0)
            memo[currPathSum] = memo.get(currPathSum, 0) + 1
            
            helper(root.left, target, memo, currPathSum)
            helper(root.right, target, memo, currPathSum)
            
            
            memo[currPathSum] -= 1
            currPathSum -= root.val
            return
        
        memo = {0 : 1}
        helper(root, sum, memo, 0)        
        return self.count