# 题目地址: https://leetcode.com/problems/increasing-triplet-subsequence/
# Runtime: 88 ms Memory Usage: 13.6 MB
# 思路: 维护一个Min和Len保存当前的序列最大值和最大长度, 另外维护一个tempMin和tempLen来保存备选项来进行替换

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        Min = nums[0]
        Sec = None
        Len = 1
        
        tempMin = None
        tempLen = 0
        
        for i in nums[1:]:
            if i > Min:
                Sec = Min
                Min = i
                Len += 1
            else:
                if Sec and i > Sec:
                    Min = i
                if tempMin is None:
                    tempMin = i
                    tempLen = 1
                elif tempMin > i and tempLen == 1:
                    tempMin = i
                elif tempMin < i:
                    tempMin = i
                    tempLen += 1
                if tempLen == Len:
                    Min = tempMin
                    tempMin = None
                    tempLen = 0
            if Len == 3:
                return True
        return False


# RunTine: 36 ms
# 思路: 依次找到三个数字，其顺序是递增的。因此我们的做法可以是依次遍历， 然后维护三个变量，分别记录最小值，第二小值，第三小值。只要我们能够填满这三个变量就返回true，否则返回false。
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = float('inf')
        second = float('inf')
        
        for n in nums:
            
            if n <= first:
                # lowest number till now
                first = n
            
            elif n <= second:
                # a number exists which is greater than first number
                second = n
            
            else:
                # a number exists which is greater than first and second number
                return True
        return False