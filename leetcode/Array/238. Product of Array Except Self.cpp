// Created by sjyan @2017-02-21
// Time Complexity: O(n)    Space Complexity: O(n)

class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int size = nums.size();
        
        vector<int> res(size);
        vector<int> begin(size);    // 顺序存储 nums 阶乘
        vector<int> end(size);      // 逆序存储 nums 阶乘
        
        begin[0] = 1;
        end[0] = 1;
        
        for(int i=1; i<size; i++)
        {
            begin[i] = begin[i-1]*nums[i-1];
            end[i] = end[i-1]*nums[size-i];
        }
        
        for(int j=0; j<size; j++)
        {
            res[j] = begin[j]*end[size-j-1];
        }
        
        return res;
    }
};