# 题目地址: https://leetcode.com/problems/add-two-numbers/
# Runtime: 48 ms Memory Usage: 12.6 MB
# 未创建新的ListNode, 所以空间占用较少, 时间以及代码复杂.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MySolution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        headl1 = l1
        headl2 = l2
        
        flag = False
        while l1 and l2:
            jinwei = 1 if flag else 0
            if (l1.val + l2.val+jinwei) > 9:
                flag = True
                l1.val = (l1.val + l2.val + jinwei) % 10
                l2.val = l1.val
            else:
                flag = False
                l1.val = l1.val + l2.val + jinwei
                l2.val = l1.val         
            if not l1.next and not l2.next:
                if flag:
                    node = ListNode(1)
                    l1.next = node
                return headl1
            l1 = l1.next
            l2 = l2.next

        if l1:
            while True:
                jinwei = 1 if flag else 0
                if (l1.val + jinwei) > 9:
                    flag = True
                    l1.val = (l1.val +  jinwei) % 10
                else:
                    flag = False
                    l1.val = (l1.val + jinwei)   
                if not l1.next:
                    if flag:
                        node = ListNode(1)
                        l1.next = node
                        break
                    else:
                        break
                l1 = l1.next
            return headl1
        if l2:
            while True:
                jinwei = 1 if flag else 0
                if (l2.val + jinwei) > 9:
                    flag = True
                    l2.val = (l2.val +  jinwei) % 10
                else:
                    flag = False
                    l2.val = (l2.val + jinwei)   
               
                if not l2.next:
                    if flag:
                        node = ListNode(1)
                        l2.next = node
                        break
                    else:
                        break
                l2 = l2.next
            return headl2

# 创建新的链表, 占用空间大, 运行快
# 用一个carry变量来实现进位的功能，每次相加之后计算carry，并用于下一位的计算
# RunTime: 40ms
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = l3 = ListNode(0)
        carry = 0
        while (l1 or l2 or carry):
            if l1:
                carry += l1.val
                l1 = l1.next                
            if l2:
                carry += l2.val
                l2 = l2.next 
            l3.val = carry % 10
            carry = carry // 10
            if l1 or l2 or carry:
                l3.next = ListNode(0)
                l3 = l3.next
        return head    