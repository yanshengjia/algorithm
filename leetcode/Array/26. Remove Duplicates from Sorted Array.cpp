// Author: Shengjia Yan
// Date: 2018-04-24 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
// Space Complexity: O(1)
// 用一个变量维护当前有效数字数量，同时它也可以用来给数组赋值，第n个 unique 的数字应该放在 nums[n-1] 位置上

class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int l = nums.size();
        
        if (!l) {
            return 0;
        }
        
        int counter = 1;
        
        for (int i=1; i<l; i++) {
            if (nums[i] != nums[i-1]) {
                nums[counter] = nums[i];
                counter++;
            }
        }
        
        return counter;
    }
};