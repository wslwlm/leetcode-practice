# 题目地址: https://leetcode.com/problems/sort-colors/
# Runtime: 32 ms Memory Usage: 12.8 MB
# 复制一个数组遍历一遍并将原数组中的 0, 2 排好, 然后剩下即为 1 的位置
# 1. 遍历两遍数组, 第一遍记录, 第二遍写入. 
# 2. 遍历一遍数组, 排前后, 中间自然排好

class MySolution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums
        tmp = nums.copy()
        l = 0
        h = n - 1
        for n in tmp:
            if n == 0:
                nums[l] = 0
                l += 1
            elif n == 2:
                nums[h] = 2
                h -= 1
        for i in range(l, h+1):
            nums[i] = 1


# RunTime: 12 ms
# 思路: 标记两个点: start, end. 然后cur指针从start->end遍历, 有0和start交换, 有1和end交换
class bestSolution:
    def sortColors(self, nums: List[int]) -> None:
        
        start = 0
        end = len(nums) - 1
        
        while end >= 0 and nums[end] == 2:
            end -= 1
        
        while start < len(nums) and nums[start] == 0:
            start += 1
        
        curr = start
        
        while curr < len(nums):
            if nums[curr] == 0 and curr > start:
                nums[curr], nums[start] = nums[start], nums[curr]
                start += 1
                curr -= 1
            elif nums[curr] == 2 and curr < end:
                nums[curr], nums[end] = nums[end], nums[curr]
                end -= 1
                curr -= 1
            curr += 1


# 类似上面的思路
class githubSolution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0 = cur = 0
        p2 = len(nums) - 1
        
        while cur <= p2:
            if nums[cur] == 0:
                nums[cur], nums[p0] = nums[p0], nums[cur]
                p0 += 1
                cur += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1