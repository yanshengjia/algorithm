// Author: Shengjia Yan
// Date: 2017年7月30日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n+x) n为dictionary大小，x为最长单词的个数
// Space Complexity: [O(x), O(n)] 


class Solution {
public:
    /**
     * @param dictionary: a vector of strings
     * @return: a vector of strings
     */
    vector<string> longestWords(vector<string> &dictionary) {
        // write your code here
        stack<string> cache;
        vector<string> res;
        int size = dictionary.size();
        int max = 0, length = 0;
        
        if (size == 0)  return res;
        
        for (int i=0; i<size; i++) {
            length = dictionary[i].length();
            
            if (length >= max) {
                cache.push(dictionary[i]);
                max = length;
            }
        }
        
        while (!cache.empty()) {
            string str = cache.top();
            length = str.length();
            
            if (length == max) {
                res.push_back(str);
                cache.pop();
            } else {
                break;
            }
        }
        
        return res;
    }
};