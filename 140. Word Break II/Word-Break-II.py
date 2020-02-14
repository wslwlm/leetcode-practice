# 题目地址: https://leetcode.com/problems/word-break-ii/
# Runtime: 48 ms Memory Usage: 12.8 MB
# 思路: 递归 + 缓存, 动态规划会TLE, 递归缓存可以将前面遍历过的字符串缓存下来

class MySolution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        return self.helper(s, wordDict, {})
    
    def helper(self, s, wordDict, rec):
        if s in rec:
            return rec[s]
        
        if not s:
            return ['']
        
        res = []
        
        for word in wordDict:
            if s.startswith(word):
                for l in self.helper(s[len(word):], wordDict, rec):
                    res.append(word + ("" if not l else " " + l))
        rec[s] = res
        return res


# RunTime: 20 ms
# 思路: 递归 + 缓存
class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = {}
        wordDict = set(wordDict)
        if len(wordDict) == 0:
            return []
        max_len = float('-inf')
        for word in wordDict:
            max_len = max(max_len, len(word))
        
        def dp(i):
            if i in cache:
                return cache[i]

            ans = []
            j = i
            while j < len(s) and j - i <= max_len:
                if s[i:j] in wordDict:
                    suffixes = dp(j)
                    for suffix in suffixes:
                        ans.append(s[i:j] + " " + suffix)
                j += 1
            if s[i:] in wordDict:
                ans.append(s[i:])

            cache[i] = ans
            return ans
        
        return dp(0)


# RunTime: 24 ms
# 思路: 先判断是否可拆分, 如果可拆分则dfs, dfs为往前走word, 直到len(s), 比较像backtrack
class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        shortest = float('inf')
        longest = 0
        dict = {}
        dp = [False for _ in range(len(s))]
        for word in wordDict:
            dict[word] = 1
            length = len(word)
            if length > longest:
                longest = length
            if length < shortest:
                shortest = length
        len_s = len(s)
        if shortest > len_s:
            return []
        res = []
        cur = []

        def dfs(pin=0):
            if pin == len_s:
                res.append(' '.join(cur))
            for i in range(shortest, longest + 1):
                if s[pin:pin + i] in dict:
                    cur.append(s[pin:pin + i])
                    dfs(pin + i)
                    cur.pop()
        for i in range(shortest - 1, len_s):
            for j in range(i - longest + 1, i - shortest + 2):
                if j < 0:
                    continue
                if (j == 0 or dp[j - 1]) and s[j:i + 1] in dict:
                    dp[i] = True
                    break
        if dp[-1]:
            dfs()
        return res