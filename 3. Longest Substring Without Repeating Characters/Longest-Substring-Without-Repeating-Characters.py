# 题目地址: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# 列表存储然后用in来进行重复判断, in会造成RunTime增加, index也会造成时间增加
# Runtime: 64 ms Memory Usage: 12.7 MB
class MySolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxS = []
        k = 0
        lsub = 0
        for i in range(len(s)):
            if s[i] in maxS:
                p = maxS.index(s[i])
                maxS = maxS[p+1: ]
                k = k - p - 1
            maxS.append(s[i])
            k += 1
            if lsub < k:
                lsub = k
        return lsub


# 字典存储, 减少了in和index使用的时间
# RunTime: 24ms
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = cur_len = 0
        cache = {}
        cur_len = 0
        for i, c in enumerate(s):
            if c not in cache or i - cur_len > cache[c]:
                cur_len += 1
                cache[c] = i
                if cur_len > max_len:
                    max_len = cur_len
            else:
                cur_len = i - cache[c]
                cache[c] = i
        return max_len