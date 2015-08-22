"""
You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    class ListNode(object):
        def __init__(self, x):
            self.val = x
            self.next = None
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def findTotal(li):
            if l1 is not None:
                node = li
                sum = 0
                multiplier = 1
                while node:
                    sum += (node.val * multiplier)
                    multiplier *= 10
                    node = node.next
                return sum
            else:
                return 0
        def numberToList(num):
            stringifyNum = str(num)
            firstNode = True
            headNode = None
            currNode = None
            prevNode = None
            for c in reversed(stringifyNum):
                if firstNode:
                    headNode = ListNode(int(c))
                    prevNode = headNode
                    firstNode = False
                else:  
                    currNode = ListNode(int(c))
                    prevNode.next = currNode
                    prevNode = currNode
            return headNode
        totalSum = findTotal(l1) + findTotal(l2)
        return numberToList(totalSum)