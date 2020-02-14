# 题目地址: https://leetcode.com/problems/ugly-number-ii/
# Runtime: 148 ms Memory Usage: 12.7 MB
# 思路: 参见 https://www.cnblogs.com/grandyang/p/4743837.html
# 从三个序列中选取合适的值

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = i3 = i5 = 0
        l = 1
        while l < n:
            m2 = nums[i2] * 2
            m3 = nums[i3] * 3
            m5 = nums[i5] * 5
            
            mn = min(m2, m3, m5)
            if m2 == mn: i2 += 1
            if m3 == mn: i3 += 1
            if m5 == mn: i5 += 1
        
            nums.append(mn)
            l += 1

        return nums[n-1]


# RunTime: 20 ms
# 思路: 从 乘2, 乘3, 乘5 的序列中挑选按顺序的值
class Ugly(object):
    def __init__(self):
        self.nums = nums = [1,]
        i2 = i3 = i5 = 0
        
        for i in range(1690):
            ugly = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            
            nums.append(ugly)
            
            if nums[i2]*2 == ugly:
                i2+=1
            if nums[i3]*3 == ugly:
                i3+=1
            if nums[i5]*5 == ugly:
                i5+=1

class Solution1:            
    u = Ugly()   
    
    def nthUglyNumber(self, n: int) -> int:
        return self.u.nums[n-1]