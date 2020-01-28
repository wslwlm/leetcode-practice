# 题目地址: https://leetcode.com/problems/permutations-ii/
# RunTime: 52ms
# 递归法

class MySolution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(set(nums)) == 1:
            return [nums]
        res = []
        for i, v in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tmpNums = nums[i+1:] + nums[:i]
            subList = self.permuteUnique(tmpNums)
            for l in subList:
                l.append(v)
            res += subList
        return res

    
# RunTime: 52ms
# 回溯法
class MySolution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []
        
        nums.sort()
        
        res = []
        self.backtrack(nums, [], res)
        return res
    def backtrack(self, nums, path, res):
        if len(set(nums)) == 1:
            res.append(path + nums)
        else:
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                tmpNums = nums[i+1:] + nums[:i]
                self.backtrack(tmpNums, path+[nums[i]], res)


# RunTime: 40ms
# 排列组合法：每一步都是排列好的, 所以主要考虑插入位置
class bestSolution:
    def permuteUnique(self, nums):
        permutations = [[]]
    
        for head in nums:
            permutations = [rest[:i]+[head]+rest[i:] for rest in permutations for i in range((rest+[head]).index(head)+1)]
            print(permutations)
        
        return permutations

bestSolution().permuteUnique([1,2,2,1])


# RunTime: 36ms
# 回溯法
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        solution = []
        combination = []
        
        self.findPermutations(nums, combination, solution)
        return solution
    
    def findPermutations(self, nums, combination, solution):
        if nums == []:
            solution.append(list(combination))
            return
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            combination.append(nums[i])
            new_nums = nums[:i] + nums[i+1:]
            self.findPermutations(new_nums, combination, solution)
            combination.pop()