"""
Given two strings s and t, return true if they are equal when both are typed into empty text editors. 
'#' means a backspace character.
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

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        copy_s = ''
        copy_t = ''
        Max = max(len(s), len(t))
        for i in range(Max):
            try:
                if s[i] == '#':
                    copy_s = copy_s[:len(copy_s)-1]
                else:
                    copy_s += s[i]
            except:
                pass

            try:
                if t[i] == '#':
                    copy_t = copy_t[:len(copy_t)-1]
                else:
                    copy_t += t[i]
            except:
                pass
        return copy_s == copy_t
        