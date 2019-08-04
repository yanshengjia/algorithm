// Author: Shengjia Yan
// Date: 2018-04-09 Monday
// Email: i@yanshengjia.com
// Time Complexity: O(min(m, n))
// Space Complexity: O(1)
// No recursion, compare two heads

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
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *guard = new ListNode(0);
        ListNode *current = guard;

        while (l1 != NULL && l2 != NULL) {
            if (l1->val < l2->val) {
                current->next = l1;
                l1 = l1->next;
            } else {
                current->next = l2;
                l2 = l2->next;
            }
            current = current->next;
        }

        if (l1 != NULL) {
            current->next = l1;
        } else {
            current->next = l2;
        }
        
        return guard->next;
    }
};