// Author: Shengjia Yan
// Date: 2018-05-29 Tuesday
// Email: i@yanshengjia.com

// Time Complexity: O(2n)
// Space Complexity: O(1)
// two pass
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int red_count = 0;
        int white_count = 0;
        int blue_count = 0;
        int size = nums.size();
        
        for (int i=0; i<size; i++) {
            if (nums[i] == 0)
                red_count ++;
            else if (nums[i] == 1)
                white_count ++;
            else
                blue_count ++;
        }
        
        for (int i=0; i<size; i++) {
            if (i < red_count)
                nums[i] = 0;
            else if (i >= red_count && i < red_count + white_count)
                nums[i] = 1;
            else
                nums[i] = 2;
        }
    }
};


// one pass
class Solution {
public:
    void sortColors(vector<int>& nums) {
        int size = nums.size();
        int red = 0, blue = size - 1;
        
        for (int i = 0; i <= blue; i++) {
            if (nums[i] == 0) {
                swap(nums[red], nums[i]);
                red++;
            }
            else if (nums[i] == 2) {
                swap(nums[blue], nums[i]);
                blue--;
                i--;
            }
        }
    }
    
    void swap(int &a, int &b) {
        int t = a;
        a = b;
        b = t;
    }
};