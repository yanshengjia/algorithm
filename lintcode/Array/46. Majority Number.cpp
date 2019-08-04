// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param nums: A list of integers
     * @return: The majority number
     */
    int majorityNumber(vector<int> nums) {
        // write your code here
        int size = nums.size();
        int major = nums[0];
        int count = 0;
        
        for (int i=1; i<size; i++) {
            if (nums[i] == major) {
                count++;
            }
            else {
                count--;
            }
            
            if (count == -1) {
                major = nums[i+1];
                count = 0;
                i++;
            }
        }

        return major;
    }
};
