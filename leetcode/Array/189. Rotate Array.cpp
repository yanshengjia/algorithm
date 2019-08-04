// Author: Shengjia Yan
// Date: 2018-05-23 Wednesday
// Email: i@yanshengjia.com

// Time Complexity: O(n)
// Space Complexity: O(k)
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int length = nums.size();
        k %= length;
        vector<int> temp;
        
        for (int i=length-k; i<length; i++) {
            temp.push_back(nums[i]);
        }
        
        for (int j=length-k-1; j>=0; j--) {
            nums[j+k] = nums[j];
        }
        
        for (int i=0; i<k; i++) {
            nums[i] = temp[i];
        }
    }
};

// Time Complexity: O(n)
// Space Complexity: O(n)
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> t = nums;
        for (int i = 0; i < nums.size(); ++i) {
            nums[(i + k) % nums.size()] = t[i];
        }
    }
};

// Time Complexity: O(n)
// Space Complexity: O(1)
// 翻转前 n-k 个数，翻转后 k 个数，再翻转整个字符串
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        if (nums.empty() || (k %= nums.size()) == 0) return;
        int n = nums.size();
        reverse(nums.begin(), nums.begin() + n - k);
        reverse(nums.begin() + n - k, nums.end());
        reverse(nums.begin(), nums.end());
    }
};