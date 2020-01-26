# 题目地址: https://leetcode.com/problems/factorial-trailing-zeroes/
# Runtime: 44 ms Memory Usage: 12.6 MB
# 求出阶乘中存在多少个5

class MySolution:
    def trailingZeroes(self, n: int) -> int:
        i = 0
        while n:
            n = n // 5
            i += n
        return i


# RunTime: 8ms
# 一样的思路, 它运行时间短的原因有可能是变量转换的问题
class bestSolution:
    # @return an integer
    def trailingZeroes(self, n):
        factor, count = 5, 0
        
        while True:
            curCount = n // factor
            if not curCount:
                break
            
            count += curCount
            factor *= 5

        return count