"""
Letter Combinations of a Phone Number

Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    if digits == "":
        return []
    keypad = {
      '0': '0',
      '1': '1',
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz'
    }
    results = []
    def recurseDigits(dig, word):
        if len(dig) == 0:
            results.append(word)
            return
        else:
            for c in keypad[dig[0]]:
                word += c
                recurseDigits(dig[1:], word)
                word = word[:-1]
    recurseDigits(digits,'')
    return results