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