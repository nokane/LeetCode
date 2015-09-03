"""
Merge Two Sorted Lists

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
"""

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if (l1 == None) and (l2 == None):
        return None
    resultsHead = None
    currentNode = None
    l1Node = l1
    l2Node = l2
    if l1Node is not None and l2Node is not None:
        if l1Node.val <= l2Node.val:
            currentNode = ListNode(l1Node.val)
            l1Node = l1Node.next
        else: 
            currentNode = ListNode(l2Node.val)
            l2Node = l2Node.next
    elif l1Node is None:
            currentNode = ListNode(l2Node.val)
            l2Node = l2Node.next
    elif l2Node is None:
            currentNode = ListNode(l1Node.val)
            l1Node = l1Node.next
    resultsHead = currentNode
    
    while l1Node and l2Node:
        if l1Node.val <= l2Node.val:
            newNode = ListNode(l1Node.val)
            currentNode.next = newNode
            currentNode = newNode
            l1Node = l1Node.next
        else: 
            newNode = ListNode(l2Node.val)
            currentNode.next = newNode
            currentNode = newNode
            l2Node = l2Node.next

    while l1Node:
        newNode = ListNode(l1Node.val)
        currentNode.next = newNode
        currentNode = newNode
        l1Node = l1Node.next

    while l2Node:
        newNode = ListNode(l2Node.val)
        currentNode.next = newNode
        currentNode = newNode
        l2Node = l2Node.next

    return resultsHead