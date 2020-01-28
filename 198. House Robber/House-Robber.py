# 题目地址: https://leetcode.com/problems/house-robber/
# Runtime: 28 ms Memory Usage: 12.7 MB
# 动态规划, 递归会TLE, 对于第ｉ个房子抢不抢, 抢的话就是dp[i-2]+nums[i-1], 不抢就是dp[i-1]
# dp数组存的是第ｉ个房子为止的最大金额

class MySolution:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        dp = [0] * (size+1)
        
        if size == 0:
            return 0
        elif size == 1:
            return nums[0]
        elif size == 2:
            return max(nums[0], nums[1])
        dp[0] = 0
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])
        
        for i in range(3, size+1):
            dp[i] = max(dp[i-1], nums[i-1] + dp[i-2])
        return dp[-1]


# RunTime: 8ms
# 空间复杂度进行优化由Ｏ(n)-->O(1), 本质还是动态规划
class bestSolution:
    def rob(self, nums: List[int]) -> int:
        prev1=0
        prev2=0
                
        for num in nums:
            tmp = prev1
            prev1 = max(num+prev2, prev1)
            prev2 = tmp
            
        return prev1