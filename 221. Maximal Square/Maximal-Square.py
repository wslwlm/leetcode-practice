# 题目地址: https://leetcode.com/problems/maximal-square/
# Runtime: 360 ms Memory Usage: 13.8 MB
# 思路: 暴力搜索

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        def search(i, j):
            length = 1
            flag = True
            while flag and (i+length < m) and (j+length < n):
                length += 1
                for r in range(length):
                    if matrix[i+length-1][r+j] != '1':
                        flag = False
                for c in range(length):
                    if matrix[c+i][j+length-1] != '1':
                        flag = False

            if not flag:
                length -= 1
            return length
            
        maxL = 0
        for i in range(m):
            if i + maxL > m:
                continue
            for j in range(n):
                if j + maxL > n:
                    continue
                if matrix[i][j] == '1':
                    l = search(i, j)
                    if l > maxL:
                        maxL = l
                        
        return maxL**2


# RunTime: 160ms
# 思路: 首先进行了数字化(数字化的结果是横向连续 1), 然后转置矩阵, 观察纵向, 纵向比i大的值
# 无用列进行优化, popper中舍去
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 将字符matrix数字化
        for y, row in enumerate(matrix):
            count_x = 1
            for x, val in enumerate(row):
                if val is '1':
                    matrix[y][x] = count_x
                    count_x += 1
                else:
                    matrix[y][x] = 0
                    count_x = 1

        # transpose
        best = 0
        matrix = list(zip(*matrix))
        popper = list()
        for i in range(10000):
            flag = False
            for j, col in enumerate(matrix):
                count = 0
                for val in col:
                    if val > i: 
                        count += 1
                        if count > i:
                            best = i + 1
                            flag = True
                            break
                    else:
                        count = 0
                if flag:
                    break
                else:
                    popper.append(j)
            if flag:
                if popper:
                    matrix = [col for j, col in enumerate(matrix) if j not in popper]
                    popper.clear()
            else:
                break
        
        return best ** 2


# RunTime: 164ms
# 思路: 动态规划, 空间复杂度优化为行数, 因为dp[i][j]需要的是上一行的dp[i-1][j]的值以及前一个值pre
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        dp = [0 if c == '0' else 1 for c in matrix[0]]
        res = max(dp)
        for i in range(1,len(matrix)):
            pre = dp[0]
            dp[0] = 0 if matrix[i][0] == '0' else 1
            for j in range(1,len(matrix[0])):
                if matrix[i][j] == '1':
                    dp[j], pre = min(dp[j-1], dp[j], pre)+1, dp[j]
                else:
                    pre, dp[j] = dp[j], 0
                    
            res = max(max(dp), res)
            
        return res ** 2


# RunTime: 168ms
# 思路: 秒啊, 从横向进行扩展, 对每一行中的连续1进行计数, 然后进行纵向 widths[i] > k 记录纵向的长度
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if (not matrix) or (not matrix[0]):
            return 0
        n = len(matrix)
        m = len(matrix[0])
        widths = [0] * n
        k = 0
        for j in range(0, m):
            max_continous_k = 0
            continous_k = 0
            for i in range(0, n):
                if matrix[i][j] == '1':
                    widths[i] += 1
                else:
                    widths[i] = 0
                if widths[i] > k:
                    continous_k += 1
                    max_continous_k = max(continous_k, max_continous_k)
                else:
                    continous_k = 0
            if max_continous_k > k:
                k += 1
        return k * k


# RunTime: 172ms
# 思路: 动态规划, X数组存储前一行的dp, Y数组存储当前行dp
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        X = [int(x) for x in matrix[0]]
        l = max(X)
        
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            Y = [0 for _ in X]
            if matrix[i][0] == '1':
                Y[0] = 1
                l = max(l, 1)
            
            for j in range(1, n):
                if matrix[i][j] == '1':
                    Y[j] = min(Y[j - 1], X[j - 1], X[j]) + 1
                    l = max(l, Y[j])
            
            X = Y
        
        return l * l