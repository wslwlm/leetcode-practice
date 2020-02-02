# 题目地址: https://leetcode.com/problems/subsets-ii/
# Runtime: 28 ms Memory Usage: 12.8 MB
# 通过用一个字典存储subsets的长度, 在nums中两个相同元素的情况下, 只对s[i-2]后的元素进行组合

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        s = {-1:1}
        res = [[]]
        
        valid = 0
        for i, num in enumerate(nums):
            tmp = []
            if i > 0 and nums[i-1] == nums[i]:
                for r in res[s[i-2]:]:
                    tmp.append(r + [num])
            else:
                for r in res:
                    tmp.append(r + [num])
            res += tmp
            s[i] = len(res)
        return res


# RunTime: 20ms
# 思路: 回溯法, 重复项则continue掉
class bestSolution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], res)


# RunTime: 24ms
# 思路: start变量记录下前两个的subsets的长度, 类似s[i-2], 遇到相同元素则用从start开始
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        nums.sort()
        start = 0
        for i, n in enumerate(nums):
            if i == 0 or n != nums[i-1]:
                start = 0
            curr = []
            for s_ind in range(start, len(subsets)):
                curr.append(subsets[s_ind] + [n])
            start = len(subsets)
            subsets += curr  
            
        return subsets


# RunTime: 32ms
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def helper(chosen, subset):
            if len(subset) == 0:
                a = tuple(chosen)
                if a not in seen:
                    result.append(chosen)
                    seen[a] = 1
            else:
                helper(chosen+[subset[0]], subset[1:])
                helper(chosen, subset[1:])
            
        seen = {}
        result = []
        nums.sort()
        helper([], nums)
        return result