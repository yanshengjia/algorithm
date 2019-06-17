// Author: Shengjia Yan
// Date: 2018-05-23 Wednesday
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
    ListNode* reverseList(ListNode* head) {
        if (head == NULL || head->next == NULL)
            return head;
        
        ListNode *p = head;
        ListNode *y = head->next;
        ListNode *q;
        head->next = NULL;
        
        while (y) {
            q = y->next;    // 保存下一次循环要处理的指针
            y->next = p;
            p = y;
            y = q;
        }
        return p;
    }
};