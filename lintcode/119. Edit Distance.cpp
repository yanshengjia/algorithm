// Author: Shengjia Yan
// Date: 2018-04-29 Sunday
// Email: i@yanshengjia.com
// Time Complexity: O(mn)
// Space Complexity: O(mn)

#include <iostream>
#include <string>
using namespace std;

/*  
    edit(i, j): edit distance between string1 (length == i) and string2 (length == j)
    edit(i, j) = min{
                        edit(i-1, j) + 1,
                        edit(i, j-1) + 1,
                        edit(i-1, j-1) + f(i, j)
                    }
    
    f(i, j) = {
        0, if str1[i-1] == str2[j-1];
        1, if str1[i-1] != str2[j-1];
    }
*/

class Solution {
public:
    /**
     * @param word1: A string
     * @param word2: A string
     * @return: The minimum number of steps.
     */
    int minDistance(string &word1, string &word2) {
        // write your code here
        int a[1000][1000];  // a[i][j]: edit(i, j)
        int l1 = word1.size();
        int l2 = word2.size();

        for (int i=0; i<=l1; i++) {
            a[i][0] = i;
        }

        for (int j=0; j<=l2; j++) {
            a[0][j] = j;
        }

        for (int i=1; i<=l1; i++) {
            for (int j=1; j<=l2; j++) {
                int t1 = a[i-1][j] + 1;
                int t2 = a[i][j-1] + 1;
                int t3 = (word1[i-1] == word2[j-1] ? a[i-1][j-1] : a[i-1][j-1] + 1);
                
                int min = (t1 < t2 ? t1 : t2);
                min = (t3 < min ? t3 : min);
                a[i][j] = min;
            }
        }

        return a[l1][l2];
    }
};

int main() {
    Solution test;
    string s1 = "abcde";
    string s2 = "abdef";

    int edit_distance = test.minDistance(s1, s2);
    cout << edit_distance << endl;

    return 0;
}