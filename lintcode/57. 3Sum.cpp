// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n^2)
// Space Complexity: O(n)


class Solution {
public:    
    /**
     * @param numbers : Give an array numbers of n integer
     * @return : Find all unique triplets in the array which gives the sum of zero.
     */
    vector<vector<int> > threeSum(vector<int> &nums) {
        // write your code here
        int size = nums.size();
        sort(nums.begin(), nums.end());
        vector<vector<int> > res;
        
        for (int i=0; i<size; i++) {
            int j = i+1, k = size-1;
            
            while (j < k) {
                if (nums[i] + nums[j] + nums[k] == 0) {
                    vector<int> temp;
                    temp.push_back(nums[i]);
                    temp.push_back(nums[j]);
                    temp.push_back(nums[k]);
                    
                    if(find(res.begin(), res.end(), temp) == res.end()) {
                        res.push_back(temp);
                    }
                    
                    j++;
                    k--;
                }
                else if (nums[i] + nums[j] + nums[k] > 0) {
                    k--;
                }
                else {
                    j++;
                }
            }
        }
   
        return res;
    }
};
