# 题目地址: https://leetcode.com/problems/contains-duplicate-ii
# Runtime: 92 ms Memory Usage: 20.4 MB

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = {}
        for i,v in enumerate(nums):
            if v in c:
                if i - c[v] <= k:
                    return True
                else:
                    c[v] = i
            else:
                c[v] = i
        return False


# 简化操作
class githubSolution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index, num in enumerate(nums):
            if num in d and index - d[num] <= k:
                return True
            d[num] = index
        return False


# RunTime: 72ms
# 维护一个集合, 当集合长度超过k时, 删除元素
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        windows = set()
        for i in range(len(nums)):
            if nums[i] in windows:
                return True
            windows.add(nums[i])
            if len(windows) > k:
                windows.remove(nums[i-k])
        return False