# 题目地址: https://leetcode.com/problems/path-sum-ii/
# Runtime: 44 ms Memory Usage: 13.8 MB
# 思路: 递归实现, 这个是求和到叶节点, 
# 递归为对左子树pathSum, sum为sum-root.val
# 对右子树pathSum, sum为sum-root.val
# 然后将左右子树得来的 List[List[int]] --> 每一个添加root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        if not root.right and not root.left:
            if root.val == sum:
                return [[root.val]]
            else:
                return []
        
        res = []
        for l in self.pathSum(root.right, sum-root.val):
            l = [root.val] + l
            res.append(l)
            
        for l in self.pathSum(root.left, sum-root.val):
            l = [root.val] + l
            res.append(l)
            
        return res


# RunTime: 24ms
# 思路: 回溯法
class Solution:
    def traverse(self, root, summ, result, tmpResult, tmpSum):
        if not root:
            return

        tmpResult.append(root.val)
        tmpSum += root.val
        if not root.left and not root.right:
            if tmpSum == summ:
                result.append(tmpResult[:])
        else:
            self.traverse(root.left, summ, result, tmpResult, tmpSum)
            self.traverse(root.right, summ, result, tmpResult, tmpSum)
        # 必须要pop, 不pop的话回溯的时候, 由于引用传递, 列表保留有进入路径的值, 会产生问题
        tmpResult.pop()

    def pathSum(self, root: TreeNode, summ: int):
        if not root:
            return []

        result = []
        self.traverse(root, summ, result, [], 0)

        return result


# 思路: 回溯法
class githubSolution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        
        def trace_node(pre_list, left_sum, node):
            new_list = pre_list.copy()
            new_list.append(node.val)
            if not node.left and not node.right:
                # 这个判断可以和上面的合并，但分开写会快几毫秒，可以省去一些不必要的判断
                if left_sum == node.val:
                    result.append(new_list)
            else:
                if node.left:
                    trace_node(new_list, left_sum-node.val, node.left)
                if node.right:
                    trace_node(new_list, left_sum-node.val, node.right)
        
        trace_node([], sum, root)
        return result


# RunTime: 32ms
# 思路: 使用栈实现
class Solution:
    def pathSum(self, root: TreeNode, sumToGet: int) -> List[List[int]]:
        
        if not root:
            return []
        
        currentNodeWithPath = []
        
        currentNodeWithPath.append((root, []))
        
        paths = []
        while len(currentNodeWithPath) > 0:
            
            currentNode, pathSoFar = currentNodeWithPath.pop()
            
            if currentNode.left is None and currentNode.right is None:
                
                if sum(pathSoFar) + currentNode.val == sumToGet:
                    paths.append(pathSoFar + [currentNode.val])
                    
            if currentNode.left is not None:

                currentNodeWithPath.append((
                    currentNode.left,
                    pathSoFar + [currentNode.val]
                ))
                    
            if currentNode.right is not None:

                currentNodeWithPath.append((
                    currentNode.right,
                    pathSoFar + [currentNode.val]
                ))
                    
        return paths