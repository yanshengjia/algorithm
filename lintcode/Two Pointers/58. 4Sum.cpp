// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n^3)
// Space Complexity: O(n)


class Solution {
public:
    /**
     * @param numbers: Give an array numbersbers of n integer
     * @param target: you need to find four elements that's sum of target
     * @return: Find all unique quadruplets in the array which gives the sum of 
     *          zero.
     */
    vector<vector<int> > fourSum(vector<int> nums, int target) {
        // write your code here
        int size = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int> > res;
        
        for (int i=0; i<size-3; i++) {
            for (int j=i+1; j<size-2; j++) {
                int p = j+1, q = size-1;
                
                while (p < q) {
                    if (nums[i] + nums[j] + nums[p] + nums[q] == target) {
                        vector<int> temp;
                        temp.push_back(nums[i]);
                        temp.push_back(nums[j]);
                        temp.push_back(nums[p]);
                        temp.push_back(nums[q]);
                        
                        if(find(res.begin(), res.end(), temp) == res.end()) {
                            res.push_back(temp);
                        }
                        p++;
                        q--;
                    }
                    else if (nums[i] + nums[j] + nums[p] + nums[q] > target) {
                        q--;
                    }
                    else {
                        p++;
                    }
                }
            }
        }
        
        return res;
    }
};
