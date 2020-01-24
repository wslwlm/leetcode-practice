# 题目地址: https://leetcode.com/problems/min-stack/
# Runtime: 60 ms Memory Usage: 16.1 MB
# pop方法中寻找 min

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float('inf')

    def push(self, x: int) -> None:
        if x < self.min:
            self.min = x
        self.stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min:
            self.min = self.findMin()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

    def findMin(self):
        minValue = float('inf')
        for i in self.stack:
            if i < minValue:
                minValue = i
        return minValue


# RunTime: 40ms
# 维护一个 min 列表
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.sm = []

    def push(self, x: int) -> None:
        self.s.append(x)
        if not self.sm or x < self.sm[-1]:
            self.sm.append(x)
        else:
            self.sm.append(self.sm[-1])

    def pop(self) -> None:
        self.s.pop()
        self.sm.pop()

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.sm[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()