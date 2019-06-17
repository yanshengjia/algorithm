// Created by sjyan @2016-11-11
// Time Complexity: O(n)    Space Complexity: O(1)

class Solution {
public:
  int majorityElement(vector<int> &nums) {
    int major;
    int count = 0;

    for (int i = 0; i < nums.size(); i++) {
      if (count == 0) {
        major = nums[i];
        count = 1;
      } else {
        if (major == nums[i])
          count++;
        else
          count--;
      }
    }
    return major;
  }
};
