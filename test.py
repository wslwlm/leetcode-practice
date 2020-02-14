class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        
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

triangle = [1,2,3,4,3,5,3,2]
print(Solution().rob(triangle))