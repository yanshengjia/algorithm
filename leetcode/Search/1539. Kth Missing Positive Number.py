"""
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.


Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:
* 1 <= arr.length <= 1000
* 1 <= arr[i] <= 1000
* 1 <= k <= 1000
* arr[i] < arr[j] for 1 <= i < j <= arr.length


Solution:
1. Linear Search  TC: O(N+k)
Traverse elements 1, 2, 3, ... and find missing element with index k

2. Binary Search  TC: O(logN)
Two good indicators for binary search:
* sorted data
* O(logN) TC

Think about a list represents how many missing numbers we have for each index, using arr[i] - i - 1
Convert this question to find the first element greater or equal than k.

Let us look for the following example for more understanding:
[2, 3, 4, 7, 11, 12] and k = 5.

We need to find place, of k-th missing positive number, so, let us create virtual list (virtual, because we will not compute it full, but only elements we need):
B = [2 - 1, 3 - 2, 4 - 3, 7 - 4, 11 - 5, 12 - 6] = [1, 1, 1, 3, 6, 6].
What this list represents is how many missing numbers we have for each inex: for first number we have missing number [1], for next two iterations also, when we add 7, we have 3 missing numbers: [1, 5, 6], when we add 11, we have 6 missing numbers: [1, 5, 6, 8, 9, 10]. How we evalaute values of list B? Very easy, it is just A[i] - i - 1.
What we need to find now in array B: first element, which is greater or equal than k. In our example, we have [1, 1, 1, 3, 6, 6]. We will find it with binary search: this element have index end = 4. Finally, we need to go back to original data, we have

arr = [2, 3, 4, 7, 11, 12]
B = [1, 1, 1, 3, 6, 6]

So, what we now know that our answer is between numbers 7 and 11 and it is equal to arr[end] - (B[end] - k + 1), where the second part is how many steps we need to make backward. Using B[end] = arr[end] - end - 1, we have end + k, we need to return.
"""


# Linear Search
# TC: O(N + k), N = len(arr)
# SC: O(N)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        arr_set = set(arr)
        for i in range(1, k + len(arr) + 1):
            if i not in arr_set:
                k -= 1
            if k == 0:
                return i
        return -1


# Binary Search
# TC: O(logN)
# SC: O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        low, high = 0, len(arr)
        while low < high:
            mid = (low + high) // 2
            if arr[mid] - mid - 1 < k:
                low = mid + 1
            else:
                high = mid
        return high + k  # res = arr[high] - (B[high] - k + 1), where B[high] = arr[high] - high - 1 -> res = high + k
