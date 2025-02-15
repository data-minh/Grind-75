"""
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation:
n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation:
n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation:
n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
"""
from typing import List

class Solution:
    """Solution 1"""
    # def missingNumber(self, nums: List[int]) -> int:
    #     mark = 0
    #     total = 1
    #     for element in nums:
    #         if element == 0:
    #             mark = 1
    #         else:
    #             total *= element
    #     if mark == 0:
    #         return 0

    #     n = len(nums)
    #     fac = self.factorial(n) 
    #     quotient = fac//total

    #     if quotient == 1:
    #         return 1
    #     else:
    #         return quotient

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        return n*self.factorial(n-1)
    
    """Solution 2"""
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = ((n+1)*n)//2
        return total - sum(nums)
        