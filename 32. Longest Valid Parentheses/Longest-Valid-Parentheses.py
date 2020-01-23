# 题目地址: https://leetcode.com/problems/longest-valid-parentheses/
# Runtime: 44 ms, Memory Usage: 13.6 MB
# 通过栈来进行括号匹配, 然后对留存符号对应数字进行考察, 算相邻之间差最大

class MySolution:
    def longestValidParentheses(self, s: str) -> int:
        chardict = {
            '(': ')',
            ')':''
        }
        maxLen = 0
        stack = []
        order = []
        lenList = len(s)
        for i in range(lenList):
            if stack and chardict[stack[-1]] == s[i]:
                stack.pop()
                order.pop()
            else:
                stack.append(s[i])
                order.append(i)
        order = [-1] + order + [lenList]
        for i in range(len(order)-1):
            tmpLen = order[i+1] - order[i] - 1
            if tmpLen > maxLen:
                maxLen = tmpLen
        return maxLen


# RunTime: 20ms
# 类似的思路, 简化的地方是省略了字符栈, 只用数字栈, 
class bestSolution:
    def longestValidParentheses(self, s: str) -> int:
        stack=[-1]
        ml=0
        for i in range(len(s)):
            if s[i]=='(':               # 左括号压栈
                stack.append(i)
            else:                       # 右括号弹出
                stack.pop()
                if len(stack)==0:
                    stack.append(i)
                else:
                    ml=max(ml,i-stack[-1])
        
        return ml