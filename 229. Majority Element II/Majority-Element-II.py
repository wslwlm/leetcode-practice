# 题目地址: https://leetcode.com/problems/majority-element-ii/
# Runtime: 128 ms Memory Usage: 13.8 MB
# 思路: hashmap记录, 然后大于n//3的加入结果

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        rec = {}
        res = []
        n = len(nums)
        
        for i in nums:
            if i in rec:
                rec[i] += 1
            else:
                rec[i] = 1
        for k, v in rec.items():
            if v > n//3:
                res.append(k)
                
        return res


# RunTime: 100ms
# 思路: 投票法, 这里投票法成立的证明是, 首先假设极限情况, 设超过n//3的数有1个, 设其数量为K1, 数组最大长度为3*K1-1
# 除了K1个数之外还有2*K1-1个数(必为奇数), 投票极限情况: K1-(N-(N-K1+1)/2) = (3*K1+1-N)/2 > 0, 所以投票可行.
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        firstVal, firstCnt = 0, 0
        secondVal, secondCnt = 0, 0
        for num in nums:
            if num == firstVal:
                firstCnt += 1
            elif num == secondVal:
                secondCnt += 1
            elif not firstCnt:
                firstVal = num
                firstCnt = 1
            elif not secondCnt:
                secondVal = num
                secondCnt = 1
            else:
                firstCnt -= 1
                secondCnt -= 1
                
        return [x for x in set([firstVal, secondVal]) if nums.count(x) > len(nums) // 3]