# 题目地址: https://leetcode.com/problems/palindrome-partitioning/
# Runtime: 88 ms Memory Usage: 13.1 MB
# 思路: 递归法, 将包含第一个字母的回文串作为递归起始

class Solution:
    def partition(self, s: str):
        if not s:
            return [[]]

        n = len(s)
        res = []
        for i in range(1, n+1):
            if s[:i] == s[:i][::-1]:
                for l in self.partition(s[i:]):
                    l = [s[:i]] + l
                    res.append(l)

        return res


# RunTime: 48ms
# 思路: 类似动态规划, mem存的是第i个字符所对应的回文列表
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        self.s = s
        self.find_sub_palindromes()
        n = len(s)
        mem = [None] * n # all partitions till i
        mem[0] = [[ s[0] ]]
        for i in range(1, len(s)):
            mem[i] = []
            for j in range(i+1):
                if self.ispalindrome[j][i]:
                    current = [s[j:i+1]]
                    if j == 0:
                        mem[i].append(current)
                    else:
                        for prefix in mem[j-1]:
                            mem[i].append(prefix + current)
        return mem[-1]
    
    def find_sub_palindromes(self):
        s, n = self.s, len(self.s)
        # is s[i:j+1] a palindrome
        self.ispalindrome = [[False] * n for _ in range(n)]
        # 以每个i为中心点, 寻找回文串, 这是奇数串
        for i in range(n):
            d = 0
            l, r = i - d, i + d
            while 0 <= l and r < n and s[l] == s[r]:
                self.ispalindrome[l][r] = True
                d += 1
                l, r = i - d, i + d
        # 这是偶数串
        for i in range(n-1):
            d = 0
            l, r = i - d, i+1 + d
            while 0 <= l and r < n and s[l] == s[r]:
                self.ispalindrome[l][r] = True
                d += 1
                l, r = i - d, i+1 + d


# RunTime: 44ms
# 思路: 考虑当添加一个新字符对当前字符串的影响
# 当添加一个新字符时, "aab" --> "aaba"
#  [
#    ["aa","b"],       ==>     ["aa", "b", "a"]
#    ["a","a","b"]     ==>     ["a", "a", "b", "a"] 和 ["a", "aba"]
#  ]
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        X = [[]]
        for x in s:
            for _ in range(len(X)):
                y = X.pop(0)
                X.append(y + [x])
                
                n = len(y)
                if n > 0 and y[-1] == x:
                    X.append(y[:-1] + [x * 2])
                
                if n > 1 and y[-2] == x:
                    X.append(y[:-2] + [y[-2] + y[-1] + x])
        
        return X


# RunTime: 56ms
# 思路: 
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        dp = [[] for _ in range(N)]
        # 构造dp数组, 使数组下标为回文串左边界, 数组内容为回文串右边界
        for i in range(N):
            j = 0
            while i - j >= 0 and i + j < N and s[i-j] == s[i+j]:
                dp[i-j].append(i+j+1)
                j+=1
            j = 1
            while i - j + 1 >= 0 and i + j < N and s[i-j+1] == s[i+j]:
                dp[i-j+1].append(i+j+1)
                j+=1
        que = [(0, [])]
        res = []
        print(dp)
        # 通过dp数组中的左右边界实现回文串跳跃, 当跳到 len(s) 时加入到res数组中
        while que:
            idx, apath = que[-1]
            que.pop()
            if idx == N: res.append(apath)
            else:
                for e in dp[idx]:
                    que.append((e, apath + [s[idx:e]]))
        return res


# 思路: 回溯法
class githubSolution:
    def partition(self, s: str) -> List[List[str]]:
        """回溯法"""
        
        res = []
        
        def helper(s, tmp):
            """
            如果是空字符串，说明已经处理完毕
            否则逐个字符往前测试，判断是否是回文
            如果是，则处理剩余字符串，并将已经得到的列表作为参数
            """
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])
        
        helper(s, [])
        return res


# RunTime: 80ms
# 思路: 回溯法
class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtrack(s, [], res)
        return res
    
    def backtrack(self, s: str, path: List[str], res:List[List[str]]):
        if not s:
            res.append(path[:])
            return
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.backtrack(s[i:], path + [s[:i]], res)