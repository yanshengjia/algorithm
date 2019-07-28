"""
We are given two sentences A and B. (A sentence is a string of space separated words. Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Solution:
Use hashmap to record occurrence number of words in A, B
"""


class Solution:
    """
    @param A: Sentence A
    @param B: Sentence B
    @return: Uncommon Words from Two Sentences
    """
    def uncommonFromSentences(self, A, B):
        # Write your code here.
        wordlist_a = A.strip().split()
        wordlist_b = B.strip().split()
        
        d_a, d_b = dict(), dict()
        
        list_a = self.find_unique_words(wordlist_a, d_a)
        list_b = self.find_unique_words(wordlist_b, d_b)
        
        res = []
        for w in list_a:
            if w not in wordlist_b:
                res.append(w)
        
        for w in list_b:
            if w not in wordlist_a:
                res.append(w)
        return res
    
    def find_unique_words(self, wordlist, d):
        for word in wordlist:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        
        unique_wordlist = []
        for k, v in d.items():
            if v == 1:
                unique_wordlist.append(k)
        return unique_wordlist
