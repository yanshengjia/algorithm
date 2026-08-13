from typing import List

# Sort intervals by their start number, then merge overlapping intervals
# Time Complexity: O(NlogN), where N is the number of intervals. Sorting takes O(NlogN) time.
# Space Complexity: O(1), not counting the space used by the output list.
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x: x[0]) # list.sort() returns None, sorting in place

        res = []

        for interval in intervals:
            # res is empty or last interval in res is NOT overlapping with current interval
            # append interval into res
            if len(res) == 0 or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # last interval in res is overlapping with current internval
                # merge them
                res[-1][1] = max(res[-1][1], interval[1])
        return res