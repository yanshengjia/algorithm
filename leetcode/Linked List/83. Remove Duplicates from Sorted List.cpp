// Author: Shengjia Yan
// Date: 2018-05-07 Monday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *cur = head;
        
        while (cur && cur->next) {
            if (cur->val == cur->next->val) {
                cur->next = cur->next->next;
            } else {
                cur = cur->next;
            }
        }
        return head;
    }
};


class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head || !head->next)   return head;
        
        ListNode *guard = head;
        ListNode *pre = guard;
        ListNode *cur = guard->next;
        
        while (cur->next) {
            if (pre->val == cur->val) {
                pre->next = cur->next;
                cur = cur->next;
            }
            else {
                pre = pre->next;
                cur = cur->next;
            }
        }
        
        if (pre->val == cur->val) {
            pre->next = cur->next;
        }
        
        return guard;
    }
};