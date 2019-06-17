"""
Author: Shengjia Yan
Date: 2018-05-11 Friday
Email: i@yanshengjia.com
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        res = []
        
        for word in words:
            l = len(word)
            new_word = ''
            for i in range(l):
                new_word += word[l-i-1]
            res.append(new_word)
        
        new_s = (' ').join(res)
        return new_s
        