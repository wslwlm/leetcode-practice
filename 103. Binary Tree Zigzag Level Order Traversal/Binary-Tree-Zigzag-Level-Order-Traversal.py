# 题目地址: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Runtime: 32 ms Memory Usage: 12.7 MB
# 借用层次遍历的做法, 用flag记录是否反转(可以简化为用奇偶判定), 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = []
        q.append(root)
        res = []
        
        flag = True
        while q:
            q_1 = q[:]
            temp = []
            
            for node in q_1:
                q.pop(0)
                
                if node.left:
                    q.append(node.left)
                    
                if node.right:
                    q.append(node.right)
                
                temp.append(node.val)
            
            if len(temp):
                if flag:
                    res.append(temp)
                    flag = False
                else:
                    temp.reverse()
                    res.append(temp)
                    flag = True
        return res


# RunTime: 12ms
# 思路: is_order_left标示当前为从左到右(数组尾部)还是从右到左(数组头部).
# 两个队列, node_queue(层次遍历), level_list(添加每一层结果), 
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        level_list = deque()
        if root is None:
            return []
        # start with the level 0 with a delimiter
        node_queue = deque([root, None])
        is_order_left = True

        while len(node_queue) > 0:
            # 出队
            curr_node = node_queue.popleft()

            if curr_node:
                if is_order_left:
                    # 放在数组尾部
                    level_list.append(curr_node.val)
                else:
                    # 放在数组头部
                    level_list.appendleft(curr_node.val)

                if curr_node.left:
                    node_queue.append(curr_node.left)
                if curr_node.right:
                    node_queue.append(curr_node.right)
            else:
                # we finish one level
                ret.append(level_list)
                # add a delimiter to mark the level
                # 入队一个None来标识这一层的结束
                if len(node_queue) > 0:
                    node_queue.append(None)

                # prepare for the next level
                level_list = deque()
                is_order_left = not is_order_left

        return ret
                    

# RunTime: 24ms
# 思路: 对一棵树进行之字形遍历其实对其子树进行之字形遍历
# 当前层次为偶数时，将当前节点放到当前层的结果数组尾部
# 当前层次为奇数时，将当前节点放到当前层的结果数组头部
# 递归对左子树进行之字形遍历，层数参数为当前层数+1
# 递归对右子树进行之字形遍历，层数参数为当前层数+1
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        search(root,0,res)
        return res
    
def search(root,level,res):
    if root==None:
        return
    if len(res)<=level:
        res.append([])
    if (level%2==0) :
        res[level].append(root.val)
    else:
        res[level].insert(0,root.val)

    search(root.left,level+1,res)
    search(root.right,level+1,res)