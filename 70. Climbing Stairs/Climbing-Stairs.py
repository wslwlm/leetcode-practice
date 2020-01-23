# 题目地址: https://leetcode.com/problems/climbing-stairs/
# Runtime: 20 ms Memory Usage: 12.6 MB
# 一维DP问题, 可以进行空间复杂度优化, 将O(n)优化为O(1)

class MySolution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        dp = [1, 2]
        for i in range(2, n):
            dp.append(dp[i-1] + dp[i-2])
        return dp[-1]


# RunTime: 8ms
# 一样思路, 可以使用递归实现, 但是会TLE
class bestSolution:
    def climbStairs(self, n: int) -> int:
        # if n == 1:
        #     total = 1
        #     return total
        # if n ==2:
        #     total =2
        #     return total
        # else: 
        #     total = self.climbStairs(n-1) + self.climbStairs(n-2)
        # return total
        
        if n ==1:
            return n
        elif n ==2:
            return n
        s = [1,2]
        for i in range(2, n):
            s.append(s[i-1]+s[i-2])
        return s[-1]