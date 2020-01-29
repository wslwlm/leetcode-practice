# 题目地址: https://leetcode.com/problems/ugly-number/
# Runtime: 24 ms Memory Usage: 12.8 MB
# 递归

class MySolution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        elif num == 1:
            return True
    
        if  num in [2,3,5]:
            return True
        
        for i in [2,3,5]:
            d, l = divmod(num, i)
            if l == 0:
                return self.isUgly(d)
        return False


# RunTime: 
# 循环
class Solution:
    def isUgly(self, num: int) -> bool:
        if num < 1:
            return False
        facs = [2, 3, 5]
        for fac in facs:
            while  num%fac == 0:
                    num //=fac
        return num == 1


# RunTime: 8ms
# 暴力解
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        
        while num%2 == 0:
            num /= 2
        
        while num%3 == 0:
            num /= 3
        
        while num%5 == 0:
            num /= 5
            
        if num == 1:
            return True
        else:
            return False