"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

Solution:
Stack
one stack or two stacks both will do, the key is we should store the cur_number and cur_str simultaneously.
"""


# Time: O(n), n is the length of s
# Space: O(n), at worst case
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_number = 0
        cur_str = ""
        
        for c in s:
            if c.isdigit():
                cur_number = cur_number * 10 + int(c)
            elif c == '[':  # push
                stack.append(cur_number)
                stack.append(cur_str)
                cur_number = 0
                cur_str = ""
            elif c == ']':  # pop
                pre_str = stack.pop()
                num = stack.pop()
                cur_str = pre_str + num * cur_str
            else:
                cur_str += c
        return cur_str