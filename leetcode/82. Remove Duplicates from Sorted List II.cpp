// Author: Shengjia Yan
// Date: 2018-05-08 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(n)
// Space Complexity: O(n)

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
        if (head == NULL || head->next == NULL) {
            return head;
        }
        
        ListNode *move = new ListNode(0);
        ListNode *newhead = move;
        ListNode *pre = head, *mid = head->next;
        
        if (pre->val != mid->val) {
            move->next = new ListNode(pre->val);
            move = move->next;
        }
        
        while (mid->next) {
            if (pre->val != mid->val && mid->val != mid->next->val) {
                move->next = new ListNode(mid->val);
                move = move->next;
            }
            pre = pre->next;
            mid = mid->next;
        }
        
        if (pre->val != mid->val) {
            move->next = new ListNode(mid->val);
        }
           
        return newhead->next;
    }
};