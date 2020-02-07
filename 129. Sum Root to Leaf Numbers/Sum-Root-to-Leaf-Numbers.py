# 题目地址: https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Runtime: 28 ms Memory Usage: 12.8 MB
# 思路: 利用层次遍历, 算出每一层当前值

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = []
        q.append((root, root.val))
        res = 0
        
        while q:
            node, val = q.pop(0)
            
            if node.left:
                q.append((node.left, val*10 + node.left.val))
            
            if node.right:
                q.append((node.right, val*10 + node.right.val))
                
            if not node.left and not node.right:
                res += val

        return res


# 思路: 递归将左右子树加起来, 保存父节点的当前值, 作为参数传入下一层递归中
class githubSolution:
    def sumNumbers(self, root: TreeNode) -> int:

        def helper(node, cur_val):
            if not node: return 0
            next_val = cur_val * 10 + node.val

            if not (node.left or node.right):
                return next_val

            left_val = helper(node.left, next_val)
            right_val = helper(node.right, next_val)

            return left_val + right_val

        return helper(root, 0)


# RunTime: 16ms
# 思路: 递归实现
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.DFS(root, 0)
    
    def DFS(self, current, num):
        if current:
            num *= 10
            num += current.val
            
            if self.IsLeaf(current):
                return num
            
            else:                
                return self.DFS(current.left, num) + self.DFS(current.right, num)
        
        else:
            return 0
    
    def IsLeaf(self, current):
        if (current.left == None) and (current.right == None):
            return True
        return False


# 思路: 使用两个队列, node_queue, sum_queue, 两个队列相互对应
class githubSolution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        result = 0
        node_queue, sum_queue = [root], [root.val]
        while node_queue:
            for i in node_queue:
                cur_node = node_queue.pop(0)
                cur_val = sum_queue.pop(0)
                if cur_node.left:
                    node_queue.append(cur_node.left)
                    sum_queue.append(cur_val * 10 + cur_node.left.val)
                if cur_node.right:
                    node_queue.append(cur_node.right)
                    sum_queue.append(cur_val * 10 + cur_node.right.val)
                if not (cur_node.left or cur_node.right):
                    result += cur_val
        return result