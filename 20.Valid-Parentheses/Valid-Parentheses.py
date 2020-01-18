# Python
# 题目地址: https://leetcode.com/problems/valid-parentheses/
# 使用栈去做, 当括号匹配时将栈顶元素弹出, 括号不匹配时压栈, 最后栈为空则True, 否则为False
# Runtime: 28 ms Memory Usage: 12.8 MB
class MySolution:
    def isValid(self, s: str) -> bool:
        dictS = {
            '{': '}',
            '(': ')',
            '[': ']'
        }
        signList = []
        for s1 in s:
            if signList and signList[-1] in dictS and dictS[signList[-1]] == s1:
                signList.pop()
            else:
                signList.append(s1)
        if not signList:
            return True
        else:
            return False

# Runtime: 8 ms
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {'(':')', '{':'}', '[':']'}
        for i in s:
            if i in dic:
                stack.append(i)
            else:
                if not len(stack):
                    return False 
                
                if dic[stack[-1]] == i:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True