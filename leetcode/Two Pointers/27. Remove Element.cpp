"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.


Solution:
1. two pointers. i: slow-runner, j: fast funner, if nums[j] != val, copy nums[j] to nums[i], i++
2. two pointers-when elements to remove are rare. i: slow-runner, j: fast funner, if nums[i] == val, swap nums[i] with the last element.
"""


class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size();
        if (size == 0) {
            return 0;
        }
        int i = 0;
        for (int j = 0; j < size; j++) {
            if (nums[j] != val) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i;
    }
};


// two pointers-when elements to remove are rare
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size();
        if (size == 0) {
            return 0;
        }
        int i = 0;
        int j = size -1;
        while (i <= j) {
            if (nums[i] == val) {
                nums[i] = nums[j];
                j--;
            }
            else {
                i++;
            }
        }
        return i;
    }
};