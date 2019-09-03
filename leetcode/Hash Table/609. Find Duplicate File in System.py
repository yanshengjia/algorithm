"""
Given a list of directory info including directory path, and all the files with contents in this directory, you need to find out all the groups of duplicate files in the file system in terms of their paths.

A group of duplicate files consists of at least two files that have exactly the same content.

A single directory info string in the input list has the following format:

"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"

It means there are n files (f1.txt, f2.txt ... fn.txt with content f1_content, f2_content ... fn_content, respectively) in directory root/d1/d2/.../dm. Note that n >= 1 and m >= 0. If m = 0, it means the directory is just the root directory.

The output is a list of group of duplicate file paths. For each group, it contains all the file paths of the files that have the same content. A file path is a string that has the following format:

"directory_path/file_name.txt"

Example 1:

Input:
["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]
Output:  
[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]


Solution:
Use a Hashtable to record the mapping of file contents and file paths.
Remember: A group of duplicate files consists of at least two files that have exactly the same content.
You are the best!
"""


# Hash Table
# Time: O(n*x), n strings of average length x is parsed.
# Space: O(n*x), d and res size grows upto n*xn∗x.
import collections
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for path in paths:
            s = path.split(' ')
            prefix = s[0]
            for i in range(1, len(s)):
                ss = s[i].split('(')
                filename = ss[0]
                content = ss[1][:-1]
                d[content].append('{}/{}'.format(prefix, filename))
        
        res = []
        for k, v in d.items():
            if len(v) >= 2:
                res.append(v)
        return res
