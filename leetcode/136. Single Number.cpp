// Created by sjyan @2016-11-09
// Time Complexity: O(n)
// Space Complexity: O(1)

class Solution {
public:
  int singleNumber(vector<int> &nums) {
    int number = nums[0];

    for (int i = 1; i < nums.size(); i++) {
      number ^= nums[i];
    }

    return number;
  }
};
