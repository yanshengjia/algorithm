"""
Write a class RecentCounter to count recent requests.

It has only one method: ping(int t), where t represents some time in milliseconds.

Return the number of pings that have been made from 3000 milliseconds ago until now.

Any ping with time in [t - 3000, t] will count, including the current ping.

It is guaranteed that every call to ping uses a strictly larger value of t than before.


Example 1:

Input：["RecentCounter","ping","ping","ping","ping"],[[],[1],[100],[3001],[3002]]
Output：[null,1,2,3,3]
Explanation：
The list of time of calls is [1,100,3001,3002].
1.call "RecentCounter" gets null.
2.call "ping",the range of time is[0,1],there is a call(t=1).
3.call "ping",the range of time is[0,100],there are two calls(t=1,t=100).
4.call "ping",the range of time is[1,3001],there are three calls(t=1,t=100,t=3001).
5.call "ping",the range of time is[2,3002],there are three calls(t=100,3001,3002).


Solution:
Use a list to maintain a circular buffer
"""


class RecentCounter:

    def __init__(self):
        self.requests = []
        self.size = 0
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        self.size += 1
        while self.size > 1 and self.requests[0] < t - 3000:
            del self.requests[0]
            self.size -= 1
        return self.size
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
