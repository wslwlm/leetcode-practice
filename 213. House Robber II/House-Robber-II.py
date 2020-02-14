# 题目地址: https://leetcode.com/problems/house-robber-ii/
# Runtime: 28 ms Memory Usage: 12.8 MB
# 思路: 动态规划, 由于第一个房子和最后一个房子连接, 所以有两种情况, 第一种选第一个房子, 另一种则不选第一个房子

class MySolution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        if n==1:
            return nums[0]
        
        dp = [0] * (n+1)
        dp1 = [0] * (n+1)
        
        dp[1] = nums[0]
        dp1[1] = 0
        
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
            dp1[i] = max(dp1[i-1], nums[i-1] + dp1[i-2])
            
        print(dp)
        print(dp1)
        return max(dp[n-1], dp1[n])


# RunTime: 16ms
# 思路: 动态规划, rob(h[1:]), rob(h[:-1])
class Solution1:
    def rob(self, h: List[int]) -> int:
        # case of giving up first + case of giving up last = all cases
        if h is None or not h:
            return 0
        if len(h) <= 3:
            return max(h)

        # problem_198, dp solution, rob a street
        def rob_st(h):
            if len(h) <= 2:
                return max(h)
            h[2] += h[0]
            for i in range(3, len(h)):
                h[i] += max(h[i-2], h[i-3])
            return max(h[-1], h[-2])
        
        return max(rob_st(h[1:]), rob_st(h[:-1]))


# RunTime: 28ms
# 思路: 动态规划, 空间复杂度优化为O(1)
class Solution2:
    def rob(self, nums: List[int]) -> int:
        def robb(num):
            prev = cur = 0
            for n in num:
                prev, cur = cur, max(n+prev, cur)
            return cur
        
        return max(robb(nums[len(nums) != 1:]), robb(nums[:-1]))