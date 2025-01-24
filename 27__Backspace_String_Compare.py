"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
Note that after backspacing an empty text, the text will continue empty.

Example 1:
Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".

Example 2:
Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".

Example 3:
Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
"""

class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        char = '#'
        index_s = s.find(char)
        index_t = t.find(char)
        # Case s
        while index_s != -1:
            if index_s == 0:
                s = s[:index_s] + s[index_s+1:]
            else:
                s = s[:index_s-1] + s[index_s+1:]
            index_s = s.find(char)

        # Case t
        while index_t != -1:
            if index_t == 0:
                t = t[:index_t] + t[index_t+1:]
            else:
                t = t[:index_t-1] + t[index_t+1:]
            index_t = t.find(char)  

        return s == t