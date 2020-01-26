# 题目地址: https://leetcode.com/problems/sum-of-two-integers/
# Runtime: 36 ms Memory Usage: 12.6 MB
# 通过 &(进位) 和 ^(不进位加法), python3中的int没有溢出的大整数, 所以要进行移位检验
# 参考: https://www.jianshu.com/p/21fd1598d4ae

class MySolution:
    def getSum(self, a: int, b: int) -> int:
        if not a:
            return b
        elif not b:
            return a
        
        while b:
            a, b = (a^b)&0xFFFFFFFF, (a&b)<<1
        return a if a >> 31 == 0 else a - 4294967296


class bestSolution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)