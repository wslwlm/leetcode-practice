# 题目地址: https://leetcode.com/problems/bitwise-and-of-numbers-range/
# Runtime: 56 ms Memory Usage: 12.7 MB
# 思路: 只有位于 2^m~2^(m+1)中的数的 & 结果不为0, 然后再对差值进行操作

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        
        tmp = 0xFFFFFFFF
        i = 1
        while i * 2 <= m:
            i *= 2
        
        if n >= i * 2:
            return 0
        else:
            i = 1
            # 差值中存在 2^2 ==> 第三位必为0, 因为差为4的两个值第三位必须一个为1, 一个为0
            while i <= n-m:
                i *= 2
                tmp <<=1
                m &= tmp
            return m


# RunTime: 32ms
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        if m == n:
            return n
        # converting to binary, ignoring 0b
        a = bin(m)[2:]
        b = bin(n)[2:]
		# we are having bit-wise and between consecutive numbers
        if len(a) != len(b):
            return 0
        
        res = ""
        # 高位相同进行保留, 不同则代表n为1, m为0, 则剩余位都为0.
        for i in range(len(a)):
            if a[i] == b[i]:
                res += a[i]
            else:
                break
        # all the rest are zeros
        res += (len(a)-len(res))*"0"
        return int(res,2)


# RunTime: 36ms
# 思路: 仍然是寻找相同高位
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        
        shift = 0
        
        # find the common MSB bits.
        while m != n:
            
            m = m >> 1
            n = n >> 1
        
            shift += 1
        
        
        return m << shift


# RunTime: 40ms
# 思路: 消除最低位1
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n = n & (n - 1)
        return n