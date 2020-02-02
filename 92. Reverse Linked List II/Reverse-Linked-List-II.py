# 题目地址: https://leetcode.com/problems/reverse-linked-list-ii/
# Runtime: 36 ms Memory Usage: 12.8 MB
# 又是取巧, 先取出来, reverse再放进去..

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MySolution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return head
        diff = n - m
        if diff == 0:
            return head
        slow = fast = head
        s = []
        for i in range(n):
            if i >= m-1:
                s.append(fast.val)
            if i > diff:
                slow = slow.next
            fast = fast.next
        
        s.reverse()
        
        
        for i in range(diff+1):
            slow.val = s[i]
            slow = slow.next
            
        return head


# RunTime: 12ms
# 思路: 在(m, n)区间内节点翻转, 然后再接起来.
class bestSolution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # 加入一个虚拟节点, 在操作时方便
        dummy = ListNode(0)
        dummy.next = head
        pm, pn = dummy, dummy
        
        for _ in range(m-1):
            pm, pn = pm.next, pn.next
        for _ in range(n-m+2):
            pn = pn.next
            
        tail = pm.next
        pre, cur = pm, pm.next
        while cur is not pn:
            tem = cur.next
            cur.next = pre
            pre = cur
            cur = tem
            
        tail.next = pn
        pm.next = pre
        
        return dummy.next