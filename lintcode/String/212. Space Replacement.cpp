// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param string: An array of Char
     * @param length: The true length of the string
     * @return: The true length of new string
     */
    int replaceBlank(char string[], int length) {
        // Write your code here
        for (int i=0; i<length; i++) {
            if (string[i] == ' ') {
                
                for (int j=length+1; j>i+2; j--) {
                    string[j] = string[j-2];
                }
            
                string[i] = '%';
                string[i+1] = '2';
                string[i+2] = '0';
                length += 2;
            }
        }
        
        return length;
    }
};