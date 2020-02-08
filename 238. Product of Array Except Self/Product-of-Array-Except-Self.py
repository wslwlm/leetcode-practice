# 题目地址: https://leetcode.com/problems/product-of-array-except-self/
# Runtime: 116 ms Memory Usage: 19.4 MB
# 思路: 两次遍历, 一次正向遍历, 一次反向遍历.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rec = nums[:]
        rec[0] = 1
        c = 1
        for i in range(1, n):
            c *= nums[i-1]
            rec[i] = c

        c = 1
        for i in range(n-2, -1, -1):
            c *= nums[i+1]
            rec[i] = rec[i] * c
        return rec