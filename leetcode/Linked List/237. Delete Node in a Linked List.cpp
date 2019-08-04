// Author: Shengjia Yan
// Date: 2018-05-23 Wednesday
// Email: i@yanshengjia.com
// Time Complexity: O(1)
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
    void deleteNode(ListNode* node) {
        if (node->next == NULL) {
            node = NULL;
        }
        else {
            node->val = node->next->val;
            node->next = node->next->next;
        }
    }
};