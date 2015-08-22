"""
Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = ""
        current = ""
        chars = dict()
        startIndex = 0
        for index,c in enumerate(s):
            if c in chars:
                if chars[c] >= startIndex: 
                    if len(current) > len(longest):
                        longest = current
                    startIndex = chars[c] + 1
                    current = s[startIndex:index]
            current += c
            chars[c] = index
        if len(current) > len(longest):
            longest = current
        return len(longest)