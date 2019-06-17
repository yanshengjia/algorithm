// Author: Shengjia Yan
// Date: 2018-04-13 Friday
// Email: i@yanshengjia.com
// Time Complexity: O(n)  n: length of string s
// Space Complexity: O(1)

class Solution {
public:
    /**
     * @param s: the given string
     * @return: all the possible states of the string after one valid move
     */
    vector<string> generatePossibleNextMoves(string &s) {
        // write your code here
        vector<string> res;
        
        int l = s.size();
        
        for (int i=0; i<l-1; i++) {
            if (s[i] == '+' && s[i+1] == '+') {
                string temp = s;
                temp[i] = '-';
                temp[i+1] = '-';
                
                // check duplicate
                if(find(res.begin(), res.end(), temp) == res.end()) {
                    res.push_back(temp);
                }   
            }
        }
        
        return res;
    }
};