# 题目地址: https://leetcode.com/problems/subsets/
# Runtime: 28 ms Memory Usage: 13 MB
# 排列组合法, [[]] --> [[], [1]] --> [[], [1], [2], [1, 2]] --> [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

class MySolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            tmp = []
            for r in res:
                tmp.append(r + [num])
            res += tmp
        return res


# 回溯法
# RunTime: 32ms
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        self.backtrack(nums, [], res)
        return res
    
    def backtrack(self, nums, path, res):
        res.append(path)
        if not nums:
            return
        for i in range(len(nums)):
            self.backtrack(nums[i+1:], path+[nums[i]], res)


# RunTime: 12ms
# 递归加排列组合
class bestSolution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        if len(nums) == 0:
            return res
        else:
            res = []
            for item in self.subsets(nums[1:]):
                res.append(item)
                res.append([nums[0]] + item)
            return res


# 回溯法
# RunTime: 16ms
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        
        def helper(items, path):
            result.append(path)
            if not items:
                return
            for i, item in enumerate(items):
                helper(items[(i+1):], path + [item])
                
        helper(nums, [])
        return result