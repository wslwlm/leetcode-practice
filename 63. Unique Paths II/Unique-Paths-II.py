# 题目地址: https://leetcode.com/problems/unique-paths-ii/
# Runtime: 44 ms Memory Usage: 12.7 MB
# 初始值注意一下, 有障碍的话初始值会改变, dp数组在遇到障碍dp[i][j]=0

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp =  [[0]*n for i in range(m)]
        for i in range(n):
            if obstacleGrid[0][i] == 1:
                break
            dp[0][i] = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1 or (obstacleGrid[i][j-1] == 1 and obstacleGrid[i-1][j] == 1):
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j]
        res = 0 if obstacleGrid[-1][-1] == 1 else dp[-1][-1]
        return res


# RunTime: 28ms
# 空间复杂度得到优化, 二维dp优化为一维dp
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if len(obstacleGrid) <= 0 or len(obstacleGrid[0]) <= 0:
            return 0
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        paths = []
        for j in range(m):
            if obstacleGrid[0][j] == 1:
                paths.extend([0] * (m - j))
                break
            else:
                paths.append(1)
        for i in range(1, n):
            if obstacleGrid[i][0] == 1:
                paths[0] = 0
            for j in range(1, m):
                if obstacleGrid[i][j]:
                    paths[j] = 0
                else:
                    paths[j] += paths[j - 1]
        return paths[-1]    