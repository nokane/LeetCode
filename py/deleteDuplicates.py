""" 
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
"""

class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head
        current = head
        next = head.next
        checkVal = current.val
        while next:
            if current.val == next.val:
                current.next = next.next
                next = current.next
            else:
                current = current.next
                next = next.next
        return head
                
        """
        :type head: ListNode
        :rtype: ListNode
        """
        