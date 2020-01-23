# 题目地址: https://leetcode.com/problems/unique-paths/
# Runtime: 28 ms Memory Usage: 12.8 MB
# 动态规划, 对每一行进行值的存储, 空间复杂度由O(m*n)优化为O(m)

class MySolution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * m
        for i in range(1, n):
            for j in range(1, m):
                dp[j] = dp[j] + dp[j-1]
        return dp[-1]


# 一样思路, 空间复杂度较大
# RunTime: 8ms
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[1] * n for e in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                paths[i][j] = paths[i-1][j] + paths[i][j-1]
        return paths[m-1][n-1]