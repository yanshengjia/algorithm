// Author: Shengjia Yan
// Date: 2017年7月24日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(s.length())
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param s A string
     * @return the length of last word
     */
    int lengthOfLastWord(string& s) {
        // Write your code here
        stringstream ss;
        ss<<s;
        string temp;
        
        while (!ss.eof()) {
            ss >> temp;
        }
        
        if (temp == "") return 0;
        else return temp.length();
    }
};