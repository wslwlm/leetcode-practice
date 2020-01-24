# 题目地址: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Runtime: 76 ms Memory Usage: 13.1 MB
# 分别从头尾开始搜索, 时间复杂度为O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while True:
            res = numbers[start] + numbers[end]
            if res > target:
                end -= 1
            elif res < target:
                start += 1
            else:
                return [start+1, end+1]

        
# RunTime: 44ms
# 一样思路
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        suming = numbers[i] + numbers[j]
        while suming != target:
            if suming > target:
                j = j - 1
            elif suming < target:
                i = i + 1
            suming = numbers[i] + numbers[j]
        return [i+1,j+1]
