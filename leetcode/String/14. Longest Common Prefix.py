"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Solution:
1. Horizontal Scanning 
水平扫描一遍数组，假设最大前缀是第一个词，在扫描过程中不断更新最大前缀
LCP(S1...SN) = LCP(LCP(LCP(LCP(S1, S2), S3), S4)...SN)

2. Vertical scanning
垂直扫描，依次比较每个词的每一个列
Imagine a very short string is at the end of the array. The above approach will still do S comparisons. One way to optimize this case is to do vertical scanning. We compare characters from top to bottom on the same column (same character index of the strings) before moving on to the next column.

3. Divide and Conquer
类似于归并排序，每次把搜索空间切两半，分别求 LCP，然后把结果合并
"""


# Horizontal Scanning
# Time: O(S), where S is the sum of all characters in all strings.
# Space: O(1), constant space
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        res = strs[0]
        for i in range(1, len(strs)):
            s = strs[i]
            last = 0
            while last < len(s):
                if last < len(res) and res[last] == s[last]:
                    last += 1
                else:
                    break
            res = s[:last]
        return res
        