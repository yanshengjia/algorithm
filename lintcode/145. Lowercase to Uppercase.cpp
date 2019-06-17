// Author: Shengjia Yan
// Date: 2018-04-08 Sunday
// Email: i@yanshengjia.com
// Time Complexity: O(1)
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param character: a character
     * @return: a character
     */
    char lowercaseToUppercase(char character) {
        // write your code here
        char upper = character + 'A' - 'a';
        return upper;
    }
};