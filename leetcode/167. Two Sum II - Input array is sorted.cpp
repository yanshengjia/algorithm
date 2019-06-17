// Created by sjyan @2017-02-23
// Time Complexity: O(n)    Space Complexity: O(1)

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int i = 0;
        int j = numbers.size()-1;
        
        while(i<j)
        {
            if(numbers[i] + numbers[j] == target)
            {
                vector<int> result{i+1, j+1};
                return result;
            }
            else if(numbers[i] + numbers[j] > target)
            {
                j--;
            }
            else
            {
                i++;
            }
        }
    }
};