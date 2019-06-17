// Author: Shengjia Yan
// Date: 2018-04-20 Friday
// Email: i@yanshengjia.com
// Time Complexity: O(n)  n: the length of potential circle
// Space Complexity: O(1)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        ListNode *fast, *slow;
        fast = slow = head;
        
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
            if (fast == slow)
                return true;
        }
        return false;
    }
};