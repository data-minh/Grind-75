"""
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # save = []
        # while len(list1) > 0 and len(list2) > 0:
        #     if list1[0] >= list2[0]:
        #         save.append(list2.pop())
        #     else:
        #         save.append(list1.pop())
        
        # while len(list1) > 0:
        #     save.append(list1.pop())
        
        # while len(list2) > 0:
        #     save.append(list2.pop())

        # return save

        dummy = ListNode()
        current = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1 
                list1 = list1.next  
            else:
                current.next = list2 
                list2 = list2.next  
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next  