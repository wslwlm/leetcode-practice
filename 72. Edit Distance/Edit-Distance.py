# 题目地址: https://leetcode.com/problems/edit-distance/
# Runtime: 172 ms Memory Usage: 16 MB
# 思路: 动态规划, 

class MySolution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        
        dp = [[0]*(n+1) for _ in range(m+1)]
        
        for i in range(1, n+1):
            dp[0][i] = i
        
        for i in range(1, m+1):
            dp[i][0] = i
            
        for i in range(1, m+1):
            for j in range(1, n+1):
                # 相等则不需要操作
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 相对应的是替换, 添加, 删除操作
                    dp[i][j] = min(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + 1

        return dp[m][n]


# RunTime: 32 ms
# 思路: 
from collections import deque

class Solution1:
    def minDistance(self, word1: str, word2: str) -> int:
        visit, q = set(), deque([(word1, word2, 0)])
        while True:
            w1, w2, d = q.popleft()
            if (w1, w2) not in visit:
                if w1 == w2:
                    return d
                visit.add((w1, w2))
                while w1 and w2 and w1[0] == w2[0]:
                    w1, w2= w1[1:], w2[1:]
                d += 1
                q.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d), (w1[1:], w2, d)]) 
        
        m, n = len(word1), len(word2)
        cur = [_ for _ in range(n + 1)]
        for i in range(1, m + 1):
            pre, cur[0] = cur[0], i
            for j in range(1, n + 1):
                temp = cur[j]
                cur[j] = 1 + min(cur[j], pre - (word1[i - 1] == word2[j - 1]), cur[j - 1])
                pre = temp
        return cur[-1]
                
        m, n = len(word1), len(word2)
        pre, cur = [0] * (n + 1), [_ for _ in range(n + 1)]
        for i in range(1, m + 1):
            pre, cur = cur, pre
            cur[0] = i
            for j in range(1, n + 1):
                cur[j] = 1 + min(pre[j], pre[j - 1] - (word1[i - 1] == word2[j - 1]), cur[j - 1])
        return cur[-1]
    
        m, n = len(word1), len(word2)
        dp = [[j for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            dp[i][0] = i
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1] , dp[i][j - 1])
        return dp[-1][-1]


# RunTime: 44 ms
# 思路: 
from collections import deque
class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        visit, q = set(), deque([(word1, word2, 0)])
        while True:
            w1, w2, d = q.popleft()
            if (w1, w2) not in visit:
                if w1 == w2:
                    return d
                visit.add((w1, w2))
                while w1 and w2 and w1[0] == w2[0]:
                    w1, w2= w1[1:], w2[1:]
                d += 1
                q.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d), (w1[1:], w2, d)]) 


# RunTime: 88ms
# 思路: 递归 + 缓存 --> lru_cache
from functools import lru_cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m = len(word1)
        n = len(word2)

        @lru_cache(None)
        def helper(i,j):
            costs = []
            if i < 0:
                return j+1
            if j < 0:
                return i + 1
            if word1[i] == word2[j]:
                costs.append(helper(i-1, j-1))
            else:
                costs.append(1+min(helper(i-1,j), helper(i, j-1), helper(i-1,j-1)))
            return min(costs)

        return(helper(m-1,n-1))


# RunTimeL 124ms
# 思路: 递归 + 缓存
class Solution3:
    def minDistance(self, word1, word2):
        def helper(i, j):
            """
            Memoized solution
            same pattern as knapsack problem in terms of memo and max choosing of the three recursion
            """
            if i == len(word1) and j == len(word2):
                return 0
            # finish word1
            if i == len(word1):
                return len(word2) - j
            if j == len(word2):
                return len(word1) - i

            if (i, j) not in memo:
                if word1[i] == word2[j]:
                    ans = helper(i + 1, j + 1)
                else: 
                    insert = 1 + helper(i, j + 1)
                    delete = 1 + helper(i + 1, j)
                    replace = 1 + helper(i + 1, j + 1)
                    ans = min(insert, delete, replace)
                memo[(i, j)] = ans
            return memo[(i, j)]
        memo = {}
        return helper(0, 0)


# RunTime: 136ms
# 思路: 
class Solution4:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        t = list(reversed(range(n + 1)))
        for i in reversed(range(m)):
            r = m - i
            for j in reversed(range(n)):
                s = t[j + 1] if word1[i] == word2[j] else min(t[j], t[j + 1], r) + 1
                t[j + 1] = r
                r = s
            t[0] = r
        return t[0]


# RunTime: 144ms
# 思路: 动态规划, 空间复杂度优化
class Solution5:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        if m < n: return self.minDistance(word2, word1)
        dp = [i for i in range(n + 1)]
        for i in range(1, m + 1):
            prev, dp[0] = i - 1, i
            for j in range(1, n + 1):
                curr = dp[j]
                if word1[i-1] == word2[j-1]:
                    dp[j] = prev
                else:
                    dp[j] = min(dp[j-1], curr, prev) + 1
                prev = curr
        return dp[-1]