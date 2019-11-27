"""
Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n numbers as input and checks whether there is a 132 pattern in the list.

Note: n will be less than 15,000.

Example 1:
Input: [1, 2, 3, 4]

Output: False

Explanation: There is no 132 pattern in the sequence.
Example 2:
Input: [3, 1, 4, 2]

Output: True

Explanation: There is a 132 pattern in the sequence: [1, 4, 2].
Example 3:
Input: [-1, 3, 2, 0]

Output: True

Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].


Solution:
1. Brute Force O(n^3)
2. Better Brute Force O(n^2)
3. Monotonous Stack 站内元素都是单调递增或者单调递减 
https://www.cnblogs.com/grandyang/p/8887985.html
维护一个单调栈和一个变量 third (第三个数字，中间值)，栈中存放所有大于 third 的数字，也就是 second (第二个数字，最大值)
从后往前遍历，如果当前元素大于栈顶元素，说明栈顶元素非最大，将其退栈，赋给 third. 栈里存放的都是可以维持 second > third 的 second 值.
如果当前元素小于 third，并且栈非空，那么说明找到了 132 pattern.
"""


# Brute Force
# Time: O(n^3)
# Space: O(1)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        l = len(nums)
        for i in range(l-2):
            for j in range(i+1, l-1):
                for k in range(j+1, l):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False


# Better Brute Force
# Fix a number 'ai', two for loops
# Time: O(n^2)
# Space: O(1)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        l = len(nums)
        mn = float('inf')
        for j in range(l-1):
            mn = min(mn, nums[j])   # mn, the smallest one, 'ai'
            if mn == nums[j]:
                continue
            for k in range(j+1, l):
                if mn < nums[k] < nums[j]:
                    return True
        return False


# Monotonous Stack
# Time: O(N)
# Space: O(N) at worst case
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 1 3 2
        # i j k
        # ai < ak < aj
        l = len(nums)
        third = float('-inf')   # aj
        stack = []
        for i in range(l-1, -1, -1):    # ai
            # why scan backwords? make sure third (aj) come from elements after ai
            if nums[i] < third:
                # third was updated, it means there is a number bigger than top of the stack, and the index of that number is prior to top of the stack (third)
                # we found ai < ak < aj
                return True
            while stack and nums[i] > stack[-1]:
                third = stack[-1]
                stack.pop()
            stack.append(nums[i])
        return False
