"""
Given two lists Aand B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.
We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.
These lists A and B may contain duplicates. If there are multiple answers, output any of them.

For example, given
A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
We should return
[1, 4, 3, 2, 0]


Solution:
Create a hasb table based on B, {value_in_b, index}
"""


# time-O(n) n is the length of list A
# space-O(n)
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        d = dict()
        for i in range(len(B)):
            d[B[i]] = i
        return [d[A[i]] for i in range(len(A))]
        