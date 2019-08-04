// Author: Shengjia Yan
// Date: 2017年7月29日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param heights: a vector of integers
     * @return: an integer
     */
    int maxArea(vector<int> &heights) {
        // write your code here
        int size = heights.size();
        if (size == 0 || size == 1) return 0;
        
        int left = 0, right = size -1, area = 0;
        
        while (left < right) {
            if (heights[left] < heights[right]) {
                int temp = heights[left] * (right - left);
                if (temp > area) {
                    area = temp;
                }
                left++;
            }
            else {
                int temp = heights[right] * (right - left);
                if (temp > area) {
                    area = temp;
                }
                right--;
            }
        }
        
        return area;
    }
};