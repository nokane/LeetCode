"""
Remove Nth Node From End of List
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""

def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    storage = []
    currentNode = head
    while currentNode:
        storage.append(currentNode)
        currentNode = currentNode.next
    if (len(storage) == 1) and (n == 1):
        return None
    elif n == 1:
        storage[len(storage)-2].next = None
    elif len(storage) == n:
        head = head.next
    else:
        storage[len(storage)-(n + 1)].next = storage[len(storage)- (n - 1)]
    return head


