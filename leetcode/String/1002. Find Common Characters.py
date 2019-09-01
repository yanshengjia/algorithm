"""
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.


Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]


Solution:
Update the res list every time we meet a new word.
"""


# Time: O(N), where N is the length of A
# Space: O(1)
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        res = list(A[0])
        for word in A:
            new_res = []
            for c in word:
                if c in res:
                    new_res.append(c)
                    res.remove(c)
            res = new_res
        return res
        