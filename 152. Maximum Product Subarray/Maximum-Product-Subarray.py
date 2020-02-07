# 题目地址: https://leetcode.com/problems/maximum-product-subarray/
# Runtime: 60 ms Memory Usage: 15.1 MB
# 思路: 动态规划, 其实不是很必要, 同时存最大值和最小值

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
 
        dp = [0] * n
        
        dp[0] = (nums[0], nums[0])
        
        for i in range(1, n):
            if nums[i] > 0:
                dp[i] = (max(dp[i-1][0]*nums[i], nums[i]), min(dp[i-1][1]*nums[i], nums[i]))
            else:
                dp[i] = (max(dp[i-1][1]*nums[i], nums[i]), min(dp[i-1][0]*nums[i], nums[i]))
        return max(dp[i][0] for i in range(n))


# RunTime: 36ms
# 思路: 乘积的最大值不是在数组头部就是在尾部, 只有0能隔开最大值
# 所以一次遍历, 两个数组中找到最大值即可
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        A = nums[::-1]
        for i in range(1, len(nums)):
            A[i] *= A[i-1] or 1
            nums[i] *= nums[i-1] or 1
        return max(A+nums)