"""
Given a list of scores of different students, return the average score of each student's top five scores in the order of each student's id.

Each entry items[i] has items[i][0] the student's id, and items[i][1] the student's score.  The average score is calculated using integer division.


Example 1:

Input: [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The average of the student with id = 1 is 87.
The average of the student with id = 2 is 88.6. But with integer division their average converts to 88.


Solution:
1. Sort
2. Priority Queue (Min Heap)
Maintain a min heap which size is 5 for each student's id.
"""


# Time: O(Nlog5), where N is the length of items
# Space: O(M), where M is the number of unique student id
import heapq
class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """
        d = dict()
        for item in items:
            id = item[0]
            score = item[1]
            if id not in d:
                l = [score]
                heapq.heapify(l)
                d[id] = l
            else:
                heapq.heappush(d[id], score)
                if len(d[id]) > 5:
                    heapq.heappop(d[id])
        
        res = []
        sorted_items = sorted(d.items())
        for i in sorted_items:
            id = i[0]
            heap = i[1]
            print(heap)
            avg = sum(heapq.nlargest(5, heap)) / 5
            res.append([id, avg])
        return res


# Min Heap
# > 60%
import heapq
import collections
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)   # {idx: min heap}
        
        for idx, val in items:
            heapq.heappush(d[idx], val)
            
            if len(d[idx]) > 5:
                heapq.heappop(d[idx])
        
        res = [[i, sum(d[i]) // len(d[i])] for i in sorted(d)]
        
        return res



# sort
# Time: O(NlogN + N), where N is the length of items
# Space: O(M), where M is the number of unique student id
class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        items.sort(reverse=True)    # sort first
        
        res = []
        curr = []
        idx = items[0][0]
        
        for i, val in items:
            if i == idx:
                if len(curr) < 5:
                    curr.append(val)
            else:
                res.append([idx, sum(curr) // len(curr)])
                curr = [val]
                idx = i
        
        res.append([idx, sum(curr) // len(curr)])
        
        res = res[::-1]
        
        return res