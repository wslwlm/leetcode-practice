# 题目地址: https://leetcode.com/problems/permutation-sequence/
# Runtime: 24 ms Memory Usage: 12.7 MB
# 逐个数字进行挑选, 首先挑出第一个, 然后把它从数组移除, 再挑其他数字

class MySolution:
    def getPermutation(self, n: int, k: int) -> str:
        l = [i for i in range(1, n+1)]
        res = ''
        c = 1
        # 求n-1对应的阶乘
        for i in range(1, n):
            c = c*i
    
        k -= 1
        while n > 1:
            ind = int(k//c)
            res += str(l[ind])
            l.remove(l[ind])
            k %= c
            c = c//(n-1)
            n -= 1
        res += str(l[0])           
        return res


# RunTime: 12ms
# 一样的思路
class bestSolution:
    def getPermutation(self, n: int, k: int) -> str:
        # k是从1开始计数的
        #factorial_cache[i] 对应 i+1的阶乘
        factorial_cache = [1]*n
        remain_nums = [1]*n
        factorial = 1
        for i in range(1, n-1):
            factorial *= i+1
            factorial_cache[i] = factorial
            remain_nums[i] = i+1
        remain_nums[n-1] = n
        result = []
        tmp = k -1 

        for i in range(n-2, -1, -1):
            factorial_i = factorial_cache[i]
            idx = tmp // factorial_i
            result.append(str(remain_nums[idx]))
            del remain_nums[idx]
            tmp = tmp % factorial_i
        result.append(str(remain_nums[tmp]))
        return ''.join(result)


# 类似的思想
import math

class githubSolution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        candidates = [str(i) for i in range(1, n + 1)]

        while n != 0:
            facto = math.factorial(n - 1)
            # i 表示前面被我们排除的组数，也就是k所在的组的下标
            # k // facto 是不行的， 比如在 k % facto == 0的情况下就会有问题
            i = math.ceil(k / facto) - 1
            # 我们把candidates[i]加入到结果集，然后将其弹出candidates（不能重复使用元素）
            res += candidates[i]
            candidates.pop(i)
            # k 缩小了 facto *  i
            k -= facto * i
            # 每次迭代我们实际上就处理了一个元素，n 减去 1，当n == 0 说明全部处理完成，我们退出循环
            n -= 1
        return res