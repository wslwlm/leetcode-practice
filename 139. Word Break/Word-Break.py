# 题目地址: https://leetcode.com/problems/word-break/
# Runtime: 36 ms Memory Usage: 12.8 MB
# 思路: 动态规划, 第i个状态 --> 第j状态为True和s[j:i]在wordDict中

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        maxlen = max([len(s) for s in wordDict])
        n = len(s)
        dp = [0] * (n+1)
        
        dp[0] = True
        
        for i in range(1, n+1):
            for j in range(i-maxlen, i):
                if s[j:i] in wordDict:
                    if dp[j]:
                        dp[i] = True
        return dp[n]


# RunTime: 12ms
# 思路: 递归, 查找域缩小, 将字符串s按word进行切割, 同时将结果储存起来, 避免重复计算
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        X = {}
        def wordBreak_(x):
            if x not in X:
                X[x] = False
                for word in wordDict:
                    if x.startswith(word):
                        n = len(word)
                        if len(x) == n or wordBreak_(x[n:]):
                            X[x] = True
                            break
            
            return X[x]
        
        return wordBreak_(s)


# RunTime: 16ms
# 思路: 从左往右查找
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 当前python3的set是有序的
        n, all_lens = len(s), set([len(w) for w in wordDict])
        res = [False] * n
        for l in all_lens:
            if l <= n and s[0:l] in wordDict:
                res[l-1] = True
        for i in range(1,n):
            if res[i-1] == True:
                for l in all_lens:
                    if i+l <= n and s[i:i+l] in wordDict:
                        res[i+l-1] = True
                    elif i+l > n:
                        # set无序的话这里应该用continue
                        break
        return res[-1]


# RunTime: 20ms
# 思路: 动态规划, 第i个状态向前逐单词查找
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict: 
                if w == s[i-len(w)+1: i+1] and(i-len(w) == -1 or dp[i-len(w)]):
                    dp[i] = True
                    break
        return dp[-1]


# RunTime: 28ms
# 思路: 队列实现, 从左到右, 不断更新end, 当end为len(s)时表示可拆分
from collections import deque
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        que= deque([0])
        vis=[0]*len(s)
        while que:
            start = que.popleft()
            if vis[start] ==0:
                for end in range(start+1, len(s)+1):
                    if s[start: end] in wordDict:
                        que.append(end)
                        if end == len(s):
                            return True
                    
                vis[start] = 1                
                
        return False


# RunTime: 36ms
# 思路: 递归+缓存
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        seen = {}
        return self.helper(s, words, seen)
            
            
    def helper(self, s, words, seen):
        if not s:
            return True
        
        res = False
        for i in range(1, len(s) + 1):
            if s[:i] in seen:
                res = seen[s[:i]]
            else:
                if s[:i] in words:
                    res = res or self.helper(s[i:], words, seen)
                seen[s[:i]] = res
                
        return seen[s]