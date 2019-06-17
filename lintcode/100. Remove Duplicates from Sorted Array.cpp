// Author: Shengjia Yan
// Date: 2017年7月9日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param A: a list of integers
     * @return : return an integer
     */
    int removeDuplicates(vector<int> &nums) {
        // write your code here
        int size = nums.size();
        int itr = 1;
            
        while (itr < size) {
            if (nums[itr] == nums[itr - 1]) {
                nums.erase(nums.begin() + itr);
                size--;
            }
            else {
                itr++;
            }
        }
        return size;
    }
};