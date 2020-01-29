# 题目地址: https://leetcode.com/problems/remove-linked-list-elements/
# Runtime: 64 ms Memory Usage: 15.5 MB
# 考虑到val连续, val在数组头尾情况即可

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MySolution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return head
        p = head
        
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
        if head.val == val:
            return head.next
        return head


# 思路类似
# RunTime: 44ms
class bestSolution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        node = head
        while node:
            if node.val == val:
                if node == head:
                    head = head.next
                    node = head
                else:
                    temp = node.next
                    pre.next = node.next
                    node = temp
            else:
                pre = node
                node = node.next
        return head


# 插入一个虚拟头部, 处理头部删除
class githubSolution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = ListNode(0)
        prev.next = head
        cur = prev
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return prev.next