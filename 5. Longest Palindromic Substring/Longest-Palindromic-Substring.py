# 题目地址: https://leetcode.com/problems/longest-palindromic-substring/
# RunTime: 32ms
class Solution:
    def longestPalindrome(self, s: str) -> str:
        str_len = len(s)
        # if length of string < 2 or s is palindrome already
        if str_len < 2 or s == s[::-1]:
            return s

        start, max_len = 0, 1

        # 一次遍历, 通过i指向当前元素(回文串的尾部), 将i-max_len的方式获得起始位置
        for i in range(1, str_len):
            odd_start = i - max_len - 1
            even_start = i - max_len
            odd = s[odd_start:i + 1]  # len(odd) = max_len + 2
            even = s[even_start:i + 1]  # len(even) = max_len + 1

            if odd_start >= 0 and odd == odd[::-1]:
                start = odd_start
                max_len += 2
            elif even_start >= 0 and even == even[::-1]:
                start = even_start
                max_len += 1
        return s[start:start + max_len]


# 动态规划的方法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :param s: str
        :return: str
          a b c b
        a 1 0 0 0
        b   1 0 1
        c     1 0
        b       1
        """
        dp = [[False for col in range(len(s))] for row in range(len(s))]
        length = 0
        max_length = 0
        start = 0
        end = 0
        while length < len(s):
            i = 0
            while i + length < len(s):
                j = i + length
                if length == 1 or length == 0:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                if dp[i][j] and max_length < length + 1:
                    max_length = length + 1
                    start = i
                    end = j
                i += 1
            length += 1

        return s[start:end+1]