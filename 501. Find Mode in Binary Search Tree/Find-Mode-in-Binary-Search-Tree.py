# 题目地址: https://leetcode.com/problems/find-mode-in-binary-search-tree/
# 直接遍历然后用字典记录

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        c = {}
        stack = []
        stack.append(root)
        while stack:
            node = stack.pop()
            if node.val in c:
                c[node.val] += 1
            else:
                c[node.val] = 1
            
            if node.left:
                stack.append(node.left)
                
            if node.right:
                stack.append(node.right)
        maxVal = 0
        res = []
        for k in c.keys():
            if c[k] > maxVal:
                maxVal = c[k]
                res = [k]
            elif c[k] == maxVal:
                res.append(k)
        return res


# RunTime: 32ms
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if not root: return []
        self.counts = {}        
        self.traverse(root)
        maxval = max(self.counts.values())
        result = []
        for k, v in self.counts.items():
            if v == maxval:
                result.append(k)
        return result
    
    def traverse(self, root):
        if root:
            self.counts[root.val] = self.counts.get(root.val, 0) + 1
            self.traverse(root.left)
            self.traverse(root.right)


# RunTime: 48ms
# So, when traversing each node, only the value of previous node is required to be compared with the value of current node for counting.
# 中序遍历 BST 相当于排序数组, 只需要和前一值比较
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.ans = []
        self.prev = root
        self.count = 0
        self.max = 0
        
        def visit(root):
            if root.val == self.prev.val:
                self.count += 1
            else:
                self.count = 1
            if self.count > self.max:
                self.max = self.count
                self.ans = []
            if self.count == self.max:
                self.ans.append(root.val)
            self.prev = root
  
        def inorder(root):
            if not root: return
            inorder(root.left)
            visit(root)
            inorder(root.right)
        
        inorder(root)
        return self.ans