# 题目地址: https://leetcode.com/problems/interleaving-string/
# Runtime: 44 ms Memory Usage: 12.8 MB
# 思路: 

class MySolution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        k = len(s3)
        
        if k != (m+n):
            return False
        
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        
        for i in range(1, m+1):
            dp[i][0] = (dp[i-1][0] and s1[i-1] == s3[i-1])
            
        for i in range(1, n+1):
            dp[0][i] = (dp[0][i-1] and s2[i-1] == s3[i-1])
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1] or dp[i][j-1] and s2[j-1] == s3[i+j-1])
                
        print(dp)
        return dp[m][n]


# RunTimme: 12 ms
# 思路: 递归 + 缓存
class Solution1:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        self.ans = False
        
        lookup = [[-1] * l2 for _ in range(l1)]
        
        
        def interleave(i,j,k):
            nonlocal l1, l2
            if self.ans: return True
            if i == l1:
                self.ans = s2[j:] == s3[k:]
                return self.ans
            if j == l2:
                self.ans= s1[i:] == s3[k:]
                return self.ans
            if lookup[i][j] >= 0: return lookup[i][j]
            res = False
            if i < l1 and s1[i] == s3[k]: res = res or interleave(i + 1,j,k+1)
            if j < l2 and s2[j] == s3[k]: res = res or interleave(i,j + 1,k+1)
            lookup[i][j] = res
            return res
            
        interleave(0,0,0)
        
        return self.ans


# RunTime: 20 ms
# 思路: 同上, 传参数不同
from functools import lru_cache
class Solution2:
    
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:        
        if len(s3) != len(s1) + len(s2): return False
        
        @lru_cache(None)
        def helper(s1,s2,s3):
            if not s1: return s2 == s3
            if not s2: return s1 == s3    
            return (s1[0] == s3[0] and helper(s1[1:],s2,s3[1:])) or (s2[0] == s3[0] and helper(s1, s2[1:],s3[1:]))                    
        return helper(s1,s2,s3)


# RunTime: 24 ms
# 思路: 使用栈的思路去实现递归, dfs, 将可能性的路径压入栈中
class Solution3:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        # This can be solved the standard DFS way (iterative approach)
        
        r = len(s1)
        c = len(s2)
        
        if r + c != len(s3):
            return False
        
        stack = []
        visited = set()
        
        stack.append((0,0))
        
        while stack:
            i,j = stack.pop()
            
            if i + j  == len(s3):
                return True
            
            if i+1 <= r and s1[i] == s3[i+j] and (i+1,j) not in visited:
                visited.add((i+1,j))
                stack.append((i+1,j))
            
            if j+1 <= c and s2[j] == s3[i+j] and (i,j+1) not in visited:
                visited.add((i,j+1))
                stack.append((i, j+1))
        
        return False