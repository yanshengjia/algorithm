"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.


Example:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 

Note:
1.The number of tasks is in the range [1, 10000].
2.The integer n is in the range [0, 100].


Solution:
1. Sorting
2. Max-Heap
Execute tasks based on their descending frequency.
The name of the task doesn't matter.
Cooling interval is n, execution duration is n+1.
For the last duration, we don't have to iterate n+1 times if there is no task left.
Modify freq of tasks after heappoping them.
"""


# Time: O(N), N is the result time. Number of iterations will be equal to resultant time timetime.
# Space: O(1), the size of list, heap and temp list will not exceed O(26)
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count the frequency of tasks
        freq = [0 for _ in range(26)]
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
        
        # exclude tasks which freq is 0
        f = []
        for i in freq:
            if i > 0:
                f.append(-i)
        
        # build a max_heap
        heapq.heapify(f)
        
        # execute tasks based on descending frequency
        res = 0
        while f:
            i = 0
            t = []  # temp list to store executed tasks, for next duration
            while i <= n:   # cooling interval n, duration is n+1
                if f:
                    task = heapq.heappop(f)
                    task += 1
                    if task < 0:
                        t.append(task)
                res += 1    # excute tasks or pad idle
                if len(f) == 0 and len(t) == 0:
                    # last duration
                    break
                
                i += 1
            
            for task in t:
                # for next duration
                # we only push tasks which freq > 0 back to heap
                heapq.heappush(f, task)
        return res
