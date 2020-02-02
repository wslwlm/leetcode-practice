# 题目地址: https://leetcode.com/problems/powx-n/
# Runtime: 32 ms Memory Usage: 12.8 MB
# 取巧的方法, 普通递归和循环都会TLE

class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n


# 切分奇数和偶数, 偶数--> x^n = x^(n//2), 奇数则减一
class githubSolution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        return self.myPow(x*x, n // 2) if n % 2 == 0 else x * self.myPow(x, n - 1)


# 使用位运算, 比如, x^10 = x^(1010)2 --> x^8 * x^2, 从高向低位移, 判断最低位是否为1
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = 1
        while n:
            if n & 1 == 1:
                res *= x
            x *= x
            n >>= 1
        return res