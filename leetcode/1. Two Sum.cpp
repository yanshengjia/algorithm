// Author: Shengjia Yan
// Date: 2018-04-09 Monday
// Email: i@yanshengjia.com
// Time Complexity: O(n^2)
// Space Complexity: O(1)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        int max = nums.size();
        
        for (int i=0; i< max; i++) {
            for (int j=i+1; j<max; j++) {
                if (nums[i] + nums[j] == target) {
                    res.push_back(i);
                    res.push_back(j);
                    return res;
                }
            }
        }
    }
};