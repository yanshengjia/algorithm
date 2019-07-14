"""
Desc:
Given a list, each element in the list can be a list or integer. flatten it into a simply list with integers.

Solution:
Recursive:
判断 list 中的元素是否是 int 类型 (isinstance)，如果是，加入结果列表；否则调用自身。
Non-Recursive:
"""

class Solution(object):

    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        # Write your code here
        flatten_list = []
        for e in nestedList:
            if isinstance(e, int):
                flatten_list.append(e)
            else:
                flatten_list.extend(self.flatten(e))
        return flatten_list
