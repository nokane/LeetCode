"""
Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

"((()))", "(()())", "(())()", "()(())", "()()()"
"""

def generateParentheses(n):
    """
    :type n: int
    :rtype: List[str]
    """
    result = []
    depthSearch(n, n, '', result)
    return result

def depthSearch(left, right, val, res):
    if (left > right) or (left < 0) or (right < 0):
        return
    if (left == 0) and (right == 0):
        res.append(val)
        return
    depthSearch(left - 1, right, val + '(', res)
    depthSearch(left, right - 1, val + ')', res)
