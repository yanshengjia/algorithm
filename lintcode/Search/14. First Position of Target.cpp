// Author: Shengjia Yan
// Date: 2017年7月27日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(logn) n为数组长度
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param nums: The integer array.
     * @param target: Target number to find.
     * @return: The first position of target. Position starts from 0. 
     */
    int binarySearch(vector<int> &array, int target) {
        // write your code here
        long long int size = array.size();
        
        if (size == 0) {
            return -1;
        }
        
        long long int left = 0, right = size - 1;
        
        while (left + 1 < right) {
            long long int mid = (left + right) / 2;
            
            if (array[mid] >= target) {
                right = mid;
            }
            else {
                left = mid;
            }
        }
        
        if (array[left] == target)  return left;
        if (array[right] == target) return right;
        
        return -1;
    }
};