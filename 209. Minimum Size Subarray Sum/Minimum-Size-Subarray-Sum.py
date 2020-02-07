# 题目地址: https://leetcode.com/problems/minimum-size-subarray-sum/
# Runtime: 100 ms Memory Usage: 15.1 MB
# 思路: 滑动窗口的思想, 维护两个指针, 当小于s时就进行向前滑动, 否则就进行收缩

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0
        slow = fast = 0
        res = nums[0]
        length = 1
        minL = float('inf')
        
        while fast < len(nums)-1 or res >= s:
            if res < s:
                fast += 1
                length += 1
                res += nums[fast]
            else:
                minL = min(length, minL)
                res -= nums[slow]
                slow += 1
                length -= 1
                
        if minL== float('inf'):
            return 0
        return minL


# RunTime: 56ms
# 思路: 滑动窗口思想
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        start = 0
        currSum = 0
        res = len(nums) + 1
        for end in range(len(nums)):
            currSum += nums[end]
            while currSum >= s:
                res = min(res, end - start + 1)
                currSum -= nums[start]
                start += 1
        return res % (len(nums) + 1)