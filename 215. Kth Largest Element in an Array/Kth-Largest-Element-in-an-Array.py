# 题目地址: https://leetcode.com/problems/kth-largest-element-in-an-array/
# Runtime: 60 ms Memory Usage: 13.5 MB
# 思路: 排序, 时间复杂度: O(n*logn)
# 其他思路: 堆排序: 维护大小为K的小顶堆
# 快排, 方案见: https://github.com/azl397985856/leetcode/blob/master/problems/215.kth-largest-element-in-an-array.md

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums