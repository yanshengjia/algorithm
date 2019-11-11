"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.


Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Solution:
Slope
Take care of the condition that the line is parallel to y-axis.                                                 
"""


# Time: O(n)
# Space: O(1)
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # check is x = 0
        if coordinates[1][0] - coordinates[0][0] == 0:
            for i in range(2, len(coordinates)):
                if coordinates[i][0] != coordinates[0][0]:
                    return False
        else:
            k = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])

            for i in range(2, len(coordinates)):
                _k = (coordinates[i][1] - coordinates[0][1]) / (coordinates[i][0] - coordinates[0][0])
                if k != _k:
                    return False
        return True