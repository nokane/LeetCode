"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

def isBalanced(root):
    """
    :type root: TreeNode
    :rtype: bool
    """
    if root is None:
        return True
    if checkHeight(root) == -1:
        return False
    else:
        return True

def checkHeight(node):
    if node is None:
        return 0
    leftHeight = checkHeight(node.left)
    if leftHeight == -1:
        return -1
    rightHeight = checkHeight(node.right)
    if rightHead == -1:
        return -1
    if abs(leftHeight - rightHeight) > 1:
        return -1
    return max(leftHeight, rightHeight) + 1
