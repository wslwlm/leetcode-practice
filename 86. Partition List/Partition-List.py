# 题目地址: https://leetcode.com/problems/partition-list/
# Runtime: 20 ms Memory Usage: 12.6 MB
# 遍历两遍, 第一遍两个数组储存, 然后第二遍对链表节点赋值, 有点赖皮的做法

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class MySolution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        tmp = head
        low = []
        high = []
        while tmp:
            if tmp.val < x:
                low.append(tmp.val)
            else:
                high.append(tmp.val)
            tmp = tmp.next
        
        tmp = head
        l = len(low)
        h = len(high)
        for i in range(l+h):
            if i < l:
                tmp.val = low[i]
            else:
                tmp.val = high[i-l]
            tmp = tmp.next
            
        return head


# RunTime: 16ms
# 思路: 将值大于x的接在small链表上, 将值大于x接在big链表上, 最后将两个链表合并
class bestSolution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small_dummy = ListNode(0)
        big_dummy = ListNode(0)
        small = small_dummy
        big = big_dummy

        cur = head
        while cur:
            if cur.val < x: # add to small
                small.next = cur
                small = small.next
            else:
                big.next = cur
                big = big.next
            cur = cur.next
        big.next = None # break the cycle
        if small != small_dummy:
            small.next = big_dummy.next
            return small_dummy.next
        return head


# RunTime: 8ms
# 思路: 不建立新链表, 确定四个指针, 然后用类似建立两个新链表的方法做
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None:
            return None
        walk = head
        startLeft = None
        currLeft = None
        startRight = None
        currRight = None
        while walk and (startLeft is None or startRight is None):
            if walk.val < x:
                if startLeft is None:
                    startLeft = walk
                currLeft = walk
            else:
                if startRight is None:
                    startRight = walk
                currRight = walk
            walk = walk.next
        if startRight is None or startLeft is None:     # 值全为大于或小于x
            return head
        while walk:
            if walk.val < x:
                currLeft.next = walk
                currLeft = walk
            else:
                currRight.next = walk
                currRight = walk
            walk = walk.next
        currLeft.next = startRight
        currRight.next = None
        return startLeft


# 思路: 不产生新的链表, 在原链表基础上建立三个指针
# 更新的时候, 当出现小于x的值的node时, 将其断开并接在sep的后面, 接着更新sep, pre, cur指针
class githubSolution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """在原链表操作，思路基本一致，只是通过指针进行区分而已"""
        # 在链表最前面设定一个初始node作为锚点，方便返回最后的结果
        first_node = ListNode(0)
        first_node.next = head
        # 设计三个指针，一个指向小于x的最后一个节点，即前后分离点
        # 一个指向当前遍历节点的前一个节点
        # 一个指向当前遍历的节点
        sep_node = first_node
        pre_node = first_node
        current_node = head
        
        while current_node is not None:
            if current_node.val < x:
                # 注意有可能出现前一个节点就是分离节点的情况
                if pre_node is sep_node:
                    pre_node = current_node
                    sep_node = current_node
                    current_node = current_node.next
                else:
                    # 这段次序比较烧脑
                    pre_node.next = current_node.next
                    current_node.next = sep_node.next
                    sep_node.next = current_node
                    sep_node = current_node
                    current_node = pre_node.next
            else:
                pre_node = current_node
                current_node = pre_node.next
        
        return first_node.next