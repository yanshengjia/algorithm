"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false


Solution:
1.Initialize a stack S.
2.Process each bracket of the expression one at a time.
3.If we encounter an opening bracket, we simply push it onto the stack. This means we will process it later, let us simply move onto the sub-expression ahead.
4.If we encounter a closing bracket, then we check the element on top of the stack. If the element at the top of the stack is an opening bracket of the same type, then we pop it off the stack and continue processing. Else, this implies an invalid expression.
5.In the end, if we are left with a stack still having elements, then this implies an invalid expression.
"""


# time-O(n), where n is the length of s
# space-O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0:
            return True
        else:
            stack = []
            for c in s:
                if len(stack) == 0 and c in [')', '}', ']']:
                    return False
                if c in ['(', '{', '[']:
                    stack.append(c)
                else:
                    if c == ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    elif c == '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
                    else:
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False

            print(stack)
            if len(stack) == 0:
                return True
            else:
                return False
