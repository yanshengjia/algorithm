"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.


Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.


Solution:
1. Two pass.
2. Read / Write Heads
For each even i, let's make A[i] even. To do it, we will draft an element from the odd slice. We pass j through the odd slice until we find an even element, then swap. Our invariant is maintained, so the algorithm is correct.
"""


# Two pass
# Read all the even integers and put them into places ans[0], ans[2], ans[4], and so on.
# Then, read all the odd integers and put them into places ans[1], ans[3], ans[5], etc.
# Time: O(N), where N is the length of A
# Space: O(N)
class Solution(object):
    def sortArrayByParityII(self, A):
        N = len(A)
        ans = [None] * N

        t = 0
        for i, x in enumerate(A):
            if x % 2 == 0:
                ans[t] = x
                t += 2

        t = 1
        for i, x in enumerate(A):
            if x % 2 == 1:
                ans[t] = x
                t += 2

        # We could have also used slice assignment:
        # ans[::2] = (x for x in A if x % 2 == 0)
        # ans[1::2] = (x for x in A if x % 2 == 1)

        return ans


# Two Pass
# Divide the array to 2 list, one for even, oven for odd
# Assign even numbers to even indexes and odd numbers to odd indexes.
# Time: O(N), where N is the length of A
# Space: O(N)
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd, even = [], []
        for a in A:
            if a % 2 == 0:
                even.append(a)
            else:
                odd.append(a)
        
        for i in range(len(A)):
            if i % 2 == 0:
                A[i] = even.pop()
            else:
                A[i] = odd.pop()
        return A


# Read / Write Heads
# Time: O(N), where N is the length of A
# Space: O(1)
class Solution(object):
    def sortArrayByParityII(self, A):
        j = 1
        for i in xrange(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A