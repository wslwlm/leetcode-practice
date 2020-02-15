# 题目地址: https://leetcode.com/problems/burst-balloons/
# Runtime: 524 ms Memory Usage: 13 MB
# 思路: 分治法+动态规划, 首先考虑k是区间[i, j]最后一个被戳爆的气球, 则k两边 [i, k-1] 和 [k+1, j] 相互独立
# 两区间相互独立后, 写出状态转移方程, dp[i][j] = dp[i][k-1] + dp[k+1][j] + nums[k]*nums[i-1]*nums[i+1]
# 因为k是最后一个被戳爆的气球, dp[i][j]代表[i, j]闭区间的硬币数

class Solution1:
    def maxCoins(self, nums) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        dp = [[0]*(n+2) for _ in range(n+2)]
        
        for length in range(1, n+1):
            for i in range(1, n-length+2):
                j = i + length - 1
                for k in range(i, j+1):
                    dp[i][j] = max(dp[i][j], dp[i][k-1] + dp[k+1][j] + nums[k]*nums[i-1]*nums[j+1])
        
        return dp[1][n]


# RunTime: 460ms
# 思路: 递归 + 缓存, 类似动态规划的思路, 用递归写出来
from functools import lru_cache

class Solution2:
    def maxCoins(self, nums: List[int]) -> int:

        # reframe the problem
        nums = [1] + nums + [1]

        # cache this
        @lru_cache(None)
        def dp(left, right):

            # no more balloons can be added
            if left + 1 == right: return 0

            # add each balloon on the interval and return the maximum score
            return max(nums[left] * nums[i] * nums[right] + dp(left, i) + dp(i, right) for i in range(left+1, right))

        # find the maximum number of coins obtained from adding all balloons from (0, len(nums) - 1)
        return dp(0, len(nums)-1)


# RunTime: 224ms
# 思路: 同上
class Solution3:
    def maxCoins(self, nums: List[int]) -> int:
        nums=[1]+[x for x in nums if x]+[1]
        n=len(nums)
        a=[[0]*n for _ in range(n)]
        for i in range(n-2,-1,-1):
            for j in range(i+2,n):
                t=nums[i]*nums[j]
                a[i][j]=max(a[i][k]+nums[k]*t+a[k][j] for k in range(i+1,j))
        return a[0][-1]