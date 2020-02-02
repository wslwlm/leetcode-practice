# 题目地址: https://leetcode.com/problems/binary-tree-inorder-traversal/
# Runtime: 28 ms Memory Usage: 12.7 MB
# 沿着左子树走到底, 然后回溯过程中, 先添加到 res, 然后将指针root指向右节点, 再遍历左子树
#
# 中序遍历的顺序为左-根-右，具体算法为：
# 从根节点开始，先将根节点压入栈
# 然后再将其所有左子结点压入栈，取出栈顶节点，保存节点值
# 再将当前指针移到其右子节点上，若存在右子节点，则在下次循环时又可将其所有左子结点压入栈中， 重复上步骤
# 图解参考: https://github.com/azl397985856/leetcode/blob/master/problems/94.binary-tree-inorder-traversal.md

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MySolution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
                
            res.append(stack[-1].val)
            root = stack[-1].right
            stack.pop()
        
        return res


# Runtime: 28 ms Memory Usage: 12.7 MB
# 递归就是递归左子树, 然后访问中间节点, 再访问右子树.
class MySolution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def helper(root, res):
            if not root:
                return
            helper(root.left, res)
            res.append(root.val)
            helper(root.right, res)

        helper(root, res)
        return res


# Runtime: 32 ms Memory Usage: 12.8 MB
# 非递归思路参考前面
class MySolution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = []
        stack.append(root)
        res = []
        flag = True
        
        node = root
        while stack:
            node = stack[-1]
            while flag and node.left is not None:
                stack.append(node.left)
                node = node.left
            
            node = stack.pop()
            res.append(node.val)
            
            flag = False
                
            if node.right:
                stack.append(node.right)
                flag = True

        return res