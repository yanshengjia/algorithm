"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.


Solution:
Hashtable
"""


# Hashtable
# Time: O(m+n), m is number of words in A, n is number of words in B
# Space: O(m+n)
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        d = dict()
        words_a = A.split(' ')
        words_b = B.split(' ')
        
        for word in words_a:
            d[word] = d.get(word, 0) + 1
        for word in words_b:
            d[word] = d.get(word, 0) + 1
        
        res = []
        for k, v in d.items():
            if v == 1:
                res.append(k)
        return res
