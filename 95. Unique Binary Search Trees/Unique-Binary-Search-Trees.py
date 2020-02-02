# 题目地址: https://leetcode.com/problems/unique-binary-search-trees/
# Runtime: 28 ms Memory Usage: 12.8 MB
#
# 具体算法:
# 生成一个[1:n + 1] 的数组
# 我们遍历一次数组，对于每一个数组项，我们执行以下逻辑
# 对于每一项，我们都假设其是断点。断点左侧的是 A，断点右侧的是 B。
# 那么 A 就是 i - 1 个数， 那么 B 就是 n - i 个数
# 用一个hashmap将 A 和 B 的结果相乘储存起来。

class MySolution:
    def numTrees(self, n: int) -> int:
        s = {0:1, 1:1, 2:2}
        
        for i in range(3, n+1):
            s[i] = 0
            for j in range(1, i+1):
                s[i] += s[j-1]*s[i-j]
        return s[n]


# RunTime: 12ms
# 用列表代替hashmap储存结果
class bestSolution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0],G[1] = 1,1
        for i in range(2,n+1):
            for j in range(1,n+1):
                G[i] += G[j-1]*G[i-j]
        return G[n]


# 思路: 暴力递归会TLE, 使用hashmap将结果存起来, 避免递归中的重复计算
class githubSolution:
    visited = dict()

    def numTrees(self, n: int) -> int:
        if n in self.visited:
            return self.visited.get(n)
        if n <= 1:
            return 1
        res = 0
        for i in range(1, n + 1):
            res += self.numTrees(i - 1) * self.numTrees(n - i)
        self.visited[n] = res
        return res