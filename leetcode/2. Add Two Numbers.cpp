// Author: Shengjia Yan
// Date: 2018-04-24 Tuesday
// Email: i@yanshengjia.com
// Time Complexity: O(m+n)
// Space Complexity: O(1)
// 注意 l1 l2 为空的边界情况

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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *res = new ListNode(-1);
        ListNode *temp = res;
        int carry = 0;
        
        while (l1 && l2) {
            int add = (l1->val + l2->val + carry) % 10;
            carry = (l1->val + l2->val + carry ) / 10;
            temp->next = new ListNode(add);
            temp = temp->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        
        while (l1) {
            int data = (l1->val + carry) % 10;
            carry = (l1->val + carry) / 10;
            temp->next = new ListNode(data);
            temp = temp->next;
            l1 = l1->next;
        }
        
        while (l2) {
            int data = (l2->val + carry) % 10;
            carry = (l2->val + carry) / 10;
            temp->next = new ListNode(data);
            temp = temp->next;
            l2 = l2->next;
        }
        
        if (carry) {
            temp->next = new ListNode(carry);
        }
        return res->next;
    }
};