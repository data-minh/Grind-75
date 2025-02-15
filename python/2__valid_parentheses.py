"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """This is one solution"""
        # save = {"a": 0, "b": 0, "c": 0}
        # for element in s:
        #     if element in ["(", ")"]:
        #         if element == "(":
        #             save["a"] += 1
        #         else:
        #             save["a"] -= 1
        #     elif element in ["[", "]"]:
        #         if element == "[":
        #             save["b"] += 1
        #         else:
        #             save["b"] -= 1
        #     elif element in ["{", "}"]:
        #         if element == "{":
        #             save["c"] += 1
        #         else:
        #             save["c"] -= 1
        # check = any(value != 0 for value in save.values())
        # return not check

        """This is two solution"""
        stack = []
        mapping = {")": "(", "]": "[", "}": "{"}

        for element in s:
            if element in mapping:
                element_poped = stack.pop() if stack else '#'
                if mapping[element] != element_poped:
                    return False
            else:
                stack.append(element)

        return not stack