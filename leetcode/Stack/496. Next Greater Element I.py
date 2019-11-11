"""
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2. Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.


Solution:
The problem means: for x in nums1, find the same number in nums2 and check if there is any number larger than x (say the number is y>x) on its right side in nums2. Print y if there is such a number or -1 if there is no such number.

Stack + Map
calculate the next greater elements for nums2 first
and then find the index of nums1's element in nums2 and use the calculaed result.
"""


# Stack
# Time: bigger than O(n1 + n2)
# Space: O(n2) at worst case 
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = dict()
        for i, v in enumerate(nums2):
            m[v] = i
        
        stack, res2 = [], []
        
        for i in range(len(nums2)):
            while stack and stack[-1][1] < nums2[i]:
                idx = stack.pop()[0]
                res2[idx] = nums2[i]
            
            stack.append((len(res2), nums2[i]))
            res2.append(-1)     # palceholder
        
        res1 = []
        for n in nums1:
            res1.append(res2[m[n]])
        return res1    
        