// Author: Shengjia Yan
// Date: 2017年7月19日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(n)

class Solution {
public:
    /**
     * @param nums: a vector of integers
     * @return: nothing
     */
    void partitionArray(vector<int> &nums) {
        // write your code here
        vector<int> odd, even;
        int size = nums.size();
        
        for (int i=0; i<size; i++) {
            if (nums[i] % 2 == 0) {
                even.push_back(nums[i]);
            }
            else {
                odd.push_back(nums[i]);
            }
        }
        
        nums.clear();
        
        int size_odd = odd.size();
        int size_even = even.size();
        
        for(int i=0; i<size_odd; i++)
            nums.push_back(odd[i]);
        
        for(int i=0; i<size_even; i++)
            nums.push_back(even[i]);
    }
};