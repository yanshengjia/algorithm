// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(n)


class Solution {
public:
    /*
     * @param nums an array of Integer
     * @param target = nums[index1] + nums[index2]
     * @return [index1 + 1, index2 + 1] (index1 < index2)
     */
    vector<int> twoSum(vector<int> &nums, int target) {
        // write your code here
        int size = nums.size();
        vector<int> res;
        
        int i = 0, j = size - 1;
        
        while (i < j) {
            if (nums[i] + nums[j] == target) {
                res.push_back(i+1);
                res.push_back(j+1);
                break;
            }
            else if (nums[i] + nums[j] > target) {
                j--;
            }
            else {
                i++;
            }
        }
        
        return res;
    }
};
