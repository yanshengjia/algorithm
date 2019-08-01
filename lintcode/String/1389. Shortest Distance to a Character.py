"""
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:

Input: S = "lovelintcode", C = 'e'
Output: [3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0]


Solution:
1. Scan twice. First round, store all the indexes of C in a list; Second round, get res[i] = min(i-index_before, index_after-i)
2. 将字符串按正、逆顺序两次扫描，第一次扫描计算当前位置字母与前一个目标字母之间的距离，后一次扫描计算当前位置字母与后一个字母之间的距离，两者取小即可。
"""


# time-O(N), where N is the length of S
# space-O(N)
class Solution:
    """
    @param S: 
    @param C: 
    @return: nothing
    """
    def shortestToChar(self, S, C):
        l = len(S)
        res = [0 for i in range(l)]
        indexes = []
        for i in range(l):
            if S[i] == C:
                indexes.append(i)
        print(indexes)
        
        for j in range(len(indexes)):
            if j == 0:
                for index in range(indexes[0]):
                    if S[0] == C:
                        res[index] = min(index, indexes[0]-index)
                    else:
                        res[index] = indexes[j] - index
                for index in range(indexes[0], indexes[1]+1):
                    if S[index] == C:
                        continue
                    else:
                        res[index] = min(index-indexes[0], indexes[1]-index)
            elif j == len(indexes) - 1:
                for index in range(indexes[j], l):
                    if S[-1] == C:
                        res[index] = min(l-1-index, index-indexes[j])
                    else:
                        res[index] = index - indexes[j]
            else:
                print(j)
                rg = [indexes[j], indexes[j+1]]
                print(rg)
            
                for index in range(rg[0], rg[1]+1):
                    if S[index] == C:
                        continue
                    else:
                        res[index] = min(index-rg[0], rg[1]-index)
        return res


class Solution:
    """
    @param S: 
    @param C: 
    @return: nothing
    """
    def shortestToChar(self, S, C):
        n = len(S)
        res = [n] * n
        pos = -n
        for i in range(n) + range(n)[::-1]:
            if S[i] == C: pos = i
            res[i] = min(res[i], abs(i - pos))
        return res