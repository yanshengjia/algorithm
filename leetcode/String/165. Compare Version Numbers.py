"""
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.

The . character does not represent a decimal point and is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

You may assume the default revision number for each level of a version number to be 0. For example, version number 3.4 has a revision number of 3 and 4 for its first and second level revision number. Its third and fourth level revision number are both 0.


Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
Example 4:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both “01” and “001" represent the same number “1”
Example 5:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: The first version number does not have a third level revision number, which means its third level revision number is default to "0"


Solution:
Split the version number and strip the leading zeros.
Remove all the zeros from the end.
Compare one by one.
"""


# > 71%
# Time: O(m), m is min(len(v1), len(v2))
# Space: O(M+N), where M is the length of v1, N is the length of v2
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1, v2 = version1.split('.'), version2.split('.')
        v1 = [int(i) for i in v1]
        v2 = [int(i) for i in v2]
        
        while len(v1) > 1 and v1[-1] == 0:
            v1.pop()
        while len(v2) > 1 and v2[-1] == 0:
            v2.pop()
        
        len1, len2 = len(v1), len(v2)
        for i in range(min(len1, len2)):
            val1 = v1[i]
            val2 = v2[i]
            if val1 > val2:
                return 1
            elif val1 < val2:
                return -1
            else:
                continue
        if len2 == len1:
            return 0
        elif len2 > len1:
            return -1
        else:
            return 1