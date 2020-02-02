# 题目地址: https://leetcode.com/problems/decode-ways/
# Runtime: 32 ms Memory Usage: 12.6 MB
# 动态规划, 根据dp[i-1]和dp[i-2]来确定dp[i], 但是和 0 有关系

class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
                
        dp = [0] * n
        dp[0] = 1
        
        num = int(s[:2])
        if num < 27:
            if num%10 == 0:
                dp[1] = 1
            else:
                dp[1] = 2
        else:
            if num%10 == 0:
                return 0
            else:
                dp[1] = 1
        
        for i in range(2, n):
            num = int(s[i-1:i+1])
            if num == 0:
                return 0
            if num < 27:
                if num%10 == 0:
                    dp[i] = dp[i-2]
                elif num < 10:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
            else:
                if num%10 == 0:
                    return 0
                else:
                    dp[i] = dp[i-1]
        return dp[-1]


# RunTime: 32ms
# 动态规划, 相对于前面简化, 子问题为 dp[i] = 以自身去编码（一位） + 以前面的元素和自身去编码（两位）
# 第一种是这个元素本身（需要自身是[1,9]）, 第二种是它和前一个元素组成[10, 26]
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
                
        dp = [0] * (n+1)
        dp[0] = 1 
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n+1):
            num1 = int(s[i-2:i])
            num2 = int(s[i-1])
            if num1 <= 26 and num1 >=10:
                dp[i] = dp[i-2]
            if num2 >= 1 and num2 <= 9:
                dp[i] += dp[i-1]
        return dp[-1]


# RunTime: 12ms
class Solution:
    def numDecodings(self, s: str) -> int:
        # Fuck these cases.
        if s is '0':
            return 0
        # Dynamic array; we only need 3 terms at a time -- the one we're calculating, and the two before.
        dp = [0] * 3
        # Base: There's only one way to (trivially) partition the empty string; you don't.
        dp[0] = 1
        # Loop structure: We need the ith element to always be set to 0, no matter how long the input is.
        # Can't simply say dp[i] = 0, since we're capping len(dp) at 3.
        # Fix: Use modulus 3 -- result will always be a number between [0,2], perfect for our indexing needs.
        # Start loop above base, including i = len(s) since that's what we're calculating.
        for i in range(1, len(s) + 1):
            # Per above, Reset current term.
            dp[i % 3] = 0
            # Recurrence relation, using modulus logic of above.
            if s[i - 1] != '0':
                dp[i % 3] += dp[(i - 1) % 3]
            # Same logic, but need to make sure we don't index out by trying to access dp[i-2].
            if i >= 2 and '10' <= s[i - 2:i] <= '26':
                dp[i % 3] += dp[(i - 2) % 3]

        # This is a bottom-up solution -- the last calculation is the result.
        return dp[len(s) % 3]


# RunTime: 16ms
# 一样的思路, 只不过是用prev和ss指代两个指针, 然后n和nps指代当前ways和前一ways
class Solution:
    def numDecodings(self, s: str) -> int:
        n = 0  # number of ways
        nps = 0  # number of ways in which previous number standalone
        if s[0] == '0':
            return 0
        for i, ss in enumerate([int(x) for x in s]):
            if not n:
                n = 1
                nps = 1
            else:
                if not ss:  # only one interpretation
                    if not prev or prev > 2:
                        return 0
                    n = nps
                    nps = 0
                elif 10*prev + ss < 27:  # possible two-digit character
                    temp = n
                    n = nps*2 + (n-nps)
                    nps = temp
                else:
                    nps = n
            prev = ss
        return n


# RunTime: 20ms
# 避免重复计算, 使用memo表将计算后的结果储存起来, 这样不会TLE, 直接递归会TLE
class Solution:
    def numDecodings(self, s: str) -> int:
        return self.helper(s, {})
    
    def helper(self, s, memo):
        if len(s) == 0:
            return 1
        if s[0] == '0':
            return 0
        if s not in memo:
            temp = 0
            if len(s) >= 2 and int(s[:2]) <= 26:
                temp += self.helper(s[2:], memo)
            temp += self.helper(s[1:], memo)
            memo[s] = temp
        return memo[s]


# RunTime: 24ms
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        
        dep, idep = 0, 1
        for i in range(1,len(s)):
            if s[i] == '0':
                if s[i-1] != '1' and s[i-1] != '2':
                    return 0
                else:
                    dep = idep
                    idep = 0
            else:
                og_idep = idep
                idep = idep + dep                
                if int(s[i-1:i+1]) >= 11 and int(s[i-1:i+1]) <=26:
                    dep = og_idep
                else: dep = 0
        return (dep+idep) 


# RunTime: 24ms
class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        dp = [0]*len(s)
        dp[0] = 1
        for i in range(1,len(s)):
            if int(s[i]) : dp[i] = dp[i-1]
            p = int(s[i-1:i+1])
            if p <= 26 and p >=10 :
                if i > 1 :
                    dp[i] += dp[i-2]
                else :
                    dp[i] +=1
            if dp[i] == 0 :
                return 0
        return dp[-1]  