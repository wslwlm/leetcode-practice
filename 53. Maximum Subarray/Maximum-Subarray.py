# Runtime: 44 ms Memory Usage: N/A
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        countlist = []
        for i, e in enumerate(nums):
            count += e
            if i < len(nums) - 1:
                if nums[i+1] >= 0:
                    if count < 0:
                        count = 0
            if count >= 0:
                countlist.append(count)
        if countlist:
            return max(countlist)
        else:
            return max(nums)

# Runtime: 68 ms Memory Usage: 13.4 MB
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        start = None
        sum = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                start = i
                break
        if start is None:
            return max(nums)
        
        end = start
        lsum = 0
        while end < len(nums):
            for i in nums[start:]:
                sum += i
                end += 1
                if sum < 0:
                    start = end
                    sum = 0
                    break
                else:
                    if sum > lsum:
                        lsum = sum
                    
        return lsum