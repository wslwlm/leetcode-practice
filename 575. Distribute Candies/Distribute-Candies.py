# 题目地址: https://leetcode.com/problems/distribute-candies/
# Runtime: 944 ms Memory Usage: 14.6 MB
# 种类数和sister数量比较

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        count= {}
        for candy in candies:
            count[candy] = count.get(candy, 0) + 1
        
        n = int(len(candies)/2)
        m = len(count.keys())
        
        if n <= m:
            return n
        else:
            return m


# RunTime: 832ms
# 类似想法
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        total_candies = len(candies)
        unique_candies = len(set(candies))
        return min(unique_candies, total_candies // 2)