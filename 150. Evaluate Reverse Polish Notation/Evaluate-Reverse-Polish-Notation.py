# 题目地址: https://leetcode.com/problems/evaluate-reverse-polish-notation/
# Runtime: 64 ms Memory Usage: 13 MB
# 思路: 一个数字栈, 当遇到符号时, 数字栈出栈, 并将计算结果入栈.

class Solution:
    def evalRPN(self, tokens) -> int:
        signList = ["+", "-", "*", "/"]
        s = []
        n = len(tokens)
        res = int(tokens[0])

        for i in tokens:
            if i not in signList:
                s.append(int(i))
            else:
                res = 0
                a = s.pop()
                b = s.pop()

                if i == '+':
                    res = a + b
                elif i == '-':
                    res = b - a
                elif i == '*':
                    res = a * b
                else:
                    res = abs(b) // abs(a)
                    res = res if ((a>0) is (b>0)) else -res

                s.append(res)

        return res


# RunTime:
# 思路: 一样
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda x, y: y + x,
            '-': lambda x, y: y - x,
            '/': lambda x, y: int(y / x),
            '*': lambda x, y: y * x
        }
        
        operands = []
        
        for token in tokens:
            if token in operators:
                result = operators[token](operands.pop(), operands.pop())
                operands.append(result)
            else:
                operands.append(int(token))
        return operands[-1]