"""
Given a binary tree, determine if it is height-balanced.
Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        left_high = self.HighTree(root.left)
        right_high = self.HighTree(root.right)
        print(left_high, right_high)
        if abs(left_high-right_high) > 1:
            return False
        else:
            return True
        
    def HighTree(self, root:Optional[TreeNode]):
        if root is None:
            return -1
        left_tree = self.HighTree(root.left)
        right_tree = self.HighTree(root.right)

        return 1 + max(left_tree, right_tree)