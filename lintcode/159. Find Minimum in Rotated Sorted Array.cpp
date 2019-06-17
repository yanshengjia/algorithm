// Author: Shengjia Yan
// Date: 2017年8月4日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)  n为数组长度
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param nums: a rotated sorted array
     * @return: the minimum number in the array
     */
    int findMin(vector<int> &nums) {
        // write your code here
        int min = nums[0];
        int size = nums.size();
        
        for (int i=1; i<size; i++) {
            if (nums[i] < nums[i-1]) {
                min = nums[i];
                break;
            }
        }
        
        return min;
    }
};