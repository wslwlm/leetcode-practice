# 题目地址: https://leetcode.com/problems/distinct-subsequences/
# Runtime: 176 ms Memory Usage: 28.3 MB
# 思路: 动态规划

class MySolution:
    def numDistinct(self, s: str, t: str) -> int:
        if not s:
            return 0
        m = len(s)
        n = len(t)

        dp = [[0]*(n+1) for _ in range(m+1)]
        dp[0][0] = 1

        for i in range(1, m+1):
            dp[i][0] = 1

        for i in range(1, m+1):
            for j in range(1, min(i+1, n+1)):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]               
        
        print(dp)
        return dp[m][n]


# RunTime: 16 ms
# 思路: 当选择当前字符的时候, dp[i]相当于多了一种dp[i-1]的选择
import collections
class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        dic = collections.defaultdict(list)
        for i,ch in enumerate(t[::-1]):
            dic[ch].append(len(t)-i)
            
        dp = [1] + [0]*len(t)
        for ch in s:
            for i in dic[ch]:
                dp[i] += dp[i-1]
                
        return dp[-1]


# RunTime: 20ms
# 思路: 与上面类似, 一种s正向一种s反向
class Solution2(object):
    def numDistinct(self, s, t):
        dp = [0] * (len(t) + 1)
        dp[-1] = 1 # String terminator count
        
        indices = collections.defaultdict(list)
        for i, v in enumerate(t):
            indices[v].append(i)
        
        for c in reversed(s): 
            for i in indices[c]:
                dp[i] += dp[i+1]
        
        return dp[0]