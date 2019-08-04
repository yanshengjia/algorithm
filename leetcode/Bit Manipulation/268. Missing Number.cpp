// Created by sjyan @ 2017年2月24日
// Time Complexity: O(n)    Space Complexity: O(1)

class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int res = n;
        
        for(int i=0; i<n; i++)
        {
            res ^= nums[i];
            res ^= i;
        }
        
        return res;
    }
};