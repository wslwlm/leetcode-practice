# 题目地址: https://leetcode.com/problems/3sum/
# Runtime: 724 ms Memory Usage: 16.1 MB
# 遍历 + 有序数组查找target, 遍历时间复杂度为O(n), 有序数组查找target时间复杂度为O(n), 总为O(n^2)

class MySolution:
    def threeSum(self, nums):
        sorted_nums = sorted(nums)
        threeSumRes = []
        for i in range(len(nums)):
            if sorted_nums[i] > 0:
                break
            if i > 0 and sorted_nums[i] == sorted_nums[i-1]:
                continue
            start = i+1
            end = len(nums) - 1
            target = -sorted_nums[i]
            while start < end:
                res = sorted_nums[start] + sorted_nums[end]
                if res > target:
                    end -= 1
                elif res < target:
                    start += 1
                else:
                    if not (threeSumRes and threeSumRes[-1][1] == sorted_nums[start] and threeSumRes[-1][2] == sorted_nums[end]):
                        threeSumRes.append([sorted_nums[i], sorted_nums[start], sorted_nums[end]])
                    start += 1
                    end -= 1
        return threeSumRes


# RunTime: 196ms
# 首先 a<b<c, 通过固定a, 然后确定b，再确定c 
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        from collections import defaultdict
        import bisect
        ans = []
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1
        nums = sorted(counter)
        for i, a in enumerate(nums):   # a < b < c, first fix a, then find b, then find c
            two_sum = 0 - a
            left = bisect.bisect_left(nums, two_sum - nums[-1], i + 1)   # the lower bound of b
            right = bisect.bisect_right(nums, two_sum // 2, left)        # the higher bound of b
            for b in nums[left:right]:
                c = two_sum - b
                if c in counter and c > b:
                    ans.append([a, b, c])     # three different elements
            if counter[a] >= 2:
                c = 0 - 2*a
                if c in counter and c != a:
                    ans.append([a, a, c])     # two different elements
                if counter[a] >= 3:
                    if a*3 == 0:
                        ans.append([a, a, a])
        return ans