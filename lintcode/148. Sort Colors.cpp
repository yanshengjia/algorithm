// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution{
public:
    /**
     * @param nums: A list of integer which is 0, 1 or 2 
     * @return: nothing
     */    
    void sortColors(vector<int> &nums) {
        // write your code here
        int array[3] = {0, 0, 0};
        int size = nums.size();
        
        for (int i=0; i<size; i++) {
            array[nums[i]]++;
        }
        
        for (int p=0; p<array[0]; p++) {
            nums[p] = 0;
        }
        
        for (int y=0; y<array[1]; y++) {
            nums[array[0] + y] = 1;
        }
        
        for (int q=0; q<array[2]; q++) {
            nums[array[0] + array[1] + q] = 2;
        } 
    }
};