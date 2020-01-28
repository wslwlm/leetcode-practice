# 题目地址: https://leetcode.com/problems/permutations/
# Runtime: 36 ms Memory Usage: 12.7 MB
# 递归

class MySolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        res = []
        for i in range(len(nums)):
            tmpNums = nums[:i] + nums[i+1:]
            subNums = self.permute(tmpNums)
            for l in subNums:
                l.append(nums[i])
            res += subNums
        return res


# 回溯法
class MySolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return []
        
        res = []
        self.backtrack(nums, [], res)
        return res
        
    def backtrack(self, nums, path, res):
        if not nums:
            res.append(path.copy())
        else:
            for i, v in enumerate(nums):
                tmpNums = nums[:i] + nums[i+1:]
                self.backtrack(tmpNums, path + [v], res)


# RunTime: 24ms   
# 回溯法
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def permutation(res,tmp,nums):
            if len(nums)==0:
                res.append(tmp)
            else:
                for i in range(len(nums)):
                    #print('before:',i,tmp,nums)
                    permutation(res,tmp+[nums[i]],nums[:i]+nums[i+1:])
                    #print('after:',i,tmp,nums)
                    
        
        res=[]
        permutation(res,[],nums)
        return res


# RunTime: 20ms
# 提取元素, 然后通过添加元素与其组合
class bestSolution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]
        
        for num in nums:
            new_perm = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    new_perm.append(perm[i:] + [num] + perm[:i])
            perms = new_perm
        
        return perms