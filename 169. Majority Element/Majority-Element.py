# 题目地址: https://leetcode.com/problems/majority-element/
# Runtime: 168 ms Memory Usage: 14.1 MB (判题服务器有波动)
# 思路简单不赘述

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsDict = {}
        numsSet = set(nums)
        numsLen = len(nums)
        for i in numsSet:
            if nums.count(i) > numsLen // 2:
                return i


# RunTime: 148ms
# 思路简单不赘述, sort的性能竟然这么好
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]       