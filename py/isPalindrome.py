"""
Determine whether an integer is a palindrome. Do this without extra space.
"""

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if (x == 0):
        return True
    elif (x < 0) or (x % 10 == 0):
        return False    
    y = 0
    while (x > y):
        y = (y * 10) + (x % 10)
        if (x == y):
            return True
        x = int(x / 10)
    return x == y
