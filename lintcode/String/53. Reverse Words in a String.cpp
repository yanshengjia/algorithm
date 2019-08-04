// Author: Shengjia Yan
// Date: 2017年7月18日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(n)
// 本题中的翻转实际上是字符串中的单词逆序一下，并不是将单词中的字符翻转，LintCode 的题意表达不明

class Solution {
public:
    /**
     * @param s : A string
     * @return : A string
     */
    string reverseWords(string s) {
        // write your code here
        string res = "";
        vector<string> repo;
        stringstream str;
        str.clear();
        str<<s;
        
        while(!str.fail()) {
            string temp;
            str>>temp;
            repo.push_back(temp);
        }
        
        int size = repo.size();
        
        for (int i=size-1; i>=0; i--) {
            res += repo[i];
            res += " ";
        }
        
        res = res.substr(1, res.length()-1);
        return res;
    }
};