"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.

Follow up:
Try to solve it in O(n log k) time and O(n) extra space.


Solution:
1. Hashmap + Sort  (-frequency, word)
2. Heap  MinHeap (-frequency, word)
"""


# Hashmap + Sort
# Time: O(NlogN), where N is the number of words
# Space: O(N)
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = dict()
        for word in words:
            d[word] = d.get(word, 0) + 1
        
        sorted_words = sorted(d.items(), key = lambda k: (-k[1], k))
        res = [sorted_words[i][0] for i in range(k)]
        return res


# Heap
# Time: O(Nlogk), >99%, where NN is the length of words. We count the frequency of each word in O(N) time, then we add N words to the heap, each in O(logk) time. Finally, we pop from the heap up to kk times. As k≤N, this is O(Nlogk) in total.
# In Python, we improve this to O(N+klogN): our heapq.heapify operation and counting operations are O(N), and each of k heapq.heappop operations are O(logN).
# Space Complexity: O(N), the space used to store our count.
import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = dict()
        for word in words:
            d[word] = d.get(word, 0) + 1
        
        heap = [(-freq, word) for word, freq in d.items()]
        heapq.heapify(heap)
        res = [heapq.heappop(heap)[1] for _ in range(k)]
        return res
        