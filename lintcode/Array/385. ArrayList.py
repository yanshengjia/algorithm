"""
Description:
Implement an ArrayListManager which can:

create(n). Create an ArrayList of integers contains [0, 1, 2, ... n-1]
clone(list). Clone a list. The cloned list should independent with the original list.
get(list, index). Get the element on the index position of the list.
set(list, index, val). Change the value the element of index position to given val.
remove(list, index). Remove the element on the index position.
indexOf(list, val). Find the first index of element that equals to val and return its index.


Solution:
模拟题，注意异常处理，异常都返回 -1
list[:] 返回的是一个新的 list
"""


class ArrayListManager:
    '''
     * @param n: You should generate an array list of n elements.
     * @return: The array list your just created.
    '''
    def create(self, n):
        # Write your code here
        return [i for i in range(n)]

    
    '''
     * @param list: The list you need to clone
     * @return: A deep copyed array list from the given list
    '''
    def clone(self, list):
        # Write your code here
        return list[:]
    
    
    '''
     * @param list: The array list to find the kth element
     * @param k: Find the kth element
     * @return: The kth element
    '''
    def get(self, list, k):
        # Write your code here
        l = len(list)
        if k >= l:
            return -1
        else:
            return list[k]
    
    
    '''
     * @param list: The array list
     * @param k: Find the kth element, set it to val
     * @param val: Find the kth element, set it to val
    '''
    def set(self, list, k, val):
        # write your code here
        if k >= len(list):
            return -1
        else:
            list[k] = val
    
    
    '''
     * @param list: The array list to remove the kth element
     * @param k: Remove the kth element
    '''
    def remove(self, list, k):
        # write tour code here
        del list[k]
    
    '''
     * @param list: The array list.
     * @param val: Get the index of the first element that equals to val
     * @return: Return the index of that element
    '''
    def indexOf(self, list, val):
        # Write your code here
        if val not in list:
            return -1
        return list.index(val)