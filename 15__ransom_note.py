"""
Given two strings ransomNote and magazine, return true 
if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        # Solution 1
        # def count_element_number(s: str) -> dict:
        #     char_count = {}
        #     for e in s:
        #         char_count[e] = char_count.get(e, 0) + 1
        #     return char_count
        
        # ransomNote_counts = count_element_number(ransomNote)
        # magazine_counts = count_element_number(magazine)

        # for k, v in ransomNote_counts.items():
        #     mark = magazine_counts.get(k, 0)
        #     if mark == 0 or mark < v:
        #         return False
        # return True

        # Solution 2
        for i in set(ransomNote):
            if ransomNote.count(i) > magazine.count(i):
                return False
        return True
