# 题目地址: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# Runtime: 52 ms Memory Usage: 12.5 MB
# 思路: 计数, 如果大于2则不写入, 小于2写入. 双指针: i, j

class MySolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count = 0
        j = 0
        last = nums[0]
        for i, v in enumerate(nums):
            if v == last:
                count += 1
            else:
                last = v
                count = 1
            if count <= 2:
                nums[j] = nums[i]
                j += 1
        return j


# 由于是有序数组, 所以可以比较当前和前K个位置, 相同则不存, 不同则存
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 写指针
        i = 0
        K = 2
        for num in nums:
            if i < K or num != nums[i-K]:
                nums[i] = num
                i += 1
        return i


# RunTime: 36ms
# 思路: left计算当两个指针的差值, 当出现计数大于 2 的则差值加 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 
        left = 0
        w = nums[0]
        k = 1
        for i in range(1,len(nums)):
            if nums[i]==w:
                k += 1
                if k>2:
                    left += 1
            else:
                k = 1
                w = nums[i]
            
            nums[i-left] = nums[i]
        l = len(nums)    
        del nums[l-left:]