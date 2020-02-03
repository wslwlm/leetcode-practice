# 题目地址: https://leetcode.com/problems/binary-tree-level-order-traversal/
# Runtime: 36 ms Memory Usage: 13 MB
# 思路: 将一个depth变量和节点一起存, 然后根据depth, 加入对应列表中

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = []
        q.append((root, 0))
        res = [[]]
        
        while q:
            node, depth = q.pop(0)
            
            if depth > len(res)-1:
                res.append([])
            res[depth].append(node.val)
            
            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
        return res


# RunTime: 12ms
# 将同一层级队列完全清空, 变为下一层级队列
class bestSolution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if not root:
            return None
        #create a queue to store the nodes
        q = [];
        
        #to store the level order of elements. This will be returned by the function
        levelOrderItems = []
        
        q.append(root)
        
        levelOrderItems.append([root.val])
        
        while len(q) > 0:
            
            #find a way to determine the level
            temp = []
            
            # currentNode = q.pop(0)
            
            # print(currentNode.val)
            q_1 = q[:]
            for currentNode in q_1:
                q.pop(0)
                
                if currentNode.left: 
                    q.append(currentNode.left)
                    temp.append(currentNode.left.val)

                if currentNode.right: 
                    q.append(currentNode.right)
                    temp.append(currentNode.right.val)
                
                
            if len(temp):
                    levelOrderItems.append(temp)
                
        return levelOrderItems         


# 思路: 如果采用递归方式，则需要将当前节点，当前所在的level以及结果数组传递给递归函数。
# 在递归函数中，取出节点的值，添加到level参数对应结果数组元素中
class githubSolution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        """递归法"""
        if root is None:
            return []
        
        result = []
        
        def add_to_result(level, node):
            """递归函数
            :param level int 当前在二叉树的层次
            :param node TreeNode 当前节点
            """
            if level > len(result) - 1:
                result.append([])
                
            result[level].append(node.val)
            if node.left:
                add_to_result(level+1, node.left)
            if node.right:
                add_to_result(level+1, node.right)
        
        add_to_result(0, root)
        return result   


# RunTime: 20ms
from collections import deque 

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # to do a breadth first search we need to use a queue data structure
        '''
        Algorithim 
        1. Create A queue, create variable to keep track of level
        2. Enqueu first element
        3. While queue is not empty
            append top of queue value to answer at curr_lelve
            if left or right exist, append them to queue
           
        Recursive Algorithim
        
        1. Base Case: append current to answer
        2. Recursive call : call recursively is left or right subtree exist
        '''
        if root == None:
            return []
        
        answer = []
        def recursive_helper(node, level):
            if level == len(answer):
                answer.append([])
            
            answer[level].append(node.val)
            
            if node.left:
                recursive_helper(node.left, level + 1)
            if node.right:
                recursive_helper(node.right, level + 1)
        
        recursive_helper(root, 0)
        
        return answer