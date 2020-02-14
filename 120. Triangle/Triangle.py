# 题目地址: https://leetcode.com/problems/triangle/
# Runtime: 60 ms Memory Usage: 13.4 MB
# 思路: 简单动态规划, 下一行的值由上一行的两个元素决定, min(dp[i-1], dp[i])

class MySolution:
    def minimumTotal(self, triangle) -> int:
        if not triangle or not triangle[0]:
            return 0
        dp = [triangle[0][0]]
        m = len(triangle)
        for i in range(1, m):
            temp = [triangle[i][0] + dp[0]]
            for j in range(1, len(triangle[i])-1):
                temp.append(min(dp[j-1], dp[j])+triangle[i][j])
            temp.append(triangle[i][len(triangle[i])-1]+dp[len(triangle[i])-2])
            dp = temp
        return min(dp)


# RunTime: 44 ms
# 思路: 类似思路, 空间优化
class Solution1:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        N = len(triangle)
        dp = [2**31-1 for _ in range(N+1)]
        dp[1] = 0
        for row in triangle:
            for i, e in zip(range(len(row)-1, -1, -1), row[::-1]):
                dp[i+1] = min(dp[i], dp[i+1]) + e
        return min(dp)


# RunTime: 48 ms
# 思路: 将三角形倒转过来, 从底开始, 加到顶部, 没使用额外空间
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        
        #bottom-up
        for i in reversed(range(0, len(triangle)-1)):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]