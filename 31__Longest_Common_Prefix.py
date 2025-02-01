"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for i in range(len(strs[0])):
            character = strs[0][i]
            mark = 0
            for s in strs[1:]:
                try:
                    if s[i] != character:
                        mark = 1
                        break
                except:
                    mark = 1
                    break
            if mark == 1:
                break
            prefix += character
        return prefix
