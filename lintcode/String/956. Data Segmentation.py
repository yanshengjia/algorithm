"""
Given a string str, we need to extract the symbols and words of the string in order.

Example 1:

input: str = "(hi (i am)bye)"
outut:["(","hi","(","i","am",")","bye",")"].
Explanation:Separate symbols and words.


Solution:
Go through the str, push the alphabetical into stack and append it to res list if we meet a non-alpha char.
"""


# Time: O(N), where N is the length of the input string
# Space: O(N) in the worst case as the string is full of alphabetical chars.
class Solution:
    """
    @param str: The input string
    @return: The answer
    """
    def dataSegmentation(self, str):
        # Write your code here
        res = []
        if len(str) == 0:
            return res
        tmp = ''
        for i in range(len(str)):
            if str[i].isalpha():
                tmp += str[i]
            else:
                if len(tmp) > 0:
                    res.append(tmp)
                    tmp = ''
                    
                if str[i] != ' ':
                    res.append(str[i])
        if len(tmp) > 0:
            res.append(tmp)
        return res
