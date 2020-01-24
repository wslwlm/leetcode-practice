# 题目地址: https://leetcode.com/problems/single-number/
# Runtime: 84 ms Memory Usage: 15.2 MB
# 用字典存储元素并进行查询

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        rec = {}
        for i in nums:
            if i not in rec:
                rec[i] = 1
            else:
                rec[i] += 1
        for k, v in rec.items():
            if v == 1:
                return k


# 使用位运算符: 按位异或, 因为题目表明为2次, 按位异或两次为0, 所以剩下那个就是单独的数
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans ^= i
        return ans