"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    """Solution 1"""
    # def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    #     def getElement(root: Optional[TreeNode]):
    #         if root:
    #             arr = []
    #             arr.append(root.val)
    #             return arr + getElement(root.left) + getElement(root.right)
            
    #         return ['.']

    #     def invertTree(root: Optional[TreeNode]):
    #         if root is None:
    #             return None
    #         root.left, root.right = root.right, root.left
    #         invertTree(root.left)
    #         invertTree(root.right)

    #         return root

    #     if root:
    #         left = getElement(invertTree(root.left))
    #         right = getElement(root.right)
            
    #         return left == right
        
    """Solution 2"""
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.compareTree(root.left, root.right)

    def compareTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        
        return (root1.val == root2.val and 
            self.compareTree(root1.left, root2.right) and
            self.compareTree(root1.right, root2.left))