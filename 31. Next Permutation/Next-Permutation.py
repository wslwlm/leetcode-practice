# 题目地址: https://leetcode.com/problems/next-permutation/
# Runtime: 36 ms Memory Usage: 12.7 MB
# 排列规律: 寻找增量最小的排列
# [3, 1, 4, 3, 2] --> 1为所找元素, 替换 ==> [3, 2, 4, 3, 1] 后部分翻转 ==> [3, 2, 1, 3, 4]
#     ^                                        ^       ^
     

class MySolution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        end = numsLen - 1
        while end > 0 and nums[end] <= nums[end-1]:
            end -= 1
        
        if end == 0:
            nums.sort()
            return
        
        tmp = nums[end-1]
        start = end - 1
        end = numsLen - 1
        
        while end > 0 and tmp >=nums[end]:
            end -= 1
        
        nums[start] = nums[end]
        nums[end] = tmp
        
        start += 1
        end = numsLen - 1
        
        while start < end:
            tmp = nums[start]
            nums[start] = nums[end]
            nums[end] = tmp
            
            start += 1
            end -= 1



# RunTime: 20ms
# 一样的思路
class bestSolution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=j=len(nums)-1
        while i>0 and nums[i]<=nums[i-1]:
                i-=1
        if i==0:
            nums.reverse()
            return
        k=i-1
        while nums[k]>=nums[j]:
            j-=1
        nums[k],nums[j]=nums[j],nums[k]
        l=k+1
        r=len(nums)-1
        while l<r:
            nums[l],nums[r]=nums[r],nums[l]
            l+=1
            r-=1