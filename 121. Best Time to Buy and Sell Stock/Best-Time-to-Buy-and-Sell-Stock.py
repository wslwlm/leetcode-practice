# 题目地址: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Runtime: 56 ms, Memory Usage: 13.8 MB
# 寻找各个位置的极点, 然后将极点之间相减

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lenPrices = len(prices)
        flag = True
        s = []
        b = []
        for i in range(lenPrices-1):
            if flag and prices[i] < prices[i+1]:
                flag = False
                s.append(prices[i])
            if not flag and prices[i] > prices[i+1]:
                flag = True
                b.append(prices[i])
        if not flag and prices[i] <= prices[i+1]:
            b.append(prices[i+1])
        sublen = len(s)
        for i in range(sublen):
            for j in range(i, sublen):
                profit = b[j] - s[i]
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit


# 记录当前最小, 然后用后面值减去当前最小
# RunTime: 40ms
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        maxProfit = 0
        minPrice = float('inf')
        
        for i in range(len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
                
            elif prices[i] - minPrice > maxProfit:
                maxProfit = prices[i] - minPrice
                
        return maxProfit