# 题目地址: https://leetcode.com/problems/reverse-bits/
# RunTime: 8ms
# 将n转为二进制然后翻转输出

class bestSolution:
    def reverseBits(self, n: int) -> int:
        bit = format(n, 'b')
        if len(bit) < 32:
            bit = "0"*(32-len(bit)) + bit
        return int(bit[::-1], 2)