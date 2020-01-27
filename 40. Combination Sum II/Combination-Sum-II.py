# 题目地址: https://leetcode.com/problems/combination-sum-ii/
# Runtime: 40 ms Memory Usage: 12.7 MB
# 类似 Combination Sum中的做法, 不过将相同元素跳过, 以及不能重复使用同一元素

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        if target == 0:
            return [[]]
        allList = []
        for i, v in enumerate(candidates):
            if target - v < 0:
                break
            if i > 0 and candidates[i] == candidates[i-1]:  # 将相同元素跳过
                continue
            subList = self.combinationSum2(candidates[i+1:], target - v)    # 不重用同一元素
            for l in subList:
                l.append(v)
            allList += subList
        return allList


# RunTime: 24ms
# 回溯法
from copy import deepcopy
class Solution:
    def combinationSum2(self, candidates, target):
    # Sorting is really helpful, se we can avoid over counting easily
        candidates.sort()                      
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result
    
    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider 
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return

        for i in range(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want 
            # to count the first element in this recursive step even if it is the same 
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is 
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]], 
                               result, target - nums[i])


# RunTime: 28ms
# 回溯法
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def helper(target,path,cand,i,res):
            if target == 0:
                res += path,
                return
            for c in range(i,len(cand)):
                if c > i and cand[c] == cand[c-1]:continue
                if cand[c] > target:break
                helper(target-cand[c],path+[cand[c]],cand,c+1,res)
        res = []
        candidates.sort()
        helper(target,[],candidates,0,res)
        return res