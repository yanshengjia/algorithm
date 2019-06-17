// Author: Shengjia Yan
// Date: 2018-05-08 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(mn)
// Space Complexity: O(m)

class Solution {
public:
    int numJewelsInStones(string J, string S) {
        int count = 0;
        int len_j = J.size();
        int len_s = S.size();
        vector<char> jewels;
        
        for (int i=0; i<len_j; i++) {
            jewels.push_back(J[i]);
        }
        
        for (int i=0; i<len_s; i++) {
            if (find(jewels.begin(), jewels.end(), S[i]) != jewels.end())
                count++;
        }
        return count;
    }
};