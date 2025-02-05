"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(start: int, end: int) -> int:
            if start > end:
                return -1
            mid = (start+end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(start, mid - 1)
            else:
                return binary_search(mid + 1, end)

        return binary_search(0, len(nums) - 1)