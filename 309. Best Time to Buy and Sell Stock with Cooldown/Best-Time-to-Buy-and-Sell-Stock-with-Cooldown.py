# 题目地址: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
# Runtime: 32 ms Memory Usage: 12.9 MB
# 思路: 使用三个状态, 两个数组buy和sell, buy数组表示的是以buy或cooldown结尾, sell数组表示以sell或cooldown结尾

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        elif n == 2:
            return max(0, prices[1]-prices[0])
        buy = [0] * n
        sell = [0] * n
        
        buy[0] = -prices[0]
        buy[1] = max(-prices[0], -prices[1])
        
        sell[0] = 0
        sell[1] = max(0, prices[1]-prices[0])
        
        for i in range(2, n):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        
        return max(buy[-1], sell[-1])


# RunTime: 16ms
# 思路: 动态规划, 空间复杂度优化为O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: return 0
        l = len(prices)
        if l == 0: return 0
        prev_sell, sell, buy = 0, 0, -prices[0]
        for price in prices[1:]:
            prev_buy = buy
            buy = max(prev_sell-price, buy)
            prev_sell = sell
            sell = max(prev_buy+price, sell)
        return sell