# 题目地址: https://leetcode.com/problems/combination-sum/
# Runtime: 48 ms Memory Usage: 12.8 MB
# 递归搜索, 为防止重复, 每次递归的都是子序列

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        if target == 0:
            return [[]]
        allList = []
        for i, v in enumerate(candidates):
            if target - v < 0:
                break
            subList = self.combinationSum(candidates[i:], target - v)
            for l in subList:
                l.append(v)
            allList += subList
        return allList


# RunTime: 32ms
# 一样的思路, 不过它是将path作为一个在递归中传递的参数, 不断更新path, 在target为0时将其添加到结果中
class bestSolution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        mini = candidates[0]
        res = []
        def rec_find(target, start, end, path):
            if target == 0:
                res.append(path)
            for i in range(start, end + 1):
                cur = candidates[i]
                if cur > target: break
                rem = target - cur
                if rem and rem < mini: continue
                rec_find(rem, i, end, path + [cur])
        rec_find(target, 0, len(candidates) - 1, [])
        return res


# 回溯法
# 类似的思想
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        回溯法，层层递减，得到符合条件的路径就加入结果集中，超出则剪枝；
        主要是要注意一些细节，避免重复等；
        """
        size = len(candidates)
        if size <= 0:
            return []
        
        # 先排序，便于后面剪枝
        candidates.sort()
        
        path = []
        res = []
        self._find_path(target, path, res, candidates, 0, size)
        
        return res
        
    def _find_path(self, target, path, res, candidates, begin, size):
        """沿着路径往下走"""
        if target == 0:
            res.append(path.copy())
        else:
            for i in range(begin, size):
                left_num = target - candidates[i]
                # 如果剩余值为负数，说明超过了，剪枝
                if left_num < 0:
                    break
                # 否则把当前值加入路径
                path.append(candidates[i])
                # 为避免重复解，我们把比当前值小的参数也从下一次寻找中剔除，
                # 因为根据他们得出的解一定在之前就找到过了
                self._find_path(left_num, path, res, candidates, i, size)
                # 记得把当前值移出路径，才能进入下一个值的路径
                path.pop()

# backtrack解题公式可参考github解法， 核心思想还是递归写法
# leetcode上回溯法的模板参考链接: 
# https://leetcode.com/problems/combination-sum/discuss/16502/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partitioning)