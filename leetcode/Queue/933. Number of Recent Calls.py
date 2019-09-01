"""
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.


Example 1:

Input: inputs = ["RecentCounter","ping","ping","ping","ping"], inputs = [[],[1],[100],[3001],[3002]]
Output: [null,1,2,3,3]


Solution:
Queue + Circular Memory
Keep a queue of the most recent calls in increasing order of t.
When we see a new call with time t, remove all calls that occurred before t - 3000.
"""


# Use a list to mimic Queue
# > 20%
class RecentCounter:

    def __init__(self):
        self.cache = []


    def ping(self, t: int) -> int:
        while len(self.cache) >= 1 and self.cache[0] < t - 3000:
            self.cache.pop(0)
        self.cache.append(t)
        return len(self.cache)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



# Use deque
# > 60% faster
import collections
class RecentCounter:

    def __init__(self):
        self.q = collections.deque()


    def ping(self, t: int) -> int:
        self.q.append(t)
        while self.q[0] < t - 3000:
            self.q.popleft()
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

