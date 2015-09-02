"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

"""
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    MAX = 2147483647
    MIN = -2147483648
    negative = False
    newNum = 0
    currNum = x
    if x < 0:
        negative = True
        currNum *= -1
    while currNum > 0:
        newNum = (newNum * 10) + (currNum % 10)
        currNum = int(currNum / 10)
    if negative:
        newNum *= -1
    if (newNum > MAX) or (newNum < MIN - 1):
        return 0
    return newNum
