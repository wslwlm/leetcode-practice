# 题目地址: https://leetcode.com/problems/set-matrix-zeroes/
# Runtime: 136 ms Memory Usage: 13.2 MB
# 寻找0所在的位置, 填充row,col列表, 再将matrix中元素置0

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        row = []
        col = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row.append(i)
                    col.append(j)
        
        for i in range(m):
            for c in col:
                matrix[i][c] = 0
        
        for j in range(n):
            for r in row:
                matrix[r][j] = 0


# RunTime: 112ms
# 一样的思路
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        coords = []
        
        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                if val == 0:
                    coords.append((i, j))
                    
        for coord in coords:
            self.helper(matrix, coord[0], coord[1])
                    
                    
    def helper(self, matrix: List[List[int]], i: int, j: int):
        height = len(matrix)
        width = len(matrix[0])
        
        for x in range(height):
            matrix[x][j] = 0
            
        for x in range(width):
            matrix[i][x] = 0