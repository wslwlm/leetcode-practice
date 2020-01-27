# 题目地址: https://leetcode.com/problems/search-in-rotated-sorted-array/
# Runtime: 32 ms Memory Usage: 12.9 MB
# 找到转折点 --> 二分查找

class Solution:
    def search(self, nums, target: int) -> int:
        numsLen = len(nums)
        i = numsLen - 1
        
        while i > 0 and nums[i-1] < nums[i]:
            i -= 1
        
        start = i - numsLen
        end = i - 1
        
        while start <= end:
            tmpMid = (end + start)//2
            mid = (tmpMid + numsLen)%numsLen
            if nums[mid] > target:
                end = tmpMid - 1
            elif nums[mid] < target:
                start = tmpMid + 1
            else:
                return mid
        return -1


# RunTime: 24ms
# 根据转折点的位置调整二分查找算法        
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        
        if nums[l] == target:   return l
        elif nums[r] == target:   return r
        while l < r:
            mid = (l + r)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[l]:                          # 处于转折点左边
                if nums[l] > target or nums[mid] < target:   # [4,5,6,7,0,1,2] or [2,4,5,6,7,0,1] 两种搜索模式, 比mid大和比left小
                    l = mid + 1                              #        ^                  ^
                else:
                    r = mid
            else:
                if nums[r] < target or nums[mid] > target:
                    r = mid
                else:
                    l = mid + 1
        return -1


# RunTime: 20ms
# 通过二分查找找到转折点, 然后二分查找找到元素
class Solution:
    # sliding window
    # trees?
    # dp
    # recursion with dfs
    # nested intervals
    # -7-6-5-4-3-2-1
    #  0 1 2 3 4 5 6
    # [4,5,6,7,0,1,2]
            
    def search(self, nums: List[int], target: int) -> int:
        # find the minimum number by iterating through the array once
        # have that number be the low index for searching (negative)
        # high index is positive index of number before it
        # (low, high) = self.findMinIndex(nums)
        # offset = self.findOffset(nums)
        n = len(nums)
        low = 0
        high = n - 1
        
        # find rotation index
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
                
        rot = low
        low = 0
        high = n - 1
        
        # binary search but with additional rotation
        while low <= high:
            mid = (low + high) // 2
            realMid = (rot + mid) % n
            if nums[realMid] == target:
                return realMid
            if target < nums[realMid]:
                high = mid - 1
            else:
                low = mid + 1
        return -1