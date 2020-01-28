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


# 动态规划的方法, dp储存的是i到j这一段是否为回文串, 如果i+1到j-1为回文串且s[i]==s[j] ==> i到j为回文
# 递推式: dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
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


# Manacher算法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        string_size = len(s)
        if string_size < 3:
            if s==s[::-1]:
                return s
            else:
                return s[0]

        manacher_str = "#"
        for index in range(len(s)):
            manacher_str += s[index]
            manacher_str += "#"

        LPS_table = [0]*len(manacher_str)
        center = 1
        max_right = 2
        max_length = 0
        LPS_center = 0

        total_size = len(manacher_str)
        for index in range(1, len(manacher_str)):
            if index < max_right:
                LPS_table[index] = min(LPS_table[2*center-index], max_right-index)
            else:
                LPS_table[index] = 0

            # when calculating LPS value, self position (index) is not included
            while (index-LPS_table[index]-1 >= 0 and
                   index+LPS_table[index]+1 < total_size and
                   manacher_str[index-LPS_table[index]-1] == manacher_str[index+LPS_table[index]+1]):
                   LPS_table[index] += 1

            if LPS_table[index] > max_length:
                max_length = LPS_table[index]
                LPS_center = index

            if LPS_table[index]+index-1 > max_right:
                max_right = LPS_table[index]+index-1
                center = index

        start = int((LPS_center-max_length)/2)
        return s[start: start+max_length]


# 通过Manacher算法中的预处理, 只用判断奇数串即可
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        s = '#'.join(s)
        s = '#' + s + '#'
        head = 0
        maxlen = 1
        for rd_tail in range(2, len(s)):
            rd_head = rd_tail - maxlen - 1
            rd_s = s[rd_head: rd_tail + 1]
            if rd_s == rd_s[::-1] and rd_head >= 0:
                head = rd_head
                maxlen += 2
        return s[head: head + maxlen].replace('#','')


# Manacher算法参考链接:
# https://mp.weixin.qq.com/s/EiJum3-44TqXZN4apuSQUQ
# https://windliang.cc/2019/06/24/%E4%B8%80%E6%96%87%E8%AE%A9%E4%BD%A0%E5%BD%BB%E5%BA%95%E6%98%8E%E7%99%BD%E9%A9%AC%E6%8B%89%E8%BD%A6%E7%AE%97%E6%B3%95/
# https://segmentfault.com/a/1190000008484167