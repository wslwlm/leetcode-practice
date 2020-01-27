# 题目地址: https://leetcode.com/problems/number-of-1-bits/
# 转为二进制然后计数

class MySolution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# 通过 &1 来计数
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            ans += n&1
            n >>= 1
        
        return ans


class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)[2:]                              # 去除'0b'前缀
        return len([c for c in b if c == '1'])


# 思路比较新奇
# 这里用一个trick， 可以轻松求出。 就是n & (n - 1) 可以消除 n 最后的一个1的原理。
# trick原理, n-1 必使n的最后一个1翻转为0
class githubSolution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count