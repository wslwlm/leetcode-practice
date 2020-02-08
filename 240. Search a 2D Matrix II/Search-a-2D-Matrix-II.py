# 题目地址: https://leetcode.com/problems/search-a-2d-matrix-ii/
# Runtime: 32 ms Memory Usage: 17.3 MB
# 思路: 暴力搜索, 过滤掉一些不可行解

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            if matrix[i][-1] < target or matrix[i][0] > target:
                continue
            for j in range(n):
                if matrix[i][j] == target:
                    return True
        return False


# RunTime: 12ms
# 思路: 从左下和右上作为起始点, 这里选择右上, 这两个点的特殊之处在往左为小, 往下为大, 减少了搜索空间。
# 充分运用矩阵的特性（横向纵向都递增）， 我们可以从角落（左下或者右上）开始遍历，这样时间复杂度是O(m + n)
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        
        # if (matrix == None):
        #     return False
        
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        j = col - 1
        
        while (i < row and j >= 0):
            if (matrix[i][j] > target):
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
            
        return False