// Created by sjyan @2016-11-11
// Time Complexity: O(n)    Space Complexity: O(1)

class Solution {
public:
  void moveZeroes(vector<int> &nums) {
    int length = nums.size();

    for (int i = 0; i < length; i++) {
      if (nums[i] == 0) {
        nums.erase(nums.begin() + i);
        nums.push_back(0);
        i--;
        length--;
      }
    }
  }
};
