"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    curr = None
    brackets = []
    def newCurr():
        if len(brackets) > 0:
            return brackets.pop(len(brackets)-1)
        else:
            return None
    for x in s:
        if (x == '(') or (x == '{') or (x == '['):
            if curr != None:
                brackets.append(curr)
            curr = x
        elif (x == ')') or (x == '}') or (x == ']'):
            if x == ')':
                if curr != '(':
                    return False
            elif x == '}':
                if curr != '{':
                    return False
            elif x == ']':
                if curr != '[':
                    return False
            curr = newCurr()
    if (len(brackets) > 0) or (curr != None):
        return False
    else:
        return True

