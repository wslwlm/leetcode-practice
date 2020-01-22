# 题目地址: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
# Runtime: 52 ms, Memory Usage: 13.9 MB
# 找极点的方法, 同121类似

class MySolution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lenPrices = len(prices)
        small = 0
        flag = True
        for i in range(lenPrices-1):
            if flag and prices[i] < prices[i+1]:
                small = prices[i]
                flag = False
            elif not flag and prices[i] > prices[i+1]:
                maxProfit += prices[i] - small
                flag = True
        if not flag and prices[i] <= prices[i+1]:
            maxProfit += prices[i+1] - small
        return maxProfit


# 通过 c - b + b - a = c - a 的道理, current_trade < 0 为极大点
# RunTime: 40ms
class bestSolution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices) - 1):
            current_trade = prices[i + 1] - prices[i]
            if current_trade > 0:
                max_profit += current_trade
                
        return max_profit