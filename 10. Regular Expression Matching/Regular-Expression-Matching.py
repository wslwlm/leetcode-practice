# 题目地址: https://leetcode.com/problems/regular-expression-matching/
# Runtime: 48 ms Memory Usage: 12.9 MB
# 思路: 动态规划, 根据遇到的字符进行判断, '*'情况较多, '.'匹配任何字符, 普通字符比较相等即可

class MySolution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)
        m = len(s)
        
        dp = [[False]*(n+1) for _ in range(m+1)]
        
        dp[0][0] = True
        
        for i in range(2, n+1):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-2]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or \
                                (dp[i-1][j] and i>1 and (s[i-1] == p[j-2] or p[j-2] == '.')) or \
                                (dp[i-1][j-1] and i>1 and s[i-1] == s[i-2])
                    
                elif p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if s[i-1] == p[j-1]:
                        dp[i][j] = dp[i-1][j-1]

        for i in range(m+1):
            print(dp[i])
        return dp[m][n]


# RunTime: 20ms
# 思路: 递归 + 缓存
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        mem = {}
        
        def match(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            
            if j == len(p):
                res = i == len(s)
            
            else:
                first_match = i != len(s) and p[j] in {'.', s[i]}
                if j < len(p) - 1 and p[j + 1] == '*':
                    # 出现'*', 有两种可能性, '*'匹配0个 --> 删除当前字符, '*' 匹配一个到多个
                    res = match(i, j + 2) or (first_match and match(i + 1, j))
                else:
                    # 不出现'*', 情况容易判断
                    res = first_match and match(i + 1, j + 1)
            
            mem[(i, j)] = res
            return res
        return match(0, 0)