// created by sjyan @2016-11-03
// Time Complexity: O(n)    Space Complexity: O(n)

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> a;
        char s[1024];
        string str;
        
        for(int i=1; i<=n; i++)
        {
            memset(s, 0, sizeof(s));
            
            if(i%3!=0 && i%5!=0)
            {
                sprintf(s, "%d", i);
                str = s;
                a.push_back(str);
            }
            else if(i%3==0 && i%5!=0)
            {
                str = "Fizz";
                a.push_back(str);
            }
            else if(i%3!=0 && i%5==0)
            {
                str = "Buzz";
                a.push_back(str);
            }
            else
            {
                str = "FizzBuzz";
                a.push_back(str);
            }
        }
        return a;
    }
};