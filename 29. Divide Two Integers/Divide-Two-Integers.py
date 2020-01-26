# 题目地址: https://leetcode.com/problems/divide-two-integers/
# Runtime: 24 ms Memory Usage: 12.8 MB
# 使用类似除法计算时的思想

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        pos = (dividend > 0) is (divisor > 0)
        allS = 0
        res = abs(dividend)
        _divisor = abs(divisor)
        if res < _divisor:
            return 0
        while res >= _divisor:
            tmpDivisor = _divisor
            s = 1
            while tmpDivisor <= res:
                tmpDivisor = tmpDivisor << 1
                s = s << 1
            tmpDivisor = tmpDivisor >> 1
            s = s >> 1
            res -= tmpDivisor
            allS += s
        if not pos:
            allS = -allS
        return min(max(-2147483648, allS), 2147483647)

# RunTime: 20ms
# 翻倍减去
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        二分法
        :param int divisor
        :param int dividend
        :return int
        """
        # 错误处理
        if divisor == 0:
            raise ZeroDivisionError
        if abs(divisor) == 1:
            result = dividend if 1 == divisor else -dividend
            return min(2**31-1, max(-2**31, result))

        # 确定结果的符号
        sign = ((dividend >= 0) == (divisor >= 0))
        
        result = 0
        # abs也可以直接写在while条件中，不过可能会多计算几次
        _divisor = abs(divisor)
        _dividend = abs(dividend)
        
        while _divisor <= _dividend:
            r, _dividend = self._multi_divide(_divisor, _dividend)
            result += r
        
        result = result if sign else -result

        # 注意返回值不能超过32位有符号数的表示范围
        return min(2**31-1, max(-2**31, result))
    
    def _multi_divide(self, divisor, dividend):
        """
        翻倍除法，如果可以被除，则下一步除数翻倍，直至除数大于被除数，
        返回商加总的结果与被除数的剩余值；
        这里就不做异常处理了；
        :param int divisor
        :param int dividend
        :return tuple result, left_dividend
        """
        result = 0
        times_count = 1
        while divisor <= dividend:
            dividend -= divisor
            result += times_count
            times_count += times_count
            divisor += divisor
        return result, dividend


# RunTime: 16ms
# 翻倍减去, 类似的思想, 不过时间没有浪费在翻倍的过程中
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


# RunTime: 12ms
# 使用log的特性, 这个取巧牛批
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        elif divisor == 1:
            return dividend
        ret = math.log(abs(dividend)) - math.log(abs(divisor))
        ret = int(math.exp(ret))
        
        if dividend*divisor >= 0:
            return min(2**31-1, ret)
        else:
            return max(-1*2**31+1, -ret)