# 题目地址: https://leetcode.com/problems/jump-game/
# Runtime: 108 ms Memory Usage: 14.8 MB
# 动态规划, 好像又不是动态规划

class MySolution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        dp = [False] * n
        dp[0] = True
        dp[1] = (nums[0] != 0)
        for i in range(1, n):
            for j in range(1, i+1):
                if dp[i-j] and nums[i-j] >= j:
                    dp[i] = True
                    break
        return dp[n-1]


# 思路: 从前往后回溯
# 用一个变量记录当前能够到达的最大的索引，我们逐个遍历数组中的元素去更新这个索引。 变量完成判断这个索引是否大于数组下表即可
class githubSolution:
    def canJump(self, nums: List[int]) -> bool:
        """思路同上"""
        _max = 0
        _len = len(nums)
        for i in range(_len-1):
            if _max < i:
                return False
            _max = max(_max, nums[i] + i)
            # 下面这个判断可有可无，但提交的时候数据会好看点
            if _max >= _len - 1:
                return True
        return _max >= _len - 1


# RunTime: 68ms
# 从后往前的回溯
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) < 2: return True
        furthest = len(nums) - 1
        for x in range(len(nums) - 2, -1, -1):
            if nums[x] + x >= furthest: furthest = x
            if furthest == 0: return True
        return furthest == 0