"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2s
"""
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        max, element = 0, None
        for i in set(nums):
            count = nums.count(i)
            if count > n and count > max:
                max = count
                element = i
        return element