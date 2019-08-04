// Author: Shengjia Yan
// Date: 2018-05-09 Wednesday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
// Space Complexity: O(n)

class Solution {
public:
    int uniqueMorseRepresentations(vector<string>& words) {
        string morse[] = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
        
        int size = words.size();
        vector<string> res;
        
        for (int i=0; i<size; i++) {
            string word = words[i];
            int l = word.size();

            string m = "";

            for (int j=0; j<l; j++) {
                m += morse[word[j] - 'a'];
            }
            
            if (find(res.begin(), res.end(), m) == res.end())
                res.push_back(m);
        }
        
        return res.size();
    }
};