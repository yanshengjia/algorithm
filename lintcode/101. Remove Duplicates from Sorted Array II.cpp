// Author: Shengjia Yan
// Date: 2017年8月14日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)  n为数组大小
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
        int count = 1;
            
        while (itr < size) {
            if (nums[itr] == nums[itr - 1]) {
                if (count < 2) {
                    count = 2;
                    itr++;
                }
                else {
                    nums.erase(nums.begin() + itr);
                    size--;
                }
            }
            else {
                count = 1;
                itr++;
            }
        }
        return size;
    }
};