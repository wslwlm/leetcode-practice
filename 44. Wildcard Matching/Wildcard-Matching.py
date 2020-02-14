# 题目地址: https://leetcode.com/problems/wildcard-matching/
# Runtime: 1020 ms Memory Usage: 20.9 MB
# 思路: 动态规划, 

class MySolution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(p)
        m = len(s)
        
        dp = [[False]*(n+1) for _ in range(m+1)]
        
        dp[0][0] = True
        
        for i in range(1, n+1):
            if p[i-1] == "*":
                dp[0][i] = dp[0][i-1]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j] or dp[i-1][j-1]
                    
                elif p[j-1] == '?':
                    dp[i][j] = dp[i-1][j-1]
                else:
                    if s[i-1] == p[j-1]:
                        dp[i][j] = dp[i-1][j-1]

        return dp[m][n]


# RunTime: 24ms
# 思路: 
from functools import lru_cache
class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s)
        n = len(p)
        
        if n == 0:
            return m == 0
        
        i = 0
        j = 0
        
        si = -1
        pi = -1
        
        while j < n:
            if p[j] == '*':
                si = i
                pi = j
                j += 1
                if j == n:
                    return True
            else:
                if i < m:
                    if p[j] in (s[i], '?'):
                        i += 1
                        if j == n - 1 and i != m and pi >= 0:
                            si = i = m - j + pi
                            j = pi + 1
                        else:
                            j += 1
                    else:
                        if pi >= 0:
                            si += 1
                            i = si
                            j = pi + 1
                        else:
                            return False
                else:
                    break
                
        return j == n and (i == m or p[-1] == '*')


# RunTime: 28 ms
class Solution2:
    def isMatch(self, s, p):
        sL = len(s)
        pL = len(p)

        ptr_s = 0
        ptr_p = 0

        star_p = -1
        fallback_s = -1

        while True:
            if ptr_s == sL and ptr_p == pL: # string and pattern both reach the end match is success
                return True
            elif ptr_s == sL:   #   string reach the end but pattern is not, the math is failed
                if p[ptr_p] == '*': # handle edge case if string is empty
                    ptr_p += 1
                else:
                    return False
            elif ptr_p == pL: # pattern reach the end but string is not, continue fall back if star appears previously
                if star_p == -1:
                    return False
                else:           # perform fall back action
                    ptr_p = star_p + 1
                    ptr_s = fallback_s
                    fallback_s += 1
            else:   # normal case
                if s[ptr_s] == p[ptr_p]:    # if both char is the same
                    ptr_s += 1
                    ptr_p += 1
                elif p[ptr_p] == '?':       # if pattern matches any single character
                    ptr_s += 1
                    ptr_p += 1
                elif p[ptr_p] == '*':       # if star appears
                    star_p = ptr_p          # mark the star position
                    fallback_s = ptr_s + 1  # set the fall back position for next time
                    ptr_p += 1              # only move pattern pointer
                else:
                    if star_p == -1:        # no star appears before
                        return False        # match fails
                    else:                   # perform fall back action
                        ptr_p = star_p + 1
                        ptr_s = fallback_s
                        fallback_s += 1


# RunTime: 32ms
# 思路: 
class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        nexts = 1
        end_bit = 1<<len(s)
        d = collections.defaultdict(int)
        for i,c in enumerate(s):
            d[c] |= 1<<i
        for c in p:
            if c == '*':
                nexts =  (end_bit<<1) - (nexts & -nexts)
            elif c == '?':
                nexts <<= 1
            else:
                nexts = (nexts & d[c]) << 1
            if nexts == 0:
                return False
        return nexts & end_bit != 0


# RunTime: 36ms
# 思路: 
class Solution4:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        s_i, p_i = 0, 0
        star_i, s_t_i = -1, -1
        
        while s_i < s_len:
            if p_i < p_len and p[p_i] in ['?', s[s_i]]:
                p_i += 1
                s_i += 1
            elif p_i < p_len and p[p_i] == '*':
                star_i = p_i
                s_t_i = s_i
                p_i += 1
            elif star_i == -1:
                return False
            else:
                p_i = star_i + 1
                s_i = s_t_i + 1
                s_t_i = s_i
                
        return all(x=='*' for x in p[p_i:])


# RunTime: 112ms
# 思路: 
class Solution5:
    def isMatch(self, s: str, p: str) -> bool:
        def recursion(s, p, s_tmp, p_star):
            if len(s) == 0:
                return all(x == "*" for x in p)

            if len(p) > 0 and p[0] in ['?', s[0]]: return recursion(s[1:], p[1:], s_tmp, p_star)
            if len(p) > 0 and p[0] == '*':
                p_star = p
                s_tmp = s
                return recursion(s, p[1:], s_tmp, p_star)
            if p_star == "":
                return False
            s_tmp = s_tmp[1:]
            return recursion(s_tmp, p_star[1:], s_tmp, p_star)

        return recursion(s, p, "", "")


# RunTime: 224ms
# 思路: 
class Solution6:
# @return a boolean
    def isMatch(self, s, p):
        length = len(s)
        if len(p) - p.count('*') > length:
            return False
        dp = [True] + [False]*length
        for i in p:
            if i != '*':
                for n in reversed(range(length)):
                    dp[n+1] = dp[n] and (i == s[n] or i == '?')
            else:
                for n in range(1, length+1):
                    dp[n] = dp[n-1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]