"""
Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and ending at [r-1, c-1]. The score of a path is the minimum value in that path. For example, the score of the path 8 → 4 → 5 → 9 is 4.

Don't include the first or final entry. You can only move either down or right at any point in time.

Example 1:

Input:
[[5, 1],
 [4, 5]]

Output: 4
Explanation:
Possible paths:
5 → 1 → 5 => min value is 1
5 → 4 → 5 => min value is 4
Return the max value among minimum values => max(4, 1) = 4.
Example 2:

Input:
[[1, 2, 3]
 [4, 5, 1]]

Output: 4
Explanation:
Possible paths:
1-> 2 -> 3 -> 1
1-> 2 -> 5 -> 1
1-> 4 -> 5 -> 1
So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
"""

def max_min_path(matrix: list) -> int:
    if not matrix or not matrix[0]:
        return 0

    n, m = len(matrix), len(matrix[0])

    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif (i == 1 and j == 0) or (i == 0 and j == 1):
                # don't include the first and final entry.
                continue
            elif i == 0:
                matrix[i][j] = min(matrix[i][j], matrix[i][j-1])
            elif j == 0:
                matrix[i][j] = min(matrix[i][j], matrix[i-1][j])
            else:
                matrix[i][j] = min(matrix[i][j], max(matrix[i-1][j], matrix[i][j-1]))
    

    if n == 1:
        return matrix[0][-2]
    elif m == 1:
        return matrix[-2][0]
    else:
        return max(matrix[-2][-1], matrix[-1][-2])


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 1]]
    print(max_min_path(matrix))


