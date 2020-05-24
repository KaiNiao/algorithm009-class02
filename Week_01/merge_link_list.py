# coding: utf-8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """合并两个有序链表"""
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """循环"""
        head = ListNode(-1)  # 新的头结点，哑结点
        prev = head  # 拷贝

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        
        # if l1 is not None:
        #     prev.next = l1
        # else:
        #     prev.next = l2
        prev.next = l1 or l2
        
        return head.next
    
    def merge_two_lists_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """递归"""
        if l1 is None:  # 边界条件
            return l2
        elif l2 is None:  # 边界条件
            return l1
        elif l1.val < l2.val:
            l1.next = self.merge_two_lists_1(l1.next, l2)
            return l1  # 返回值较小的结点
        else:
            l2.next = self.merge_two_lists_1(l2.next, l1)
            return l2
