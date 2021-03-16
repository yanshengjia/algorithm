"""
Design a hit counter which counts the number of hits received in the past 5 minutes.

Each function accepts a timestamp parameter (in seconds granularity) and you may assume that calls are being made to the system in chronological order (ie, the timestamp is monotonically increasing). You may assume that the earliest timestamp starts at 1.

It is possible that several hits arrive roughly at the same time.

Example:

HitCounter counter = new HitCounter();

// hit at timestamp 1.
counter.hit(1);

// hit at timestamp 2.
counter.hit(2);

// hit at timestamp 3.
counter.hit(3);

// get hits at timestamp 4, should return 3.
counter.getHits(4);

// hit at timestamp 300.
counter.hit(300);

// get hits at timestamp 300, should return 4.
counter.getHits(300);

// get hits at timestamp 301, should return 3.
counter.getHits(301); 

Follow up:
What if the number of hits per second could be very large? Does your design scale? Use hashmap (timestamp, count of timestamp)


Solution:
Use hashmap to keep the timestamps as well as the count of timestamps.
(timestamp, count)
Keep the size of `hits` map as 300 since the hit counter only counts hits in the past 5 minutes.
Use deque to pop item from sorted_hits using O(1) time.
"""


from collections import deque

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = {}                  # max size is 300
        self.sorted_hits = deque([])    # max size is 300
        
    # TC: O(1)
    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if timestamp not in self.sorted_hits:
            self.sorted_hits.append(timestamp)
        self.hits[timestamp] = self.hits.get(timestamp, 0) + 1
        while self.sorted_hits and timestamp - self.sorted_hits[0] > 300:
            outdated = self.sorted_hits.popleft()   # deque popleft O(1) time
            self.hits.pop(outdated, None)           # dict pop O(1) time
        
    # TC: O(1)
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        count = 0
        for i in range(timestamp -299, timestamp + 1):
            if i in self.hits:
                count += self.hits[i]
        return count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
