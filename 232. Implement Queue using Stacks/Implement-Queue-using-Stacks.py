# 题目地址: https://leetcode.com/problems/implement-queue-using-stacks/
# Runtime: 20 ms Memory Usage: 12.9 MB
# 双栈实现队列, 一个栈导到另一个栈

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inbox = []
        self.outbox = list()

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inbox.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.empty():
            return None
        if not self.outbox:
            while self.inbox:
                value = self.inbox.pop()
                self.outbox.append(value)
        return self.outbox.pop()
            
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.empty():
            return None
        
        if not self.outbox:
            while self.inbox:
                value = self.inbox.pop()
                self.outbox.append(value)

        return self.outbox[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.inbox and not self.outbox