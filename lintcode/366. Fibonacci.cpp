// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
// Time Complexity: O(n)
// Space Complexity: O(1)


class Solution{
public:
    /**
     * @param n: an integer
     * @return an integer f(n)
     */
    int fibonacci(int n){
        // write your code here
        long long int result = 1;
        long long int prev_result = 1;
        long long int next_result = 0;
        
        if (n == 1)
            return 0;
        else if (n == 2)
            return 1;
        else{
            while (n > 2){
                n--;
                prev_result = next_result;
                next_result = result;
                result = prev_result + next_result;
            }
            return result;
        }
    }
};
