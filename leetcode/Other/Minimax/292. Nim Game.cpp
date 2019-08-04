// created by sjyan @2016-11-03
// Time Complexity: O(1)    Space Complexity: O(1)

class Solution {
public:
    bool canWinNim(int n) {
        if(n%4 == 0)
            return false;
        else 
            return true;
    }
};