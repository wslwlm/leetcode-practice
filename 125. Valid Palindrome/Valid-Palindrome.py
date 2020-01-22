# 题目地址: https://leetcode.com/problems/valid-palindrome/
# Runtime: 28 ms, Memory Usage: 14.3 MB
# 去除掉各种标点符号后, 进行大写判断

class MySolution:
    def isPalindrome(self, s: str) -> bool:
        rule = re.compile(r"[^a-zA-Z0-9]")
        s = rule.sub('',s).upper()
        return s== s[::-1]


# 一样的思路
# RunTime: 16ms
class bestSolution:
    def isPalindrome(self, s: str) -> bool:        
        stripped = ''.join(filter(str.isalnum, s)).casefold()
        
        if stripped == stripped[::-1]:
            return True        
        return False