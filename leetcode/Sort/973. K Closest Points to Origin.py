"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)


Example 1:

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].
Example 2:

Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)


Solution:
1. Sort.
Calculate the distance bewteen each point and the origin point, then sort. Return the first k points.

2. Divide and Conquer
Partition

3. Minheap
"""


# Sort
# Time: O(NlogN), where N is the number of points, cuz fast sorting takes O(NlogN)
# Space: O(N)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        d = dict()
        count = 0
        for point in points:
            distance = self.cal_distance(point[0], point[1])
            d[count] = distance
            count += 1
        
        sorted_d = sorted(d.items(), key=lambda kv: kv[1])
        res = []
        i = 0
        while i < len(sorted_d):
            if i < K:
                res.append(points[sorted_d[i][0]])
                i += 1
            else:
                if sorted_d[i][1] == sorted_d[i-1][1]:
                    res.append(points[sorted_d[i][0]])
                    i += 1
                else:
                    break
        return res
    
    def cal_distance(self, x1, y1):
        return x1**2 + y1**2


# Sort by a custom key function
class Solution(object):
    def kClosest(self, points, K):
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:K]