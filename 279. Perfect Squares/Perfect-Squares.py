# 题目地址: https://leetcode.com/problems/perfect-squares/
# Runtime: 6360 ms Memory Usage: 12.8 MB
# 思路: 动态规划, 时间复杂度高

class Solution:
    def numSquares(self, n: int) -> int:
        if n < 4:
            return n
        dp = [0] * (n+1)
        
        for i in range(4):
            dp[i] = i
        
        for i in range(4, n+1):
            m = int(math.sqrt(i))
            temp = float('inf')
            for j in range(2, m+1):
                temp = min(dp[i-j**2]+1, temp)
            dp[i] = temp
        return dp[n]


# RunTime: 16ms
# 思路：四平方定理（任何一个整数都可以表示成四个数的平方和）
# 1.由于一个数如果含有因子4，那么我们可以把4都去掉，并不影响结果
# 2.等于4的情况：如果一个数除以8余7的话，那么肯定是由4个完全平方数组成
# 3.等于2或者1的情况：如果一个数由2个平方数组成，如果其中一个平方数是0，那么就是1，如果不是0，那就是2。
# 4.等于3的情况：其他
def num_squares(n: int) -> int:
    """
    https://leetcode.com/problems/perfect-squares/solution/
    Approach 5: Mathematics
    Time complexity: O(sqrt(n))
​    Space complexity: O(1)
    """
    def is_square(k: int) -> bool:
        s = int(math.sqrt(k))
        return s * s == k

    # Reduce the 4^k factor from n
    while (n & 3) == 0:  # n % 4 == 0
        n >>= 2  # n //= 4

    # https://en.wikipedia.org/wiki/Legendre%27s_three-square_theorem
    # https://en.wikipedia.org/wiki/Lagrange%27s_four-square_theorem
    if (n & 7) == 7:  # n % 8 == 7
        return 4

    if is_square(n):
        return 1

    if any(is_square(n - i * i) for i in range(1, int(math.sqrt(n)) + 1)):
        return 2

    return 3

class Solution:
    def numSquares(self, n: int) -> int:
        return num_squares(n)


# RunTime: 52ms
# 思路: 递归+缓存
class Solution:
    def numSquares(self, n: int) -> int:
        def is_divided_by(n, count):

            if count == 1:
                return n in square_nums

            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        square_nums = set([i * i for i in range(1, int(n**0.5)+1)])

        for count in range(1, n+1):
            if is_divided_by(n, count):
                return count


# RunTime: 56ms
# 思路: 栈+缓存
class Solution:
    def numSquares(self, n: int) -> int:
        tot = 0
        def checksq(n):
            nsq = int(round(math.sqrt(n)))
            return nsq * nsq == n
        if checksq(n):
            return 1
        to_check = set([n])
        nxt = set()
        checked = set([n])
        times = 2
        while to_check:
            n = to_check.pop()
            for i in range(1, int(round(math.sqrt(n))) + 1):
                i2 = n - i * i
                if i2 > 0 and not i2 in checked:
                    if checksq(i2):
                        return times
                    checked.add(i2)
                    nxt.add(i2)
            if not to_check:
                times += 1
                to_check = nxt
                nxt = set()
        return -1


# RunTime: 84ms
# 思路: 动态规划, 本质是一样的, 使用空间去换时间, len(dp) = n --> dp[-i*i] = dp[n-i*i]
import math
class Solution:
    _dp=[0]
    def numSquares(self, n: int) -> int:
        dp=self._dp
        while len(dp)<n+1:
            dp.append(1+min(dp[-i*i] for i in range(1,int(len(dp)**0.5)+1)))
        return dp[n]     