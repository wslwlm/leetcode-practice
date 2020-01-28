# 题目地址: https://leetcode.com/problems/rotate-image/
# Runtime: 32 ms Memory Usage: 12.8 MB
# 深拷贝, 然后旋转

class MySolution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        matrix_tmp = copy.deepcopy(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][n-j-1] = matrix_tmp[j][i]


# RunTime: 12 ms
# 沿对角线对折, 然后再reverse. 时间复杂度: O(n); 空间复杂度: O(1)
class bestSolution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(n):
            matrix[i].reverse()