// Author: Shengjia Yan
// Date: 2018-04-08 Sunday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
// Space Complexity: O(n)


class Solution {
public:
    /**
     * @param head: the given linked list
     * @return: the array that store the values in reverse order 
     */
    vector<int> reverseStore(ListNode * head) {
        // write your code here
        vector<int> result;
        stack<int> cache;
        
        while(head != NULL) {
            cache.push(head->val);
            head = head->next;
        }
        
        while(!cache.empty()) {
            result.push_back(cache.top());
            cache.pop();
        }
        return result;
    }
};