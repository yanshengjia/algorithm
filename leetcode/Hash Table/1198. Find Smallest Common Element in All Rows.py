"""
Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.

If there is no common element, return -1.

 

Example 1:

Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5
 

Constraints:

1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in increasing order.


Solution:
1. Count
2. Binary Search
3. Hashtable {num: [row_idx]}
when len(row_indexes) == row_number, return num
"""


# Hashtable
# Time: O(mn)
# Space: O(mn)
import collections
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        row, col = len(mat), len(mat[0])
        d = collections.defaultdict(list)
        
        for i in range(row):
            for j in range(col):
                n = mat[i][j]
                d[n].append(row)
                if len(d[n]) == row:
                    return n
        return -1
