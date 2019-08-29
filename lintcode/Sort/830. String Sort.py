"""
Given a string, sort the string with the first keyword which is the most commonly used characters and the second keyword which is the dictionary order.

Example1

Input:  str = "bloomberg"
Output: "bbooeglmr"
Explanation:
'b' and 'o' appear the most frequently, but the dictionary sequence of 'b' is the smaller than 'o', so 'b' is ranked first, followed by 'o', and so on.

Solution:
Custom Sort.
We need to write a compare function according to the requirement.
"""


# Python2 
# > 90%
# Time: O(NlogN), where N is the length of str
# Space: O(N)
class Solution:
    """
    @param str: the string that needs to be sorted
    @return: sorted string
    """
    def stringSort(self, str):
        # Write your code here
        d = dict()
        for c in str:
            d[c] = d.get(c, 0) + 1
        
        def compare(a, b):
            if d[a] == d[b]:
                if a < b:
                    return -1
                elif a > b:
                    return 1
                else:
                    return 0
            else:
                return d[b] - d[a]
        
        l = list(str)
        l.sort(cmp=compare)
        return ''.join(l)
