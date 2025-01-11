"""
Given a string s which consists of lowercase or uppercase letters, return the length of the longest 
palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

class Solution:
    def longestPalindrome(self, s: str) -> int:
        longest_lenght = 0
        mark = 0
        for element in set(s):
            count = s.count(element)
            if count == len(s):
                return count
            if count % 2 == 0:
                longest_lenght += count
            if count % 2 == 1:
                if mark == 0:
                    longest_lenght += count
                else:
                    longest_lenght += count - 1
                mark = 1

        return longest_lenght
        