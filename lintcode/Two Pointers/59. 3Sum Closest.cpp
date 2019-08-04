// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n^2)
// Space Complexity: O(1)


class Solution {
public:    
    /**
     * @param numbers: Give an array numbers of n integer
     * @param target: An integer
     * @return: return the sum of the three integers, the sum closest target.
     */
    int threeSumClosest(vector<int> nums, int target) {
        // write your code here
        int size = nums.size();
        sort(nums.begin(), nums.end());
        int diff = 0x7fffffff;
        int sum = 0;
        
        for (int i=0; i<size; i++) {
            int j = i+1, k = size-1;
            
            while (j < k) {
                int temp = nums[i] + nums[j] + nums[k];
                
                if (abs(target - temp) < diff) {
                    diff = abs(target - temp);
                    sum = temp;
                }
                
                if (temp == target) {
                    return temp;
                }
                else if (temp < target) {
                    j++;
                }
                else {
                    k--;
                }
            }
        }
        
        return sum;
    }
};
