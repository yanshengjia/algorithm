// Author: Shengjia Yan
// Date: 2017年7月30日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n) n为字符串key长度
// Space Complexity: O(1)


class Solution {
public:
    /**
     * @param key: A String you should hash
     * @param HASH_SIZE: An integer
     * @return an integer
     */
    int hashCode(string key,int HASH_SIZE) {
        // write your code here
        int size = key.length();
        long long int sum = 0, base = 1;
        
        if (size == 0)  return 0;
        
        for (int i=size-1; i>=0; i--) {
            int t = key[i];
            sum += t * base;
            sum %= HASH_SIZE;
            base = (base * 33) % HASH_SIZE;
        }
        
        return sum;
    }
};