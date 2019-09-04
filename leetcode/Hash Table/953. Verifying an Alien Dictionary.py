"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.


Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).


Solution:
Use a Hash table to record the mapping of chars and orders.
Then check the adjacent words.
"""


# Check adjacent words
# Time: O(N), where N is the total content of words
# Space: O(1)
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        d = dict()
        for i, o in enumerate(order):
            d[o] = i
        
        l = len(words)
        if l == 1:
            return True
        for i in range(l-1):
            left, right = words[i], words[i+1]
            ll, lr = len(left), len(right)
            c = 0
            while c < min(ll, lr):
                if d[left[c]] < d[right[c]]:
                    break
                if d[left[c]] > d[right[c]]:
                    return False
                c += 1
            if ll > c and c == lr:
                return False
        return True
