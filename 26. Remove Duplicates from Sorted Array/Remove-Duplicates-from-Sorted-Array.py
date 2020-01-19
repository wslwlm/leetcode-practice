# 题目地址: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 倒序删除列表中重复元素
# 列表中删除元素, 倒序与正序区别: https://www.cnblogs.com/bananaplan/p/remove-listitem-while-iterating.html
# 正序会跳过; 倒序会向前填充, 不会跳过
# Runtime: 88 ms, Memory Usage: 14.4 MB
class MySolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        flag = None
        diff = 1
        i = 0
        for i in range(len(nums)-1, -1, -1):
            if flag == nums[i]:
                nums.pop(i)
            else:
                flag = nums[i]
                diff += 1
            i += 1
        return diff

# 不使用删除而是将列表前面元素填充
# Runtime: 60 ms
class BestSolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1223
        i = 0
        n = len(nums)
        last = None
        for num in nums:
            if num != last:
                nums[i] = num
                i += 1
            last = num
        return i     

# github作者地址: https://github.com/azl397985856/leetcode/blob/master/problems/26.remove-duplicates-from-sorted-array.md

# 双指针
# 使用快慢指针来记录遍历的坐标。
# 开始时这两个指针都指向第一个数字
# 如果两个指针指的数字相同，则快指针向前走一步
# 如果不同，则两个指针都向前走一步
# 当快指针走完整个数组后，慢指针当前的坐标加1就是数组中不同数字的个数
class githubSolution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums:
            slow = 0
            for fast in range(1, len(nums)):
                if nums[fast] != nums[slow]:
                    slow += 1
                    nums[slow] = nums[fast]
            return slow + 1
        else:
            return 0 