# 两两交换链表中的节点
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
#
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
#
#
#
# 示例:
#
# 给定
# 1->2->3->4, 你应该返回
# 2->1->4->3.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 使用递归处理两两交换相邻节点
    def swapPairs(self, head: ListNode) -> ListNode:

        def fun(p):
            if p == None or p.next == None:
                return p
            temp = p.next
            p.next = fun(temp.next)
            temp.next = p
            return temp

        p = head
        return fun(p)

    def swapPairs2(self, head: ListNode) -> ListNode:
        if (head == None or head.next == None):
            return head
        temp = head.next
        head.next = self.swapPairs(temp.next)
        temp.next = head
        return temp

    def swapPairs3(self, head: ListNode) -> ListNode:
        p = head
        while p is not None and p.next is not None:  # 前后都存在
            tmp = p.val  # 前一个值a,给t,
            p.val = p.next.val  # 后一个值b,给a
            p.next.val = tmp  # t再给b,
            p = p.next.next
        return head