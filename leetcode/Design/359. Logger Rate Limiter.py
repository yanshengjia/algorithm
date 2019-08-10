"""
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

Example:

Logger logger = new Logger();

// logging string "foo" at timestamp 1
logger.shouldPrintMessage(1, "foo"); returns true; 

// logging string "bar" at timestamp 2
logger.shouldPrintMessage(2,"bar"); returns true;

// logging string "foo" at timestamp 3
logger.shouldPrintMessage(3,"foo"); returns false;

// logging string "bar" at timestamp 8
logger.shouldPrintMessage(8,"bar"); returns false;

// logging string "foo" at timestamp 10
logger.shouldPrintMessage(10,"foo"); returns false;

// logging string "foo" at timestamp 11
logger.shouldPrintMessage(11,"foo"); returns true;


Solution:
1. Circular Memory. Use a Queue to keep record of the recent messages. Everytime we have a new msg, remove all the old msg that are more than 10s earlier.
2. Instead of logging print times, store when it's ok for a message to be printed again. 
"""


# Circular Memory (Queue)
# faster than 8%
# Time: O(N), where N is the number of call function shouldPrintMessage()
# Space: O(1), up to O(10)
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []  # keep record of the recent messages
        self.size = 0

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if self.size == 0:
            self.queue.append((timestamp, message))
            self.size = 1
            return True
        else:
            while self.size > 0 and self.queue[0][0] <= timestamp - 10:
                self.queue.pop(0)
                self.size -= 1
            for i in range(self.size):
                if self.queue[i][1] == message:
                    return False
            self.queue.append((timestamp, message))
            self.size += 1
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


# Circular Memory (Queue + Hash Table)
# faster than 7%
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []  # keep record of the recent messages
        self.d = {} # keep record of the recent messages
        self.size = 0

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if self.size == 0:
            self.queue.append((timestamp, message))
            self.d[message] = timestamp
            self.size = 1
            return True
        else:
            while self.size > 0 and self.queue[0][0] <= timestamp - 10:
                t, m = self.queue.pop(0)
                self.d.pop(m)
                self.size -= 1
            if message in self.d:
                return False
            self.queue.append((timestamp, message))
            self.d[message] = timestamp
            self.size += 1
            return True



# Store when it's ok for a message to be printed again
# Weakness: HashMap soon will blew up ....
# faster than 13%
# Time: O(1)
# Space: O(N), where N is the number of msgs
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ok = {} # keep record of when it's ok for a msg to be printed again

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        if timestamp < self.ok.get(message, 0):
            return False
        self.ok[message] = timestamp + 10
        return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)