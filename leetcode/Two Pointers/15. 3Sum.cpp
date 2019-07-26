// Author: Shengjia Yan
// Date: 2018-05-16 Wednesday
// Email: i@yanshengjia.com
// Time Complexity: O(n^2 + nlogn)
// Space Complexity: O(1)

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int size = nums.size();
        vector<vector<int> > res;
        
        if (size < 3)   return res;
        
        for (int i=0; i<size-2; i++) {
            int p = i+1, q = size - 1;
            if (nums[i] > 0)  continue;
            if (i > 0 && nums[i] == nums[i-1])  continue;
            
            while (p < q) {
                int sum = nums[i] + nums[p] + nums[q];
                if (sum == 0) {
                    vector<int> triplet;
                    triplet.push_back(nums[i]);
                    triplet.push_back(nums[p]);
                    triplet.push_back(nums[q]);
                    res.push_back(triplet);
                    while (p < q && nums[p] == nums[p+1])  p++;
                    while (p < q && nums[q] == nums[q-1])  q--;
                    p++;
                    q--;
                }
                else if (sum > 0) {
                    while (p < q && nums[q] == nums[q-1])  q--;
                    q--;
                }
                else {
                    while (p < q && nums[p] == nums[p+1])  p++;
                    p++;
                }       
            }
        }
        return res;
    }
};