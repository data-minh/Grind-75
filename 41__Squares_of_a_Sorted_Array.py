"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # result = [0]*n
        # l, r, mark = 0, n - 1, n - 1
        
        # while r >= l:
        #     left, right = nums[l]**2, nums[r]**2
        #     if left > right:
        #         result[mark] = left
        #         l += 1
        #     else:
        #         result[mark] = right
        #         r -= 1
        #     mark -= 1
        # return result
        return sorted(element**2 for element in nums)