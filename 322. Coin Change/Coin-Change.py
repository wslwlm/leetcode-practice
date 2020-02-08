# 题目地址: https://leetcode.com/problems/coin-change/
# Runtime: 1796 ms Memory Usage: 12.9 MB
# 思路: 动态规划

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        coins.sort()
        minA = coins[0]
        
        dp = [-1]*(amount+1)
        dp[0] = 0
        
        for i in range(minA, amount+1):
            minC = float('inf')
            for j in coins:
                if j > i:
                    break
                if dp[i-j] != -1:
                    minC = min(dp[i-j]+1, minC)
            dp[i] = minC
        
        if dp[amount] == float('inf'):
            return -1
        return dp[amount]


# RunTime: 40ms
# 思路: 从最大数值硬币开始搜索, 然后更新 min_coins, 然后通过比较缩小搜索空间, 
class Solution:
    def coinChange(self, coins, amt):
        def helper(num_coins, remaining, i, min_coins):
            coin = coins[i]

            # 搜索到可用值
            if not remaining % coin:
                return min(num_coins + remaining // coin, min_coins)

            # 未搜索到可用值
            if i is len(coins) - 1:
                return min_coins

            # 从最大硬币面值开始, 看remianing中能取多少个当前硬币
            for j in range(remaining // coin, -1, -1):
                if (num_coins + j) - (remaining - coin*j)//-coins[i + 1] < min_coins:
                    min_coins = min(helper(num_coins + j, remaining - coin * j, i + 1, min_coins), min_coins)

            return min_coins

        coins.sort(reverse=True)
        min_coins = helper(0, amt, 0, amt + 1)
        if min_coins == amt + 1:
            return -1
        return min_coins


# RunTime: 72 ms
# 思路: 类似递归, remianing - coins[i] ==> 下一次递归输入的remaining 
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        if not amount :
            return 0
        
        coins.sort(reverse = True)
        self.min_coins = amount + 1
        
        def dfs(start_coin, coin_count, remaining_amount) :
            if remaining_amount in coins :
                self.min_coins = min(self.min_coins, coin_count)
                
            for i in range(start_coin, len(coins)) :
                if remaining_amount > coins[i] * (self.min_coins - coin_count) :
                    break
                
                if remaining_amount >= coins[i] :
                    dfs(i, coin_count + 1, remaining_amount - coins[i])
                    
        dfs(0, 1, amount)
        
        return self.min_coins if self.min_coins != amount + 1 else -1