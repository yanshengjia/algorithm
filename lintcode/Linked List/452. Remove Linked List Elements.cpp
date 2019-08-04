// Author: Shengjia Yan
// Date: 2017年7月1日
// Email: sjyan@seu.edu.cn
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
    /**
     * @param head a ListNode
     * @param val an integer
     * @return a ListNode
     */
    ListNode *removeElements(ListNode *head, int val) {
        // Write your code here
        if (head == NULL)
            return head;

        ListNode *p = head, *q = head->next;

        while (q != NULL) {
            if (q->val == val) {
                p->next = q->next;
                q = q->next;
            }
            else {
                p = p->next;
                q = q->next;
            }
        }

        if (head->val == val)
            head = head->next;

        return head;
    }
};