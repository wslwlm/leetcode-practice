# 题目地址: https://leetcode.com/problems/minimum-path-sum/
# Runtime: 104 ms Memory Usage: 14.5 MB
# 思路: 动态规划

class MySolution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        if n == 0:
            return 0
        
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        for i in range(1, n):
            dp[0][i] = dp[0][i-1] + grid[0][i]
            
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
                
        return dp[-1][-1]


# RunTime: 76 ms
# 思路: 动态规划, 空间复杂度优化为O(n)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        row_len, col_len = len(grid), len(grid[0])
        dp = [grid[0][0]]

        for col in range(1, col_len):
            dp.append(dp[col-1]+grid[0][col])

        for row in range(1, row_len):
            dp[0] = dp[0]+grid[row][0]
            for col in range(1, col_len):
                dp[col] = min(dp[col-1], dp[col])+grid[row][col]

        return dp[-1]