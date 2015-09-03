"""
ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:



string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows == 1:
        return s
    resultString = ""
    delt = numRows * 2 - 2
    for i in xrange(numRows):
        for position in range(i,len(s), delt):
            resultString += s[position]
            if (i != 0) and (i != numRows - 1):
                if (position + delt - 2 * i) < len(s):
                    resultString += s[position + delt - 2 * i]
    return resultString