# 题目地址: https://leetcode.com/problems/reverse-linked-list/
# 三指针翻转, 1   ->   2    ->   3 ==> 1<-2<-3
#            ^        ^         ^
#            prev     cur      after
# 可递归实现, 由于单链表是线性的，使用递归方式将导致栈的使用也是线性。
# 当链表长度达到一定程度时，递归会导致爆栈，因此，现实中并不推荐使用递归方式来操作链表。

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = head
        if not prev:
            return head
        cur = prev.next
        if not cur:
            return head
        after = cur.next
        
        prev.next = None
        
        while cur:
            cur.next = prev
            prev = cur
            cur = after
            if after:
                after = after.next
        return prev


# 三指针的初始化比较好, 简化后面逻辑
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, cur, nex = None, head, None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        return prev