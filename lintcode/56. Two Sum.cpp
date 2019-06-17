// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n^2)
// Space Complexity: O(n)

class Solution {
public:
    /*
     * @param numbers : An array of Integer
     * @param target : target = numbers[index1] + numbers[index2]
     * @return : [index1+1, index2+1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        // write your code here
        int i, j;
        int size = nums.size();
        vector<int> result;
        
        for (i=0; i<size-1; i++) {
            for (j=i+1; j<size; j++) {
                if (nums[i] + nums[j] == target) {
                    result.push_back(i+1);
                    result.push_back(j+1);
                    return result;
                }
            }
        }
        
    }
};
