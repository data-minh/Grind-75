/*
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
*/
import java.util.Map;
import java.util.Stack;
import java.util.HashMap;


public class ValidParentheses {
    public boolean isValid(String s) {
        Map<Character, Character> map = new HashMap<>();
        map.put(']', '[');
        map.put(')', '(');
        map.put('}', '{');

        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++){

            Character element = s.charAt(i);

            if(map.containsKey(element)){
                if(stack.empty() || stack.pop() != map.get(element)){
                    return false;
                }
            }
            else{
                stack.push(element);
            }
        }
        return stack.isEmpty();
    } 

    public static void main(String[] args) {
        ValidParentheses vp = new ValidParentheses();
        System.out.println(vp.isValid("()[]{}")); // true
        System.out.println(vp.isValid("(]"));     // false
        System.out.println(vp.isValid("({[]})")); // true
    }
}
