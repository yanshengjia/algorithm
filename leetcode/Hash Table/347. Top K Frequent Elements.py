

from typing import List


# Use Hash Table to store count of numbers. Then sort by frequency and get top k.
# Time Complexity: O(NlogN), where N is the number of unique elements in nums. Sorting takes O(NlogN) time.
# Space Complexity: O(N), where N is the number of unique elements in nums. We store the count for each unique element.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        
        sorted_items = sorted(
            counts.items(), 
            key=lambda x: x[1], # x is a (key, value) tuple; x[1] returns the value used for sorting
            reverse=True
        )

        top_k = [num for num, count in sorted_items[:k]]
        return top_k
        