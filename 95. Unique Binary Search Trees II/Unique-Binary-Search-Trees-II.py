# 题目地址: https://leetcode.com/problems/unique-binary-search-trees-ii/
# Runtime: 60 ms Memory Usage: 14.9 MB
# 递归得到 n-1 的树, 然后将n插入这些树中生成新的树, 麻烦的是需要负值这些树, 防止指针错乱

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class MySolution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        if n == 1:
            return [TreeNode(1)]
        res = []
        # 生成 n-1 的树
        for tree in self.generateTrees(n-1):
            #print(tree, n)
            res += self.insertNum(tree, n)
        return res

    # 将 n 插入树中       
    def insertNum(self, tree, n):
        res = []
        tmp = tree
        while tmp:
            node = TreeNode(n)
            s = tmp.right
            tmp.right = node
            node.left = s
            newTree = self.copyTree(tree)
            res.append(newTree)
            
            tmp.right = s
            node.left = None
            tmp = tmp.right
            
        node = TreeNode(n)
        node.left = tree
        res.append(node)
        return res
    
    # 复制树
    def copyTree(self, root):
        if root:
            new_root = TreeNode(root.val)
        else:
            return None
        new_root.left = self.copyTree(root.left)
        new_root.right = self.copyTree(root.right)
        return new_root


# 分治法
# 思路: 将问题进一步划分为子问题，假如左侧和右侧的树分别求好了，将左右两者进行做和, 需要两层循环来完成这个过程
class githubSolution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if not n:
            return []

        def generateTree(start, end):
            if start > end:
                return [None]
            res = []
            for i in range(start, end + 1):
                ls = generateTree(start, i - 1)
                rs = generateTree(i + 1, end)
                for l in ls:
                    for r in rs:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        res.append(node)

            return res

        return generateTree(1, n)


# 思路: 分治法
from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.__memo = defaultdict(lambda: None)

    def generateTrees(self, n: int) -> List[TreeNode]:

        # Sanity check
        if not n:
            return []
        return self.__generateSubtrees(1, n + 1)

    def __generateSubtrees(self, start: int, end: int) -> List[TreeNode]:
        size = end - start

        # Edge cases
        if size == 0:
            return [None]
        if size == 1:
            return [TreeNode(start)]

        # Check memo
        if self.__memo[(start, end)] is not None:
            return self.__memo[(start, end)]

        all_subtrees = []

        for idx in range(start, end):
            left_subtrees = self.__generateSubtrees(start, idx)
            right_subtrees = self.__generateSubtrees(idx + 1, end)

            subtrees_product = [(a, b)
                                for a in left_subtrees
                                for b in right_subtrees]

            def createTree(val, left_node, right_node):
                root = TreeNode(val)
                root.left = left_node
                root.right = right_node
                return root

            all_subtrees.extend([createTree(idx, left_subtree, right_subtree)
                                 for left_subtree, right_subtree
                                 in subtrees_product])
        # Memoization
        self.__memo[(start, end)] = all_subtrees

        return all_subtrees


# RunTime: 36ms
# 分治法, 递归过程中用hashmap记录, 避免重复计算
class Solution(object):
    def generateTrees(self, n):
        if n <= 0:
            return []
        self.cache = {}
        ans = self._dfs(0, n + 1)
        return ans

    def _dfs(self, lo, hi):
        if hi - lo == 1:
            return [None]
        if (lo, hi) not in self.cache:
            ans = []
            for mid in range(lo + 1, hi):
                for left in self._dfs(lo, mid):
                    for right in self._dfs(mid, hi):
                        current = TreeNode(mid)
                        current.left = left
                        current.right = right
                        ans.append(current)
            self.cache[(lo, hi)] = ans
        return self.cache[(lo, hi)]