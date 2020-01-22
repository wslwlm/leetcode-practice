# 题目地址: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Runtime: 36 ms Memory Usage: 12.7 MB
# 双指针通过相距n的两个指针slow和fast, slow指示删除元素, fast指示链表尾部

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MySolution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p = q = head
        for _ in range(n):
            p = p.next
        if not p:
            return head.next
        while p.next:
            p = p.next
            q = q.next
            
        q.next = q.next.next
        return head


# 使用字典存储链表中节点的引用, 通过做差求出需要删除的元素
# RunTime: 12ms
class bestSolution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if (not head.next and n == 1) or not head:
            return None
        curr = head
        dictionary = {}
        count = 1
        while curr:
            dictionary[count] = curr
            curr = curr.next
            count += 1
        remove = dictionary[count - n]
        if count - n - 1 == 0:
            return head.next
        prev = dictionary[count - n - 1]
        prev.next = remove.next
        
        return head