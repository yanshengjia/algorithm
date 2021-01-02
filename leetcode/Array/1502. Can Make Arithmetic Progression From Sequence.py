"""
Given an array of numbers arr. A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Return true if the array can be rearranged to form an arithmetic progression, otherwise, return false.


Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.


Solution 1: sort and check
* TC: O(NlogN)
* SC: O(1)

Solution 2: generate arithmetic progression sequence by min and max value in array, put all elements in hashmap, check the elements in generated sequence if in hashmap or not.
* TC: O(N)
* SC: O(N)
"""


# Sort and Check
# TC: O(NlogN)
# SC: O(1)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        
        delta = arr[1] - arr[0]
        
        for i in range(1, len(arr)-1):
            if arr[i+1] - arr[i] != delta:
                return False
        return True


# Generate arithmetic progreesion and compare
# TC: O(N)
# SC: O(N)
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        _min, _max = min(arr), max(arr)
        delta = (_max - _min) / (n - 1)
        
        progression = {}
        
        for i in range(n):
            an = _min + i * delta
            progression[an] = progression.get(an, 0) + 1
        
        for a in arr:
            if a not in progression:
                return False
            else:
                progression[a] -= 1
                if progression[a] < 0:
                    return False
        return True
        