"""
Given the head of a singly linked list, return true if it is a 
palindrome or false otherwise.

Input: head = [1,2,2,1]
Output: true

Input: head = [1,2]
Output: false
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Create stack
        stack = []
        cphead = head
        while cphead:
            stack.append(cphead.val)
            cphead = cphead.next
        # Review the linked list and compare
        current = head
        while current:
            if current.val != stack.pop():
                return False
            current = current.next
        return True

