# 题目地址: https://leetcode.com/problems/longest-increasing-subsequence/
# Runtime: 848 ms, Memory Usage: 12.8 MB
# 动态规划 + 普通查找, 算法复杂度: O(N^2)

class MySolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        numsLen = len(nums)
        if numsLen < 2:
            return numsLen
        dp = [1]
        for i in range(1,numsLen):
            dp.append(max([dp[j] + 1 for j in range(i) if nums[j] < nums[i]] + [1]))      
        return max(dp)


# RunTime: 20ms
# 动态规划 + 二分查找, 算法复杂度: O(N*logN)
class bestSolution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = []
        
        for n in nums:
            if not dp or n > dp[-1]: dp.append(n)
            else:
                l,r = 0, len(dp) - 1
                while l <= r:
                    m = l + (r - l) // 2
                    if dp[m] > n: r = m - 1
                    elif dp[m] < n: l = m + 1
                    else:
                        l = m
                        break
                dp[l] = n
        return len(dp)

# 参考网址: https://blog.csdn.net/wbin233/article/details/77570070 (LIS算法: 最长上升子序列) 